{
   TFile *f = new TFile ("/eos/home-m/mgadalla/LSC/stability_plots_2017/stability_plots_constant/stability_plots_constant_2017_onlystablexscan.root", "recreate");
  
   TChain *chain = new TChain ("lumi/tree");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias1/crab_CMSSW_10_6_8_patch1_ZeroBias1_splitPerBXTrue/200414_025013/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias1/crab_CMSSW_10_6_8_patch1_ZeroBias1_splitPerBXTrue/200414_035027/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias2/crab_CMSSW_10_6_8_patch1_ZeroBias2_splitPerBXTrue/200414_025100/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias3/crab_CMSSW_10_6_8_patch1_ZeroBias3_splitPerBXTrue/200414_025138/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias4/crab_CMSSW_10_6_8_patch1_ZeroBias4_splitPerBXTrue/200414_025216/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias5/crab_CMSSW_10_6_8_patch1_ZeroBias5_splitPerBXTrue/200414_025258/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias6/crab_CMSSW_10_6_8_patch1_ZeroBias6_splitPerBXTrue/200414_025350/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias6/crab_CMSSW_10_6_8_patch1_ZeroBias6_splitPerBXTrue/200414_035205/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias7/crab_CMSSW_10_6_8_patch1_ZeroBias7_splitPerBXTrue/200414_025426/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias7/crab_CMSSW_10_6_8_patch1_ZeroBias7_splitPerBXTrue/200414_035238/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/eos/home-m/mgadalla/LSC/6016/ZeroBias8/crab_CMSSW_10_6_8_patch1_ZeroBias8_splitPerBXTrue/200414_025454/0000/pcc_Data_PixVtx_Event_90X_*.root");
   
   
   Int_t nentries = chain->GetEntries();
   cout << nentries << endl;
  
  chain->SetBranchStatus("*",0);
  chain->SetBranchStatus("LS",1);
  chain->SetBranchStatus("timeStamp_begin",1);
  chain->SetBranchStatus("run",1);
  chain->SetBranchStatus("vtx_x",1);
  chain->SetBranchStatus("vtx_y",1);
  chain->SetBranchStatus("nVtx",1);
   
  gSystem->Exec("date");

  
  Int_t Lumiscetion;
  UInt_t TimestambBegin;
  Int_t Run;
  cout << "hiiiiiii1";
   
  float X_vtx[984768261];
  
  //float Y_vtx[984768261];
  
  Int_t numvtx;
  
 
  for (int j=0 ; j <=nentries ; j++){X_vtx[j]=0;}

  chain->SetBranchAddress("run",&Run);
  chain->SetBranchAddress("LS",&Lumiscetion);
  chain->SetBranchAddress("timeStamp_begin",&TimestambBegin);
  chain->SetBranchAddress("vtx_x",X_vtx);
  //chain->SetBranchAddress("vtx_y",Y_vtx);
  chain->SetBranchAddress("nVtx",&numvtx); 
 
  TCanvas* c1 = new TCanvas("c1","stability_constant_2017_xscan",700,500);                                
  c1->Divide(1,2);
  TProfile* ls_x = new TProfile("ls_x","Profile of vtx_x versusls;lumisection;mean vtx_x position(cm)",48,10,58,-0.900390,1.05613);
  TProfile* timestamp_x = new TProfile("timestamp_x","Profile of vtx_x versus timestamp;timestamp(sec);mean vtx_x position(cm)",1120,1501261177,1501262297,-0.900390,1.05613);
  //TProfile* ls_y = new TProfile("ls_y","Profile of vtx_y versus ls",50,70,120,-0.900390,1.05613);
  //TProfile* timestamp_y = new TProfile("timestamp_y","Profile of vtx_y versus timestamp",1139,1501262589,1501263728,-0.900390,1.05613);
  int stable_lumisection_xscan[] ={11, 12, 16, 17, 21, 22, 26, 27, 31, 32, 36, 37, 41, 42, 46, 47, 51, 52, 56, 57};
  int stable_timestamp_begin_xscan[] = {1501261190,1501261293,1501261417,1501261526,1501261642,1501261776,1501261894,1501262008,1501262120,1501262238};
  int stable_timestamp_end_xscan[] = {1501261235,1501261350,1501261462,1501261579,1501261700,1501261832,1501261952,1501262067,1501262182,1501262297};
  for (Int_t i=0 ; i < nentries ; i++){  
     //if(i % 100 == 0) cout << i << " ";  
     chain->GetEntry(i);
     
     if ( Run != 300050) { continue;} 
        for (Int_t j=0 ; j < 20 ; j++){
           if  (Lumiscetion == stable_lumisection_xscan[j]) {ls_x->Fill(Lumiscetion, *X_vtx);}
           }
        for (Int_t k=0 ; k < 10 ; k++){
           if  (TimestambBegin >= stable_timestamp_begin_xscan[k] && TimestambBegin <= stable_timestamp_end_xscan[k]) {timestamp_x->Fill(TimestambBegin, *X_vtx);}
           }
     
     //ls_y->Fill(Lumiscetion, *Y_vtx);
     //timestamp_y->Fill(TimestambBegin, *Y_vtx);

  }
                                                      
  c1 -> cd(1);
  ls_x->SetMinimum(0.04);
  ls_x->SetMaximum(0.115);                                                                  
  ls_x->Draw();
  ls_x->Write();
                                                                  
  c1->cd(2);                                                                   
  timestamp_x->SetMinimum(0.04);
  timestamp_x->SetMaximum(0.115);
  timestamp_x->Draw();
  timestamp_x->Write();
  /*
  c1->cd(2);
  ls_y->SetMinimum(-0.08);
  ls_y->SetMaximum(-0.028);
  ls_y->Draw();
  
  c1->cd(4);
  timestamp_y->SetMinimum(-0.08);
  timestamp_y->SetMaximum(-0.028);
  timestamp_y->Draw();
  */
  c1 -> Write();
  c1 -> SaveAs("/eos/home-m/mgadalla/LSC/stability_plots_2017/stability_plots_constant/stability_plots_constant_2017_xscan.pdf");
  
  gSystem->Exec("date");
}


