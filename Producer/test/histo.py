import ROOT
import numpy as np

f1 = ROOT.TFile("output.root", "OPEN")

NBin = 13
binning =  np.array((0.,15.,30.,45.,60.,75.,90.,105.,120.,135.,150.,165.,180.,195.))

h1 = ROOT.TH1F("h1",";pT [GeV];410/15 ",NBin,binning)
h2 = ROOT.TH1F("h2","Electron phi",10,-4,4)
h3 = ROOT.TH1F("h3","Electron eta",10,-4,4)
#RIP h4
h5 = ROOT.TH1F("h5","Di-Electron invariant mass",10,0,100)

electron1 = ROOT.TLorentzVector()
electron2 = ROOT.TLorentzVector()
eTot = ROOT.TLorentzVector()

for evt in f1.Get("egammaReconstruction/tree"):
	
#------------------ELECTRON_PT--------------------#
	
	for i in range(0,len(evt.electron_pt)):

		h1.Fill(evt.electron_pt[i])

#------------------ELECTRON_PHI-------------------#

		h2.Fill(evt.electron_phi[i])

#------------------ELECTRON_ETA-------------------#

		h3.Fill(evt.electron_eta[i])

#-----------Di-Electron Invariant Mass------------#
		
		electron1.SetPtEtaPhiM(evt.electron_pt[i], evt.electron_eta[i], evt.electron_phi[i], evt.electron_mass[i])
	        electron2.SetPtEtaPhiM(evt.electron_pt[i], evt.electron_eta[i], evt.electron_phi[i], evt.electron_mass[i])

		eTot = electron1 + electron2

		print("Electron Pt")
		print(eTot.Pt())
		print("Electron Eta")
		print(eTot.Eta())
		print("Electron Phi")
		print(eTot.Phi())
		print("Electron M")
		print(eTot.M()) 

		h5.Fill(eTot.M())

#------------------------------------------------#
c1 = ROOT.TCanvas("c1","c1",1000,1000)

h1.SetTitle("Electron pt")
h1.GetXaxis().SetTitle("GeV")
h1.GetYaxis().SetTitle("Events")
h1.Draw("HIST")
h1.Draw("C9E1 SAME")
c1.Draw()

c1.SaveAs("Electron_pt_var_bin_2000.png")

c2 = ROOT.TCanvas("c2","c2",1000,1000)

h2.SetTitle("Electron #phi")
h2.GetXaxis().SetTitle("Radians")
h2.GetYaxis().SetTitle("Events")
h2.Draw("HIST")
h2.Draw("C9E1 SAME")
c2.Draw()

c2.SaveAs("Electron_phi_2000.png")

c3 = ROOT.TCanvas("c3","c3",1000,1000)

h3.SetTitle("Electron #eta")
h3.GetXaxis().SetTitle("#eta(#theta)")
h3.GetYaxis().SetTitle("Events")
h3.Draw("HIST")
h3.Draw("C9E1 SAME")
c3.Draw()

c3.SaveAs("Electron_eta_2000.png")

c5 = ROOT.TCanvas("c5","c5",1000,1000)

h5.SetTitle("Di-Electron Invariant Mass")
h5.GetXaxis().SetTitle("Mass")
h5.GetYaxis().SetTitle("Events")
h5.Draw("HIST")
h5.Draw("C9E1 SAME")
c5.Draw()

c5.SaveAs("Electron_Di-Electron_TLV_2000.png")

f1.Close()
