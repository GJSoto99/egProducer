import ROOT
import numpy as np

f1 = ROOT.TFile("output.root", "OPEN")

#-----------ELECTRON_PT-------------#
NBin = 10
binning =  np.array((0,15,25,45,55,70,80,95,130,190))
h1 = ROOT.TH1D("h1",";pT [GeV];410/15 ",NBin,binning)

for evt1 in f1.Get("egammaReconstruction/tree"):
	
	for i in range(0,len(evt1.electron_pt)):
		h1.Fill(evt1.electron_pt[i])

c1 = ROOT.TCanvas("c1","c1",1000,1000)

h1.SetTitle("Electron pt")
h1.GetXaxis().SetTitle("GeV")
h1.GetYaxis().SetTitle("Events")
h1.Draw("HIST")
h1.Draw("C9E1 SAME")
c1.Draw()

c1.SaveAs("Electron_pt_var_bin.png")

#-----------ELECTRON_PHI-------------#

h2 =ROOT.TH1F("h2","Electron phi",10,-4,4)

for evt2 in f1.Get("egammaReconstruction/tree"):

        for j in range(0,len(evt2.electron_phi)):
                h2.Fill(evt2.electron_phi[j])

c2 = ROOT.TCanvas("c2","c2",1000,1000)

h2.SetTitle("Electron #phi")
h2.GetXaxis().SetTitle("Radians")
h2.GetYaxis().SetTitle("Events")
h2.Draw("HIST")
h2.Draw("C9E1 SAME")
c2.Draw()

c2.SaveAs("Electron_phi.png")

#-----------ELECTRON_PT-------------#

h3 = ROOT.TH1F("h3","Electron eta",10,-4,4)

for evt3 in f1.Get("egammaReconstruction/tree"):

        for k in range(0,len(evt3.electron_eta)):
                h3.Fill(evt3.electron_eta[k])

c3 =ROOT.TCanvas("c3","c3",1000,1000)

h3.SetTitle("Electron #eta")
h3.GetXaxis().SetTitle("#eta(#theta)")
h3.GetYaxis().SetTitle("Events")
h3.Draw("HIST")
h3.Draw("C9E1 SAME")
c3.Draw()

c3.SaveAs("Electron_eta.png")

f1.Close()
