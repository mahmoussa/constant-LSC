{
   TFile *f = new TFile ("stability_plots_constant_2017_onlystableyscan.root", "recreate");
  
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
   
  //float X_vtx[984768261];
  
  float Y_vtx[984768261];
  
  Int_t numvtx;
  
 
  for (int j=0 ; j <=nentries ; j++){Y_vtx[j]=0;}

  chain->SetBranchAddress("run",&Run);
  chain->SetBranchAddress("LS",&Lumiscetion);
  chain->SetBranchAddress("timeStamp_begin",&TimestambBegin);
  //chain->SetBranchAddress("vtx_x",X_vtx);
  chain->SetBranchAddress("vtx_y",Y_vtx);
  chain->SetBranchAddress("nVtx",&numvtx); 
 
  TCanvas* c1 = new TCanvas("c1","stability_constant_2017_yscan",700,500);                                
  c1->Divide(1,2);
  
  //TProfile* ls_x = new TProfile("ls_x","Profile of vtx_x versusls;lumisection;mean vtx_x position(cm)",48,10,58,-0.900390,1.05613);
  //TProfile* timestamp_x = new TProfile("timestamp_x","Profile of vtx_x versus timestamp;timestamp(sec);mean vtx_x position(cm)",1120,1501261177,1501262297,-0.900390,1.05613);
  
  TProfile* ls_y = new TProfile("ls_y","Profile of vtx_y versus ls;lumisection;mean vtx_y position(cm)",50,70,120,-0.900390,1.05613);
  TProfile* timestamp_y = new TProfile("timestamp_y","Profile of vtx_y versus timestamp;timestamp(sec);mean vtx_x position(cm)",1139,1501262589,1501263728,-0.900390,1.05613);
  
  int stable_lumisection_yscan[] ={72, 73, 77, 78, 82, 83, 87, 88, 92, 93, 97, 98, 102, 103, 107, 108, 112, 113, 117, 118};
  int stable_timestamp_begin_yscan[] = {1501262589,1501262708,1501262825,1501262941,1501263058,1501263190,1501263308,1501263425,1501263542,1501263660};
  int stable_timestamp_end_yscan[] = {1501262659,1501262777,1501262893,1501263010,1501263126,1501263259,1501263377,1501263493,1501263611,1501263728};
  
  
  for (Int_t i=0 ; i < nentries ; i++){  
     //if(i % 100 == 0) cout << i << " ";  
     chain->GetEntry(i);
     
     if ( Run != 300050) { continue;} 
        for (Int_t j=0 ; j < 20 ; j++){
           if  (Lumiscetion == stable_lumisection_yscan[j]) {ls_y->Fill(Lumiscetion, *Y_vtx);}
           }
        for (Int_t k=0 ; k < 10 ; k++){
           if  (TimestambBegin >= stable_timestamp_begin_yscan[k] && TimestambBegin <= stable_timestamp_end_yscan[k]) {timestamp_y->Fill(TimestambBegin, *Y_vtx);}
           }
     
     //ls_y->Fill(Lumiscetion, *Y_vtx);
     //timestamp_y->Fill(TimestambBegin, *Y_vtx);

  }
                                                      
  c1 -> cd(1);
  ls_y->SetMinimum(-0.06);
  ls_y->SetMaximum(0);                                                                  
  ls_y->Draw();
  ls_y->Write();
                                                                  
  c1->cd(2);                                                                   
  timestamp_y->SetMinimum(-0.06);
  timestamp_y->SetMaximum(0);
  timestamp_y->Draw();
  timestamp_y->Write();
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
  c1 -> SaveAs("stability_plots_constant_2017_yscan.pdf");
  
  gSystem->Exec("date");
}


