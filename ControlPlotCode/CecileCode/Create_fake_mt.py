if __name__ == "__main__":

    import ROOT
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--scale', default="nominal", choices=['nominal', 'up', 'down', 'wup', 'wdown','qcdup','qcddown','JESup','JESdown'], help="Which TES?")
    options = parser.parse_args()

    #nbhist=1
    nbhist=31
    postfix=["","_norm_ff_qcd_mt_systUp","_norm_ff_qcd_mt_systDown","_norm_ff_qcd_dm0_njet0_mt_statUp","_norm_ff_qcd_dm0_njet0_mt_statDown","_norm_ff_qcd_dm0_njet1_mt_statUp","_norm_ff_qcd_dm0_njet1_mt_statDown","_norm_ff_qcd_dm1_njet0_mt_statUp","_norm_ff_qcd_dm1_njet0_mt_statDown","_norm_ff_qcd_dm1_njet1_mt_statUp","_norm_ff_qcd_dm1_njet1_mt_statDown","_norm_ff_w_mt_systUp","_norm_ff_w_mt_systDown","_norm_ff_w_dm0_njet0_mt_statUp","_norm_ff_w_dm0_njet0_mt_statDown","_norm_ff_w_dm0_njet1_mt_statUp","_norm_ff_w_dm0_njet1_mt_statDown","_norm_ff_w_dm1_njet0_mt_statUp","_norm_ff_w_dm1_njet0_mt_statDown","_norm_ff_w_dm1_njet1_mt_statUp","_norm_ff_w_dm1_njet1_mt_statDown","_norm_ff_tt_mt_systUp","_norm_ff_tt_mt_systDown","_norm_ff_tt_dm0_njet0_mt_statUp","_norm_ff_tt_dm0_njet0_mt_statDown","_norm_ff_tt_dm0_njet1_mt_statUp","_norm_ff_tt_dm0_njet1_mt_statDown","_norm_ff_tt_dm1_njet0_mt_statUp","_norm_ff_tt_dm1_njet0_mt_statDown","_norm_ff_tt_dm1_njet1_mt_statUp","_norm_ff_tt_dm1_njet1_mt_statDown"]

    fData=ROOT.TFile("files_nominal_mt/Data.root","r")
    fout=ROOT.TFile("files_nominal_mt/Fake.root","recreate")

    h_0jet=[]
    h_boosted=[]
    h_vbf=[]
    h_1jet=[]
    h_gg2jets=[]
    h_vh2jets=[]
    h_vbf2=[]
    for k in range(0,nbhist):
      h_0jet.append(fData.Get("AI0jet/reweighted_data_obs"+postfix[k]))
      h_boosted.append(fData.Get("AIboosted/reweighted_data_obs"+postfix[k]))
      h_vbf.append(fData.Get("AIvbf/reweighted_data_obs"+postfix[k]))
      h_1jet.append(fData.Get("AI1jet/reweighted_data_obs"+postfix[k]))
      h_gg2jets.append(fData.Get("AIgg2jets/reweighted_data_obs"+postfix[k]))
      h_vh2jets.append(fData.Get("AIvh2jets/reweighted_data_obs"+postfix[k]))
      h_vbf2.append(fData.Get("AIvbf2/reweighted_data_obs"+postfix[k]))

    fout.cd()
    dir0jet=fout.mkdir("mt_0jet")
    dir0jet.cd()
    for k in range(0,nbhist):
      h_0jet[k].Scale(h_0jet[0].Integral(-1,-1,-1,-1)/h_0jet[k].Integral(-1,-1,-1,-1))
      h_0jet[k].SetName("jetFakes"+postfix[k])
      h_0jet[k].Write()

    dir1jet=fout.mkdir("mt_boosted")
    dir1jet.cd()
    for k in range(0,nbhist):
      h_boosted[k].Scale(h_boosted[0].Integral(-1,-1,-1,-1)/h_boosted[k].Integral(-1,-1,-1,-1))
      h_boosted[k].SetName("jetFakes"+postfix[k])
      h_boosted[k].Write()

    dir2jet=fout.mkdir("mt_vbf")
    dir2jet.cd()
    for k in range(0,nbhist):
      h_vbf[k].Scale(h_vbf[0].Integral(-1,-1,-1,-1)/h_vbf[k].Integral(-1,-1,-1,-1))
      h_vbf[k].SetName("jetFakes"+postfix[k])
      h_vbf[k].Write()

    dir3jet=fout.mkdir("mt_1jet")
    dir3jet.cd()
    for k in range(0,nbhist):
      h_1jet[k].Scale(h_1jet[0].Integral(-1,-1)/h_1jet[k].Integral(-1,-1))
      h_1jet[k].SetName("jetFakes"+postfix[k])
      h_1jet[k].Write()

    dir4jet=fout.mkdir("mt_gg2jets")
    dir4jet.cd()
    for k in range(0,nbhist):
      h_gg2jets[k].Scale(h_gg2jets[0].Integral(-1,-1)/h_gg2jets[k].Integral(-1,-1))
      h_gg2jets[k].SetName("jetFakes"+postfix[k])
      h_gg2jets[k].Write()

    dir5jet=fout.mkdir("mt_vh2jets")
    dir5jet.cd()
    for k in range(0,nbhist):
      h_vh2jets[k].Scale(h_vh2jets[0].Integral(-1,-1)/h_vh2jets[k].Integral(-1,-1))
      h_vh2jets[k].SetName("jetFakes"+postfix[k])
      h_vh2jets[k].Write()

    dir6jet=fout.mkdir("mt_vbf2")
    dir6jet.cd()
    for k in range(0,nbhist):
      h_vbf2[k].Scale(h_vbf2[0].Integral(-1,-1)/h_vbf2[k].Integral(-1,-1))
      h_vbf2[k].SetName("jetFakes"+postfix[k])
      h_vbf2[k].Write()

