import ROOT
import numpy as np
import vector as vec

f1 = ROOT.TFile("output.root", "OPEN")

NBin = 13
binning =  np.array((0.,15.,30.,45.,60.,75.,90.,105.,120.,135.,150.,165.,180.,195.))

h1 = ROOT.TH1F("h1",";pT [GeV];410/15 ",NBin,binning)
h2 = ROOT.TH1F("h2","Electron phi",10,-4,4)
h3 = ROOT.TH1F("h3","Electron eta",10,-4,4)
h4 = ROOT.TH1F("h4","Di-Electron invariant mass",10,0,0.01)
h5 = ROOT.TH1F("h5","Di-Electron invariant mass",10,0,0.01)

for evt in f1.Get("egammaReconstruction/tree"):
	
#------------------ELECTRON_PT--------------------#
	
	for i in range(0,len(evt.electron_pt)):
		h1.Fill(evt.electron_pt[i])

#------------------ELECTRON_PHI-------------------#

	for j in range(0,len(evt.electron_phi)):
		h2.Fill(evt.electron_phi[j])

#------------------ELECTRON_ETA-------------------#

	for k in range(0,len(evt.electron_eta)):
		h3.Fill(evt.electron_eta[k])

#-----------Di-Electron Invariant Mass------------#
		
	for e in range(0, len(evt.electron_mass)):

	  if len(evt.electron_mass) != 2:
		continue

	  if evt.electron_charge[0] == evt.electron_charge[1]:
		#continue

	  #if (evt.electron_mass[1] + evt.electron_mass[0] < 0.0020) and (evt.electron_mass[1] + evt.electron_mass[0] > 0.0005):
		h4.Fill(evt.electron_mass[e])
		
#------------------------------------------------#

v1 = vec.obj(electron_pt,electron_phi,electron_eta,electron_mass)
v2 = vec.obj(electron_pt,electron_phi,electron_eta,electron_mass)

#for ent in f1.Get("egammaReconstruction/tree"): 

    #for a in range(0, len(ent.electron_mass)): 
    
	  #m = v1.electron_mass[a] + v2.electron_mass[a]

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

c3 =ROOT.TCanvas("c3","c3",1000,1000)

h3.SetTitle("Electron #eta")
h3.GetXaxis().SetTitle("#eta(#theta)")
h3.GetYaxis().SetTitle("Events")
h3.Draw("HIST")
h3.Draw("C9E1 SAME")
c3.Draw()

c3.SaveAs("Electron_eta_2000.png")

c4 =ROOT.TCanvas("c4","c4",1000,1000)

h4.SetTitle("Di-Electron Invariant Mass")
h4.GetXaxis().SetTitle("Mass")
h4.GetYaxis().SetTitle("Events")
h4.Draw("HIST")
h4.Draw("C9E1 SAME")
c4.Draw()

c4.SaveAs("Electron_Di-Electron_2000.png")

f1.Close()
