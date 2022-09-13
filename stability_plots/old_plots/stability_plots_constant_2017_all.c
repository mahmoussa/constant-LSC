{
   TFile *f = new TFile ("stability_plots_constant_2017.root", "recreate");
  
   TChain *chain = new TChain ("lumi/tree");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias1/crab_CMSSW_10_6_8_patch1_ZeroBias1_splitPerBXTrue/200414_025013/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias1/crab_CMSSW_10_6_8_patch1_ZeroBias1_splitPerBXTrue/200414_035027/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias2/crab_CMSSW_10_6_8_patch1_ZeroBias2_splitPerBXTrue/200414_025100/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias3/crab_CMSSW_10_6_8_patch1_ZeroBias3_splitPerBXTrue/200414_025138/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias4/crab_CMSSW_10_6_8_patch1_ZeroBias4_splitPerBXTrue/200414_025216/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias5/crab_CMSSW_10_6_8_patch1_ZeroBias5_splitPerBXTrue/200414_025258/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias6/crab_CMSSW_10_6_8_patch1_ZeroBias6_splitPerBXTrue/200414_025350/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias6/crab_CMSSW_10_6_8_patch1_ZeroBias6_splitPerBXTrue/200414_035205/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias7/crab_CMSSW_10_6_8_patch1_ZeroBias7_splitPerBXTrue/200414_025426/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias7/crab_CMSSW_10_6_8_patch1_ZeroBias7_splitPerBXTrue/200414_035238/0000/pcc_Data_PixVtx_Event_90X_*.root");
   chain->Add("/home/mahmoud/2017_LS_data/legacy_vtx_data/ZeroBias8/crab_CMSSW_10_6_8_patch1_ZeroBias8_splitPerBXTrue/200414_025454/0000/pcc_Data_PixVtx_Event_90X_*.root");
   
   
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
 
  TCanvas* c1 = new TCanvas("c1","stability_constant_2017",700,500);                                
  c1->Divide(1,2);
  TProfile* ls_x = new TProfile("ls_x","Profile of vtx_x versus ls",48,10,58,-0.900390,1.05613);
  TProfile* timestamp_x = new TProfile("timestamp_x","Profile of vtx_x versus timestamp",1120,1501261177,1501262297,-0.900390,1.05613);
  //TProfile* ls_y = new TProfile("ls_y","Profile of vtx_y versus ls",50,70,120,-0.900390,1.05613);
  //TProfile* timestamp_y = new TProfile("timestamp_y","Profile of vtx_y versus timestamp",1139,1501262589,1501263728,-0.900390,1.05613);
  
  for (Int_t i=0 ; i < nentries ; i++){  
     //if(i % 100 == 0) cout << i << " ";  
     chain->GetEntry(i);
     
     if ( Run != 300050) { continue;} 
     ls_x->Fill(Lumiscetion, *X_vtx);
     timestamp_x->Fill(TimestambBegin, *X_vtx);
     
     //ls_y->Fill(Lumiscetion, *Y_vtx);
     //timestamp_y->Fill(TimestambBegin, *Y_vtx);

  }
                                                      
  c1 -> cd(1);
  ls_x->SetMinimum(0.04);
  ls_x->SetMaximum(0.115);                                                                  
  ls_x->Draw();
                                                                   
  c1->cd(2);                                                                   
  timestamp_x->SetMinimum(0.04);
  timestamp_x->SetMaximum(0.115);
  timestamp_x->Draw();
  /*
  c1->cd(2);
  ls_y->SetMinimum(-0.06);
  ls_y->SetMaximum(0);
  ls_y->Draw();
  
  c1->cd(4);
  timestamp_y->SetMinimum(-0.06);
  timestamp_y->SetMaximum(0);
  timestamp_y->Draw();
  */
  c1 -> Print("stability_plots_constant_2017.root");
  c1 -> SaveAs("stability_plots_constant_2017.pdf");
  
  gSystem->Exec("date");
}


