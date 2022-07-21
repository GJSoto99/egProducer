#ifndef EGTREEPRODUCER_H
#define EGTREEPRODUCER_H

// Standard C++ includes
#include <memory>
#include <vector>
#include <iostream>

// ROOT includes
#include "TTree.h"
#include "TLorentzVector.h"
#include "TPRegexp.h"

// CMSSW framework includes
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h" 

// CMSSW data formats
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/EgammaReco/interface/ElectronSeed.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "DataFormats/EgammaCandidates/interface/Electron.h"
#include "DataFormats/TrackReco/interface/TrackBase.h" 
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// Other relevant CMSSW includes
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "L1Trigger/L1TGlobal/interface/L1TGlobalUtil.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionData.h"


class egTreeProducer : public edm::one::EDAnalyzer<edm::one::SharedResources, edm::one::WatchRuns, edm::one::WatchLuminosityBlocks> {
	public:
		explicit egTreeProducer(const edm::ParameterSet&);
		~egTreeProducer();
		
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
	private:
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;

        virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        
        const edm::EDGetTokenT<std::vector<reco::Electron>>  electronToken;

        TTree* tree;

		std::vector<float>  electron_pt;
		std::vector<float>  electron_eta;
		std::vector<float>  electron_phi;
		std::vector<float>  electron_mass;	//new
		std::vector<int>    electron_charge;	//new
		

		int run_, lumi_, event_;

};

//Constructor
egTreeProducer::egTreeProducer(const edm::ParameterSet& iConfig): 
				electronToken  (consumes<std::vector<reco::Electron> >(iConfig.getParameter<edm::InputTag>("electron")))
{
	usesResource("TFileService");	
}

//destructor
egTreeProducer::~egTreeProducer() {}

void egTreeProducer::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup) {}

void egTreeProducer::beginJob() 
{

	// Access the TFileService
	edm::Service<TFileService> fs; 
  
    // Create the TTree
    tree = fs->make<TTree>("tree"  , "tree");

    tree->Branch("event"  ,&event_ , "event/I");   
    tree->Branch("lumi"   ,&lumi_  , "lumi/I");  
    tree->Branch("run"    ,&run_   , "run/I");    

    tree->Branch("electron_pt" , "std::vector<float>", &electron_pt  , 32000, 0);
    tree->Branch("electron_eta", "std::vector<float>", &electron_eta , 32000, 0);
    tree->Branch("electron_phi", "std::vector<float>", &electron_phi , 32000, 0);
    tree->Branch("electron_mass", "std::vector<float>", &electron_mass , 3200, 0);	//new
    tree->Branch("electron_charge", "std::vector<int>", &electron_charge , 3200, 0); 	//new

    return ;
}

void egTreeProducer::endJob() {}
void egTreeProducer::endRun(edm::Run const&, edm::EventSetup const&) {}

void egTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

    using namespace edm;
    using namespace std;
    
	std::cout << "entered here \n" ;

	run_ = 0;
	lumi_= 0;
	event_ = 0;

	electron_pt.clear();
	electron_eta.clear();
	electron_phi.clear();
	electron_mass.clear();		//new
	electron_charge.clear();	//new


    Handle<vector<reco::Electron>> electronH;
    iEvent.getByToken(electronToken, electronH);

	//-------------- Get Event Info -----------------------------------

	run_    = iEvent.id().run();
	event_  = iEvent.id().event();
	lumi_   = iEvent.id().luminosityBlock();

	for (auto eleItr = electronH->begin(); eleItr != electronH->end(); ++eleItr) 
	{	
		electron_pt.push_back( eleItr->pt() );
		electron_eta.push_back( eleItr->eta() );
		electron_phi.push_back( eleItr->phi() );
		electron_mass.push_back( eleItr->mass());	//new
		electron_charge.push_back( eleItr->charge());	//new
	} 

    tree->Fill();	
}


void egTreeProducer::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const&) {}
void egTreeProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) {}
void egTreeProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) 
{
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(egTreeProducer);

#endif 
