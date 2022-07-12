import FWCore.ParameterSet.Config as cms

process = cms.Process('LL')

process.load('PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

## ----------------- Global Tag -----------------
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_hlt_GRun', '')

#--------------------- Report and output ---------------------------   
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.TFileService=cms.Service("TFileService",
                                 fileName=cms.string("output.root")
)

process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
        wantSummary = cms.untracked.bool(False),
)

##-------------------- Define the source  ----------------------------
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:step0_HLT.root'
    )
)

##--- l1 stage2 digis ---
process.load("EventFilter.L1TRawToDigi.gtStage2Digis_cfi")
process.gtStage2Digis.InputLabel = cms.InputTag( "hltFEDSelectorL1" )

##-------------------- User analyzer  --------------------------------
#import trigger conf
process.egammaReconstruction = cms.EDAnalyzer(
    'egTreeProducer',
    electron = cms.InputTag('hltEgammaGsfElectrons'),
)

# ------------------ path --------------------------
process.p = cms.Path(process.egammaReconstruction)
