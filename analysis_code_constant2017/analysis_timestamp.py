import ROOT as r
import sys
import os
import pickle
import datetime
import math

print (datetime.datetime.now())
def generateTimeWindows(whichScan,whichVtx):
   if whichScan == "X1":
        begin = [1501261190,1501261293,1501261417,1501261526,1501261642,1501261776,1501261894,1501262008,1501262120,1501262238]
        end = [1501261235,1501261350,1501261462,1501261579,1501261700,1501261832,1501261952,1501262067,1501262182,1501262297]
        
   if whichScan == "Y1":
        begin = [1501262594,1501262718,1501262832,1501262949,1501263058,1501263198,1501263315,1501263434,1501263548,1501263660]
        end = [1501262653,1501262770,1501262887,1501263004,1501263122,1501263259,1501263377,1501263493,1501263611,1501263712]
   return begin, end

def generateOffsetPositions_nostepsize(whichScan):
   if "X1" in whichScan:
      nomPos_av =[ -175.560022483197 , -78.5415056119271 , 19.3517935417874 , 116.54838299783 , 214.230083646694 , 214.469526333868 , 117.150971459819 , 19.9659306338802 , -78.6628002605352 , -176.250449036778 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -174.213372023118 , -78.0418606240285 , 19.3937542607244 , 116.114839728251 , 213.333911357559 , 213.478293456565 , 116.865219972199 , 20.1082363174736 , -77.7720105827834 , -175.008171532415 ]
      nomPos_arc = [ -176.906672943276 , -79.0411505998257 , 19.3098328228503 , 116.981926267408 , 215.126255935828 , 215.460759211172 , 117.436722947439 , 19.8236249502868 , -79.553589938287 , -177.49272654114 ]
   if "Y1" in whichScan:
      nomPos_av =[ -174.105444834605 , -77.7226701985845 , 19.5192629112704 , 117.276599371834 , 214.483484708366 , 214.298684775616 , 116.74764005966 , 19.2281906267501 , -77.7448514077823 , -175.19401115983 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -173.707782362966 , -77.696026386614 , 19.104900088441 , 116.265115663507 , 213.229910468837 , 212.341287935313 , 115.422505406166 , 18.2211036240957 , -77.6319000043476 , -174.535724905372 ]
      nomPos_arc = [ -174.503107306244 , -77.749314010555 , 19.9336257340997 , 118.28808308016 , 215.737058947895 , 216.25608161592 , 118.072774713153 , 20.2352776294046 , -77.857802811217 , -175.852297414288 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc

def generateOffsetPositions_stepsize_no_outliersremoval(whichScan):
   if "X1" in whichScan:
      nomPos_av =[ -178.974229232929 , -81.1021605492258 , 17.6446909169215 , 115.694826185397 , 214.230083646694 , 214.469526333868 , 116.297414647386 , 18.2588280090144 , -81.2234551978339 , -179.664655786509 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -179.86574533829 , -82.2811404854072 , 16.5675683531386 , 114.701741274458 , 213.333911357559 , 213.478293456565 , 115.452121518406 , 17.2820504098878 , -82.0112904441621 , -180.660544847587 ]
      nomPos_arc = [ -178.082713127568 , -79.9231806130447 , 18.7218134807043 , 116.687911096335 , 215.126255935828 , 215.460759211172 , 117.142707776366 , 19.2356056081408 , -80.435619951506 , -178.668766725432 ]
   if "Y1" in whichScan:
      nomPos_av =[ -178.733879595396 , -81.1939961441779 , 17.2050462808747 , 116.119485556636 , 214.483484708366 , 214.298684775616 , 115.590526244462 , 16.9139739963545 , -81.2161773533757 , -179.822445920621 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -180.469677026722 , -82.767447259431 , 15.723953506563 , 114.574636872568 , 213.229910468837 , 212.341287935313 , 113.732026615227 , 14.8401570422177 , -82.7033208771646 , -181.297619569128 ]
      nomPos_arc = [ -176.99808216407 , -79.6205450289248 , 18.6861390551865 , 117.664334240703 , 215.737058947895 , 216.25608161592 , 117.449025873696 , 18.9877909504914 , -79.7290338295868 , -178.347272272114 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc

def generateOffsetPositions_stepsize_using_outliersremoval(whichScan):
   if "X1" in whichScan:
      nomPos_av =[ -179.582783922556 , -81.5585765664465 , 17.3404135721078 , 115.54268751299 , 214.230083646694 , 214.469526333868 , 116.145275974979 , 17.9545506642006 , -81.6798712150546 , -180.273210476137 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -179.86574533829 , -82.2811404854072 , 16.5675683531386 , 114.701741274458 , 213.333911357559 , 213.478293456565 , 115.452121518406 , 17.2820504098878 , -82.0112904441621 , -180.660544847587 ]
      nomPos_arc = [ -178.799234875938 , -80.4605719243219 , 18.3635526065195 , 116.508780659243 , 215.126255935828 , 215.460759211172 , 116.963577339274 , 18.877344733956 , -80.9730112627832 , -179.385288473802 ]
   if "Y1" in whichScan:
      nomPos_av =[ -178.232491853235 , -80.8179553375573 , 17.4557401519552 , 116.244832492176 , 214.483484708366 , 214.298684775616 , 115.715873180002 , 17.1646678674349 , -80.8401365467551 , -179.32105817846 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -179.410399151171 , -81.9729888527676 , 16.2535924443386 , 114.839456341456 , 213.229910468837 , 212.341287935313 , 113.996846084115 , 15.3697959799933 , -81.9088624705012 , -180.238341693577 ]
      nomPos_arc = [ -176.40392509844 , -79.1749272297017 , 18.9832175880019 , 117.812873507111 , 215.737058947895 , 216.25608161592 , 117.597565140104 , 19.2848694833068 , -79.2834160303637 , -177.753115206484 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc

def makeCalibPlot(whichScan,rootOutFile,pdfOutFile,condition):
   if 'X1' in whichScan:
        whichVtx = "vtx_x" 

   if 'Y1' in whichScan:
        whichVtx = "vtx_y"

   print "Now for scan ", whichScan, " and vtx coordinate ", whichVtx

   filelist = os.listdir("./")

   chain = r.TChain("lumi/tree")

   with open('./filesFor_time_Scan.pkl', 'rb') as f:
        filelist= pickle.load(f)

   for name in filelist[whichScan]:
        localName = name.split('/')[-1] # pcc_
        posZeroBias = name.find('ZeroBias') #112
        print "posZeroBias" ,posZeroBias
        print name   #root://eoscms/eos
        if not posZeroBias:
            print "Problem with form of filename, assumed to be of a form such that filename[pos, pos+8] == ZeroBias, please check"
            sys.exit(1)
        whichZeroBias = name[posZeroBias: posZeroBias+9]
        print "whichzerobias" ,whichZeroBias
        localName = whichZeroBias + '_' + localName
        if localName.find(".root"):
            chain.Add(name)

   numFiles = chain.GetListOfFiles().GetEntries()
   nentries = chain.GetEntries()
   print "Chain contains " + str(numFiles) + " files"
   print "Chain contains events", nentries

   beginTS, endTS=  generateTimeWindows(whichScan,whichVtx)
   if 'nostepsize' in condition:
      Pos_av , Pos_nom , Pos_DOR , Pos_arc = generateOffsetPositions_nostepsize(whichScan)
   if 'stepsize_no_outliersremoval' in condition:
      Pos_av , Pos_nom , Pos_DOR , Pos_arc = generateOffsetPositions_stepsize_no_outliersremoval(whichScan)
   if 'stepsize_using_outliersremoval' in condition:
      Pos_av , Pos_nom , Pos_DOR , Pos_arc = generateOffsetPositions_stepsize_using_outliersremoval(whichScan)
  
   rfile = r.TFile(rootOutFile,"recreate")
   print "ok text0-1-2-3"
   canvas = [r.TCanvas() for i in range(0,15)]

   r.gStyle.SetOptStat(1) #show normal statistics
   r.gStyle.SetOptFit(1)  #show fit statistics
   r.gStyle.SetStatFormat("8.7g")
   r.gStyle.SetFitFormat("8.7g")
   if whichVtx == "vtx_y":
      r.gStyle.SetStatX(0.8)
      r.gStyle.SetStatY(0.5)
   if whichVtx == "vtx_x":
      r.gStyle.SetStatX(0.5)
      r.gStyle.SetStatY(0.55)

   hist = r.TH1F("hist",whichScan + " scan, " + whichVtx, 1000, -0.2, 0.2) # hardcoded   
   hList = [r.TH1F() for entry in beginTS]
   histoList = [r.TH1F() for entry in beginTS]
   avVtxPos = [0.0 for entry in beginTS]
   errAvVtxPos = [0.0 for entry in beginTS]
   chi2_ndfAvVtxPos = [0.0 for entry in beginTS]
   errAvVtxPos_multiplied_max1chi2 = [0.0 for entry in beginTS]
   slope_forward = [0.0 for j in range(0,4)]
   slope_forward_error = [0.0 for j in range(0,4)]
   slope_backward = [0.0 for j in range(0,4)]
   slope_backward_error = [0.0 for j in range(0,4)]
   histo_mean=[0.0 for entry in beginTS]
   histo_mean_error=[0.0 for entry in beginTS]
   mg = [r.TMultiGraph()for i in range(0,4)]
   resedual_mg=[r.TMultiGraph()for i in range(0,4)]
   forward_vtxVspos=[r.TGraphErrors()for i in range(0,4)]
   backword_vtxVspos=[r.TGraphErrors()for i in range(0,4)]
   resedual_forward_vtxVspos=[r.TGraphErrors()for i in range(0,4)]
   resedual_backword_vtxVspos=[r.TGraphErrors()for i in range(0,4)]
   line = [r.TLine for i in range(0,4)]
   fit_forward_vtxVspos=[]
   fit_backword_vtxVspos=[]
   latex1 = r . TLatex ()
   latex2 = r . TLatex ()
   latex1 . SetNDC ()
   latex2 . SetNDC ()
   latex1 . SetTextColor(r.kRed)
   latex2 . SetTextColor(r.kBlue)
   latex1.SetTextFont(42)
   latex2.SetTextFont(42)
   
   for index, value in enumerate(beginTS):
      hList[index] = hist.Clone()
      hList[index].SetName("hist"+str(index))

      stringCond = "run == 300050 " + "&& timeStamp_begin >= " + str(beginTS[index]) + " && timeStamp_begin <= " + str(endTS[index]) + "&& nVtx >= 1 " + " && vtx_isGood"
      print stringCond
      # chain.Draw(whichVtx + " >>hist"+str(index), stringCond, ' ' , 'nentries='100 , 'startfrom =' 0 )
      chain.Draw(whichVtx + " >>hist"+str(index), stringCond )        
      histoList[index]= r.gDirectory.Get("hist"+str(index))
      histoList[index].GetXaxis().SetTitle(whichVtx + " [cm]")
      histoList[index].GetYaxis().SetTitle("Offset in [#mum]")
      histoList[index].SetTitle("%i" %index)
      if histoList[index].GetEntries()==0:
         continue
      if index==0 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.059455, 0.135425) # range mean+-5std using [-2,2] range
      if index==1 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.04975,0.12573)
      if index==2 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.039925,0.115955)
      if index==3 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.030085,0.106295)
      if index==4 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.02026,0.09648)
      if index==5 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.0216,0.09742)
      if index==6 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.03134,0.10714)
      if index==7 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.04103,0.11705)
      if index==8 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.051015,0.126705)
      if index==9 and whichVtx == "vtx_x" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" , 0.060725,0.136635)

      if index==0 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.084820377626,-0.019550377626)
      if index==1 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0749609769555,-0.0099309769555)
      if index==2 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.065283728649,2.62713510000012E-05)
      if index==3 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0554652254542,0.0098447745458)
      if index==4 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0455554174093,0.0195745825907)
      if index==5 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0463971736219,0.0188028263781)
      if index==6 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0561226150529,0.0089373849471)
      if index==7 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0660364006317,-0.0008464006317)
      if index==8 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0758803872573,-0.0107103872573)
      if index==9 and whichVtx == "vtx_y" : gauss_Fit = r.TF1("gauss_Fit" , "gaus" ,-0.0858463560129,-0.0204363560129)
      
      histo_mean[index]= (histoList[index].GetMean())*10000
      histo_mean_error[index]= (histoList[index].GetRMS() / math.sqrt(histoList[index].GetEntries()))*10000
      histoList[index].Fit(gauss_Fit,'ER')      
      fit = histoList[index].GetFunction("gauss_Fit")
      avVtxPos[index]=fit.GetParameter(1)*10000
      errAvVtxPos[index] = fit.GetParError(1)*10000
      chi2_ndfAvVtxPos[index] = (fit.GetChisquare()/ fit.GetNDF())
      print 'chi2 / dof ' , chi2_ndfAvVtxPos[index]
      errAvVtxPos_multiplied_max1chi2[index] = errAvVtxPos[index] * max(1,math.sqrt(chi2_ndfAvVtxPos[index]))
      canvas[index].cd()              
      histoList[index].Draw()
      histoList[index].Write()
      canvas[index].SaveAs(pdfOutFile+"(")

   for i in range(0,5):
      forward_vtxVspos[0].SetPoint(i, Pos_av[i],avVtxPos[i])
      #forward_vtxVspos[0].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[0].SetPointError(i, 0. ,errAvVtxPos[i])
      forward_vtxVspos[1].SetPoint(i, Pos_nom[i],avVtxPos[i])
      #forward_vtxVspos[1].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[1].SetPointError(i, 0. ,errAvVtxPos[i])
      forward_vtxVspos[2].SetPoint(i, Pos_DOR[i],avVtxPos[i])
      #forward_vtxVspos[2].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[2].SetPointError(i, 0. ,errAvVtxPos[i])
      forward_vtxVspos[3].SetPoint(i, Pos_arc[i],avVtxPos[i])
      #forward_vtxVspos[3].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[3].SetPointError(i, 0. ,errAvVtxPos[i])

      backword_vtxVspos[0].SetPoint(i, Pos_av[i+5],avVtxPos[i+5])
      #backword_vtxVspos[0].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[0].SetPointError(i, 0. ,errAvVtxPos[i+5])
      backword_vtxVspos[1].SetPoint(i, Pos_nom[i+5],avVtxPos[i+5])
      #backword_vtxVspos[1].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[1].SetPointError(i, 0. ,errAvVtxPos[i+5])
      backword_vtxVspos[2].SetPoint(i, Pos_DOR[i+5],avVtxPos[i+5])
      #backword_vtxVspos[2].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[2].SetPointError(i, 0. ,errAvVtxPos[i+5])
      backword_vtxVspos[3].SetPoint(i, Pos_arc[i+5],avVtxPos[i+5])
      #backword_vtxVspos[3].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[3].SetPointError(i, 0. ,errAvVtxPos[i+5])
      
   for j in range(0,4):
      forward_vtxVspos[j].SetLineWidth(2)
      forward_vtxVspos[j].SetMarkerColor(r.kRed)
      forward_vtxVspos[j].SetMarkerStyle(21)
      forward_vtxVspos[j].SetMarkerSize(0.5)
      forward_vtxVspos[j].Fit("pol1")
      fit_forward_vtxVspos.append(forward_vtxVspos[j].GetFunction("pol1"))
      slope_forward[j]= fit_forward_vtxVspos[j].GetParameter(1)
      slope_forward_error[j]= fit_forward_vtxVspos[j].GetParError(1)
      mg[j].Add(forward_vtxVspos[j]) 

      backword_vtxVspos[j].SetLineWidth(2)
      backword_vtxVspos[j].SetMarkerColor(r.kBlue)
      backword_vtxVspos[j].SetMarkerStyle(20)
      backword_vtxVspos[j].SetMarkerSize(0.5)
      backword_vtxVspos[j].Fit("pol1")
      fit_backword_vtxVspos.append(backword_vtxVspos[j].GetFunction("pol1"))
      slope_backward[j]= fit_backword_vtxVspos[j].GetParameter(1)
      slope_backward_error[j]= fit_backword_vtxVspos[j].GetParError(1)
      mg[j].Add(backword_vtxVspos[j]) 

   for j in range(0,4):
      canvas[j+10].Divide(1,2)
      canvas[j+10].cd(1)
      canvas[j+10].cd(1).SetPad(0,0.3,1.0,1.0)
      mg[j].Draw("ap")
      if j == 0:
         mg[j].SetTitle("timestamp scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_av separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_av in microns")
         mg[j].GetYaxis().SetTitle("Pos_av" + whichVtx + "  in microns")
  
      elif j == 1:
         mg[j].SetTitle("timestamp scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_nom separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_nom in microns")
         mg[j].GetYaxis().SetTitle("Pos_nom" + whichVtx + "  in microns")

      elif j == 2:
         mg[j].SetTitle("timestamp scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_DOR separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_DOR in microns")
         mg[j].GetYaxis().SetTitle("Pos_DOR" + whichVtx + "  in microns")
         
      elif j == 3:
         mg[j].SetTitle("timestamp scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_arc separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_arc in microns")
         mg[j].GetYaxis().SetTitle("Pos_arc" + whichVtx + "  in microns")
      
      forward_vtxVspos[j].GetFunction("pol1").SetLineColor(r.kRed)
      backword_vtxVspos[j].GetFunction("pol1").SetLineColor(r.kBlue)
      mg[j].Write()

   for i in range(0,5):
      y0_forward_fit = fit_forward_vtxVspos[0].Eval(Pos_av[i])
      y1_forward_fit = fit_forward_vtxVspos[1].Eval(Pos_nom[i])
      y2_forward_fit = fit_forward_vtxVspos[2].Eval(Pos_DOR[i])
      y3_forward_fit = fit_forward_vtxVspos[3].Eval(Pos_arc[i])
      resedual_forward_vtxVspos[0].SetPoint(i,Pos_av[i],(avVtxPos[i] - y0_forward_fit))
      #resedual_forward_vtxVspos[0].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[0].SetPointError(i, 0. , errAvVtxPos[i])
      resedual_forward_vtxVspos[1].SetPoint(i,Pos_nom[i],(avVtxPos[i] - y1_forward_fit))
      #resedual_forward_vtxVspos[1].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[1].SetPointError(i, 0. , errAvVtxPos[i])
      resedual_forward_vtxVspos[2].SetPoint(i,Pos_DOR[i],(avVtxPos[i] - y2_forward_fit))
      #resedual_forward_vtxVspos[2].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[2].SetPointError(i, 0. , errAvVtxPos[i])
      resedual_forward_vtxVspos[3].SetPoint(i,Pos_arc[i],(avVtxPos[i] - y3_forward_fit))
      #resedual_forward_vtxVspos[3].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[3].SetPointError(i, 0. , errAvVtxPos[i])

      y0_backword_fit = fit_backword_vtxVspos[0].Eval(Pos_av[i+5])
      y1_backword_fit = fit_backword_vtxVspos[1].Eval(Pos_nom[i+5])
      y2_backword_fit = fit_backword_vtxVspos[2].Eval(Pos_DOR[i+5])
      y3_backword_fit = fit_backword_vtxVspos[3].Eval(Pos_arc[i+5])

      resedual_backword_vtxVspos[0].SetPoint(i,Pos_av[i+5],(avVtxPos[i+5] - y0_backword_fit))
      #resedual_backword_vtxVspos[0].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[0].SetPointError(i, 0. , errAvVtxPos[i+5])
      resedual_backword_vtxVspos[1].SetPoint(i,Pos_nom[i+5],(avVtxPos[i+5] - y1_backword_fit))
      #resedual_backword_vtxVspos[1].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[1].SetPointError(i, 0. , errAvVtxPos[i+5])
      resedual_backword_vtxVspos[2].SetPoint(i,Pos_DOR[i+5],(avVtxPos[i+5] - y2_backword_fit))
      #resedual_backword_vtxVspos[2].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[2].SetPointError(i, 0. , errAvVtxPos[i+5])
      resedual_backword_vtxVspos[3].SetPoint(i,Pos_arc[i+5],(avVtxPos[i+5] - y3_backword_fit))
      #resedual_backword_vtxVspos[3].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[3].SetPointError(i, 0. , errAvVtxPos[i+5])

   for j in range(0,4):
      resedual_forward_vtxVspos[j].SetMarkerColor(r.kRed)
      resedual_forward_vtxVspos[j].SetMarkerStyle(21)
      resedual_forward_vtxVspos[j].SetMarkerSize(1.)
      resedual_mg[j].Add(resedual_forward_vtxVspos[j]) 

      resedual_backword_vtxVspos[j].SetMarkerColor(r.kBlue)
      resedual_backword_vtxVspos[j].SetMarkerStyle(21)
      resedual_backword_vtxVspos[j].SetMarkerSize(1.)
      resedual_mg[j].Add(resedual_backword_vtxVspos[j])
      
   for j in range(0,4):    
      canvas[j+10].cd(2)
      canvas[j+10].cd(2).SetPad(0,0,1.0,0.3)
      resedual_mg[j].Draw("PA")
      resedual_mg[j].GetYaxis().SetTitle("Residuals [#mum]")
      resedual_mg[j].GetYaxis().SetLabelSize(0.07)
      resedual_mg[j].GetYaxis().SetTitleSize(0.07)
      resedual_mg[j].GetYaxis().SetTitleOffset(0.5)
      resedual_mg[j].SetTitle("")
      resedual_mg[j].Write()
   for j in range(0,4):
      line[j] = r.TLine(canvas[j+10].cd(2).GetUxmin(), 0.0, canvas[j+10].cd(2).GetUxmax(), 0.0)
      line[j].SetLineColor(14)
      line[j].SetLineStyle(3)
      line[j].Draw() 

   for j in range(0,4): 
      canvas[j+10].cd(1)
      stats1 =forward_vtxVspos[j].GetListOfFunctions().FindObject("stats") 
      if not stats1: 
         continue 
      stats1.__class__ = r.TPaveStats
      stats2 =backword_vtxVspos[j].GetListOfFunctions().FindObject("stats")
      if not stats2: 
         continue 
      stats2.__class__ = r.TPaveStats
      stats1.SetLineWidth (0)
      stats2.SetLineWidth (0)
      stats1.SetTextColor(r.kRed)
      stats1.SetTextSize(0.04)
      stats2.SetTextColor(r.kBlue)
      stats2.SetTextSize(0.04)
      if 'X1' in whichScan:
         latex1 . DrawText (0.2, 0.4 , " X1 scan Forward " )
         stats1.SetX1NDC(0.15) 
         stats1.SetX2NDC(0.50)
         stats1.SetY1NDC(0.15)
         stats1.SetY2NDC(0.38)
         latex2 . DrawText (0.55, 0.8 , " X1 scan Backword " )
         stats2.SetX1NDC(0.50)
         stats2.SetX2NDC(0.85) 
         stats2.SetY1NDC(0.55)
         stats2.SetY2NDC(0.78)
         canvas[j+10].Modified()
         canvas[j+10].Update()
      if 'Y1' in whichScan:
         latex1 . DrawText (0.2,0.8 , " Y1 scan Forward " )
         stats1.SetX1NDC(0.15) 
         stats1.SetX2NDC(0.50)
         stats1.SetY1NDC(0.55)
         stats1.SetY2NDC(0.78)
         latex2 . DrawText (0.55,0.4 , " Y1 scan Backword " )
         stats2.SetX1NDC(0.50)
         stats2.SetX2NDC(0.85) 
         stats2.SetY1NDC(0.15)
         stats2.SetY2NDC(0.38)

   for j in range(0,4):      
      canvas[j+10].SaveAs("calib_"+condition+".root"+"(")
      canvas[j+10].SaveAs(pdfOutFile+"(")

   canvas[14].SaveAs("calib_"+condition+".root"+"]")
   canvas[14].SaveAs(pdfOutFile+"]")

   with open("parameters_"+condition+ ".txt", 'w') as f1:
      f1.write("luminos region from gauss mean and gauss mean error from cms tracker order of results are  avvtxpos errnomax errwithmax of "+ whichScan + "is: \n")
      for item1, item2, item3 in zip(avVtxPos, errAvVtxPos, errAvVtxPos_multiplied_max1chi2):
         f1.write("%s , %s , %s \n" % (item1, item2, item3))
      f1.write("--------------------------- \n")
      f1.write("luminos region from histogram mean and error = rms / sqrt(nentreis) "+ whichScan + "is: \n")
      for item1, item2 in zip(histo_mean, histo_mean_error):
         f1.write("%s , %s  \n" % (item1, item2))
      f1.write("--------------------------- \n")

   with open("slopes_errors_"+condition+".txt", 'w') as f2:
      f2.write("slopes and statistical errors first forward (av , nom, dor, arc) second backward (av , nom, dor, arc) "+ whichScan + "is: \n")
      for item1, item2 in zip(slope_forward, slope_forward_error):
         f2.write("%s , %s  \n" % (item1, item2))
      f2.write("--------------------------- \n")
      for item1, item2 in zip(slope_backward, slope_backward_error):
         f2.write("%s , %s  \n" % (item1, item2))
      f2.write("--------------------------- \n")

   rfile.Write()
   rfile.Close()

