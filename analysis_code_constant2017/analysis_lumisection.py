import ROOT as r
import sys
import os
import pickle
import datetime
import math

print (datetime.datetime.now())
def generateTimeWindows(whichScan,whichVtx):
   if whichScan == "X1":
        begin = [11,16,21,26,31,36,41,46,51,56]
        end =   [12,17,22,27,32,37,42,47,52,57]
   if whichScan == "Y1":
        begin = [72,77,82,87,92,97,102,107,112,117]
        end =   [73,78,83,88,93,98,103,108,113,118]
   return begin, end

def generateOffsetPositions_nostepsize(whichScan):
   if "X1" in whichScan:
      nomPos_av =[ -175.560022483197 , -78.4809501847379 , 19.2742630617799 , 116.699697520274 , 214.207356022252 , 214.787957874149 , 117.014393664282 , 20.058865497455 , -78.6747685058085 , -176.234540675653 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -174.213372023118 , -77.9722937041809 , 19.3330997459534 , 116.270026639508 , 213.331467106409 , 213.738370319191 , 116.715110476237 , 20.1917891875953 , -77.7547890133918 , -175.002936573637 ]
      nomPos_arc = [ -176.906672943276 , -78.9896066652949 , 19.2154263776064 , 117.12936840104 , 215.083244938095 , 215.837545429107 , 117.313676852327 , 19.9259418073147 , -79.5947479982251 , -177.466144777668 ]
   if "Y1" in whichScan:
      nomPos_av =[ -174.033605658325 , -77.7107698993896 , 19.4643090982158 , 117.213603455505 , 214.406774722454 , 214.349154731316 , 116.709599676828 , 19.2636025313228 , -77.7966559339116 , -175.172266479775 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -173.63680023832 , -77.7062996213496 , 19.1045933433742 , 116.228564164308 , 213.211750716169 , 212.366838421221 , 115.428280663843 , 18.2478086433306 , -77.6363542510087 , -174.523975843495 ]
      nomPos_arc = [ -174.43041107833 , -77.7152401774297 , 19.8240248530574 , 118.198642746702 , 215.601798728739 , 216.331471041412 , 117.990918689813 , 20.2793964193149 , -77.9569576168145 , -175.820557116056 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc

def generateOffsetPositions_stepsize_no_outliersremoval(whichScan):
   if "X1" in whichScan:
      nomPos_av =[ -178.834331455572 , -80.936681789019 , 17.6371093255925 , 115.88111515218 , 214.207356022252 , 214.787957874149 , 116.195811296188 , 18.4217117612676 , -81.1305001100896 , -179.508849648027 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -179.73954651194 , -82.1169244457977 , 16.5700132515422 , 114.888477892302 , 213.331467106409 , 213.738370319191 , 115.333561729031 , 17.4287026931841 , -81.8994197550086 , -180.529111062459 ]
      nomPos_arc = [ -177.929116399203 , -79.7564391322404 , 18.7042053996428 , 116.873752412058 , 215.083244938095 , 215.837545429107 , 117.058060863345 , 19.4147208293511 , -80.3615804651705 , -178.488588233595 ]
   if "Y1" in whichScan:
      nomPos_av =[ -178.721952362389 , -81.227029802438 , 17.1201364961836 , 116.041511654489 , 214.406774722454 , 214.349154731316 , 115.537507875812 , 16.9194299292905 , -81.3129158369599 , -179.86061318384 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -180.436365128718 , -82.8059731641478 , 15.7048116481754 , 114.528667816709 , 213.211750716169 , 212.366838421221 , 113.728384316244 , 14.8480269481318 , -82.7360277938069 , -181.323540733893 ]
      nomPos_arc = [ -177.007539596062 , -79.6480864407284 , 18.5354613441916 , 117.554355492269 , 215.601798728739 , 216.331471041412 , 117.34663143538 , 18.9908329104491 , -79.8898038801132 , -178.397685633788 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc

def generateOffsetPositions_stepsize_using_outliersremoval(whichScan):
   if "X1" in whichScan:
      nomPos_av =[ -179.482845382061 , -81.4230672338863 , 17.3128523623477 , 115.718986670558 , 214.207356022252 , 214.787957874149 , 116.033682814566 , 18.0974547980228 , -81.6168855549568 , -180.157363574517 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -179.816959854831 , -82.1749844529655 , 16.531306580097 , 114.86912455658 , 213.331467106409 , 213.738370319191 , 115.314208393309 , 17.3899960217389 , -81.9574797621764 , -180.60652440535 ]
      nomPos_arc = [ -178.705681424644 , -80.3388629013209 , 18.3159228869224 , 116.679611155698 , 215.083244938095 , 215.837545429107 , 116.863919606985 , 19.0264383166307 , -80.9440042342511 , -179.265153259036 ]
   if "Y1" in whichScan:
      nomPos_av =[ -178.194872682362 , -80.8317200424172 , 17.3836763361974 , 116.173281574496 , 214.406774722454 , 214.349154731316 , 115.669277795819 , 17.1829697693044 , -80.9176060769392 , -179.333533503812 ]
      nomPos=[ -177.1511625 , -78.7338505 , 19.683462 , 118.100768 , 216.518085 , 216.518085 , 118.100768 , 19.683462 , -78.7338505 , -177.1511625 ]
      nomPos_DOR = [ -179.356246599723 , -81.995884267402 , 16.2448709126726 , 114.798697448957 , 213.211750716169 , 212.366838421221 , 113.998413948492 , 15.388086212629 , -81.9259388970611 , -180.243422204898 ]
      nomPos_arc = [ -176.40304882768 , -79.1947183644425 , 18.8377067283822 , 117.705478184364 , 215.601798728739 , 216.331471041412 , 117.497754127475 , 19.2930782946397 , -79.4364358038273 , -177.793194865406 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc

def makeCalibPlot(whichScan,rootOutFile,pdfOutFile,condition):
   if 'X1' in whichScan:
        whichVtx = "vtx_x" 

   if 'Y1' in whichScan:
        whichVtx = "vtx_y"

   print "Now for scan ", whichScan, " and vtx coordinate ", whichVtx

   filelist = os.listdir("./")

   chain = r.TChain("lumi/tree")

   with open('./filesFor_ls_Scan.pkl', 'rb') as f:
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

      stringCond = "run == 300050 " + "&& LS >= " + str(beginTS[index]) + "&& LS <= " + str(endTS[index]) + "&& nVtx >= 1 " + " && vtx_isGood"
      print stringCond
      chain.Draw(whichVtx + " >>hist"+str(index), stringCond)
               
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
         mg[j].SetTitle("lumisection scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_av separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_av in microns")
         mg[j].GetYaxis().SetTitle("Pos_av" + whichVtx + "  in microns")
  
      elif j == 1:
         mg[j].SetTitle("lumisection scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_nom separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_nom in microns")
         mg[j].GetYaxis().SetTitle("Pos_nom" + whichVtx + "  in microns")

      elif j == 2:
         mg[j].SetTitle("lumisection scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_DOR separation in microns")
         mg[j].GetXaxis().SetTitle("Pos_DOR in microns")
         mg[j].GetYaxis().SetTitle("Pos_DOR" + whichVtx + "  in microns")
         
      elif j == 3:
         mg[j].SetTitle("lumisection scan " + whichScan + ": Mean " + whichVtx + " position in microns vs Pos_arc separation in microns")
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