if __name__ == '__main__':

   makeCalibPlot("X1", "LScalib_X_nostepsize.root", "plotsLScalib_X_nostepsize.pdf", "X_beam_position_nostepsize")
   makeCalibPlot("X1", "LScalib_X_stepsize_no_outliersremoval.root", "plotsLScalib_X_stepsize_no_outliersremoval.pdf", "X_beam_position_stepsize_no_outliersremoval")
   makeCalibPlot("X1", "LScalib_X_stepsize_using_outliersremoval.root", "plotsLScalib_X_stepsize_using_outliersremoval.pdf", "X_beam_position_stepsize_using_outliersremoval")
   
   makeCalibPlot("Y1", "LScalib_Y_nostepsize.root", "plotsLScalib_Y_nostepsize.pdf", "Y_beam_position_nostepsize")
   makeCalibPlot("Y1", "LScalib_Y_stepsize_no_outliersremoval.root", "plotsLScalib_Y_stepsize_no_outliersremoval.pdf", "Y_beam_position_stepsize_no_outliersremoval")
   makeCalibPlot("Y1", "LScalib_Y_stepsize_using_outliersremoval.root", "plotsLScalib_Y_stepsize_using_outliersremoval.pdf", "Y_beam_position_stepsize_using_outliersremoval")

   

print (datetime.datetime.now())




