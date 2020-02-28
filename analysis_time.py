import ROOT as r
import sys
import os
import pickle
import datetime

print (datetime.datetime.now())
def generateTimeWindows(whichScan,whichVtx):
   if whichScan == "X1":
        begin = [1530413319, 1530413436, 1530413552, 1530413667, 1530413784,
           1530413915, 1530414041, 1530414157, 1530414274, 1530414389]
        end = [1530413388, 1530413504, 1530413621, 1530413736, 1530413853,
           1530413984, 1530414110, 1530414225, 1530414342, 1530414457]
   if whichScan == "Y1":
        begin = [1530414711, 1530414829, 1530414947, 1530415063, 1530415181,
           1530415314, 1530415432, 1530415548, 1530415666, 1530415784]
        end = [1530414779, 1530414897, 1530415015, 1530415132, 1530415250,
           1530415382, 1530415500, 1530415618, 1530415735, 1530415853]
   return begin, end

def generateOffsetPositions(whichScan):
   if "X1" in whichScan: 
      nomPos_av =[ -177.106960056178, -79.9287368402516, 18.3554769277857, 116.224350378425, 213.996033757535, 214.899554788786, 116.971283948336, 18.7373120294032, -79.2805279403163, -177.46828021129 ]   
      nomPos =[ -177.154432982, -78.735303599525, 19.6838229895, 118.1029528381, 216.5220826865, 216.5220826865, 118.1029528381, 19.6838229895, -78.735303599525, -177.154432982 ]
      nomPos_DOR =[ -176.9775, -80.3239130434782, 17.8882142857143, 115.661428571429, 213.357857142857, 214.514285714286, 116.994642857143, 19.0557971014493, -78.8101449275362, -177.03731884058 ]
      nomPos_arc =[ -177.236420112357, -79.533560637025, 18.8227395698571, 116.787272185421, 214.634210372214, 215.284823863286, 116.947925039529, 18.4188269573571, -79.7509109530964, -177.899241582 ]
   if "Y1" in whichScan:
      nomPos_av =[ -173.665463423454, -76.641708155482, 21.2466718692826, 119.2298631378, 217.183368932535, 216.808956122792, 119.006456054441, 20.9635667749311, -77.0519380944053, -174.703064774126 ]
      nomPos =[ -177.154432982, -78.735303599525, 19.6838229895, 118.1029528381, 216.5220826865, 216.5220826865, 118.1029528381, 19.6838229895, -78.735303599525, -177.154432982 ]
      nomPos_DOR =[ -174.273913043479, -76.9278985507246, 21.0720588235294, 119.317857142857, 217.096071428571, 216.468478260869, 118.59384057971, 20.4242957746479, -77.6521428571428, -175.200724637682 ]
      nomPos_arc =[ -173.057013803429, -76.3555177602393, 21.4212849150357, 119.141869132743, 217.2706664365, 217.149433984714, 119.419071529171, 21.5028377752143, -76.4517333316679, -174.205404910571 ]
   return nomPos_av , nomPos , nomPos_DOR , nomPos_arc



def makeCalibPlot(whichScan,rootOutFile,pdfOutFile):
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
   Pos_av , Pos_nom , Pos_DOR , Pos_arc = generateOffsetPositions(whichScan)
   text0= "av_arc_DOR pos"
   text1= "nominal pos"
   text2= "DOROS pos"
   text3= "arc pos"
   rfile = r.TFile(rootOutFile,"recreate")
   print "ok text0-1-2-3"
   canvas = r.TCanvas()
#    r.gStyle.SetPalette(1)
   r.gStyle.SetOptStat(1) #show normal statistics
   r.gStyle.SetOptFit(1)  #show fit statistics
   if whichVtx == "vtx_y":
      r.gStyle.SetStatX(0.8)
      r.gStyle.SetStatY(0.5)
   if whichVtx == "vtx_x":
      r.gStyle.SetStatX(0.5)
      r.gStyle.SetStatY(0.55)
   
   hist = r.TH1F("hist",whichScan + " scan, " + whichVtx, 150, -0.2, 0.2) # hardcoded
   hList = [r.TH1F() for entry in beginTS]
   histoList = [r.TH1F() for entry in beginTS]
   avVtxPos = [0.0 for entry in beginTS]
   errAvVtxPos = [0.0 for entry in beginTS]
   mg = [r.TMultiGraph()for i in range(0,4)]
   forward_vtxVspos=[r.TGraphErrors()for i in range(0,4)]
   backword_vtxVspos=[r.TGraphErrors()for i in range(0,4)]
   latex1 = r . TLatex ()
   latex2 = r . TLatex ()
   latex1 . SetNDC ()
   latex2 . SetNDC ()
   latex1 . SetTextColor(r.kRed)
   latex2 . SetTextColor(r.kBlue)
   latex1.SetTextFont(42)
   latex2.SetTextFont(42)
   #mg.SetTitle("timestamp scan " + whichScan + ": Mean " + whichVtx + " position in microns vs average" +  text + " separation in microns")
   print "all definitions are ok"
   for index, value in enumerate(beginTS):
      hList[index] = hist.Clone()
      hList[index].SetName("hist"+str(index))

      stringCond = "run == 319019 " + "&& timeStamp_begin >= " + str(beginTS[index]) + " && timeStamp_begin <= " + str(endTS[index]) + "&& nVtx >= 1 " + " && vtx_isGood"
      print stringCond
      chain.Draw(whichVtx + " >>hist"+str(index), stringCond)
               
      histoList[index]= r.gDirectory.Get("hist"+str(index))
      histoList[index].GetXaxis().SetTitle(whichVtx + " [mm]")
      histoList[index].GetYaxis().SetTitle("Offset in [#mum]")
      histoList[index].SetTitle("%i" %index)
      if histoList[index].GetEntries()==0:
         continue
        
      histoList[index].Fit("gaus")
      fit = histoList[index].GetFunction("gaus")
      avVtxPos[index]=fit.GetParameter(1)
      errAvVtxPos[index] = fit.GetParError(1)                
      histoList[index].Draw()
      histoList[index].Write()
      canvas.SaveAs(pdfOutFile+"(")
   
   #canvas.SetPad(0,0.3,1.0,1.0)
   for i in range(0,5):
      forward_vtxVspos[0].SetPoint(i, Pos_av[i],10000*avVtxPos[i])
      forward_vtxVspos[0].SetPointError(i, 0. ,10000*errAvVtxPos[i])
      forward_vtxVspos[1].SetPoint(i, Pos_nom[i],10000*avVtxPos[i])
      forward_vtxVspos[1].SetPointError(i, 0. ,10000*errAvVtxPos[i])
      forward_vtxVspos[2].SetPoint(i, Pos_DOR[i],10000*avVtxPos[i])
      forward_vtxVspos[2].SetPointError(i, 0. ,10000*errAvVtxPos[i])
      forward_vtxVspos[3].SetPoint(i, Pos_arc[i],10000*avVtxPos[i])
      forward_vtxVspos[3].SetPointError(i, 0. ,10000*errAvVtxPos[i])
   for j in range(0,4):
      forward_vtxVspos[j].SetLineWidth(2)
      forward_vtxVspos[j].SetMarkerColor(r.kRed)
      forward_vtxVspos[j].SetMarkerStyle(21)
      forward_vtxVspos[j].SetMarkerSize(0.5)
      forward_vtxVspos[j].Fit("pol1")
      mg[j].Add(forward_vtxVspos[j]) 
 
   
   for i in range(5,10):
      backword_vtxVspos[0].SetPoint(i-5, Pos_av[i],10000*avVtxPos[i])
      backword_vtxVspos[0].SetPointError(i-5, 0. ,10000*errAvVtxPos[i])
      backword_vtxVspos[1].SetPoint(i-5, Pos_nom[i],10000*avVtxPos[i])
      backword_vtxVspos[1].SetPointError(i-5, 0. ,10000*errAvVtxPos[i])
      backword_vtxVspos[2].SetPoint(i-5, Pos_DOR[i],10000*avVtxPos[i])
      backword_vtxVspos[2].SetPointError(i-5, 0. ,10000*errAvVtxPos[i])
      backword_vtxVspos[3].SetPoint(i-5, Pos_arc[i],10000*avVtxPos[i])
      backword_vtxVspos[3].SetPointError(i-5, 0. ,10000*errAvVtxPos[i])

   for j in range(0,4):
      backword_vtxVspos[j].SetLineWidth(2)
      backword_vtxVspos[j].SetMarkerColor(r.kBlue)
      backword_vtxVspos[j].SetMarkerStyle(20)
      backword_vtxVspos[j].SetMarkerSize(0.5)
      backword_vtxVspos[j].Fit("pol1")
      mg[j].Add(backword_vtxVspos[j]) 
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
      canvas.Update()
      stats1 =forward_vtxVspos[j].GetListOfFunctions().FindObject("stats")
      stats2 =backword_vtxVspos[j].GetListOfFunctions().FindObject("stats")
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
      canvas.SaveAs(pdfOutFile+"(")
      canvas.SaveAs("calib_"+whichScan+".root"+"(")
   #canvas.Modified()
   #canvas.SaveAs(pdfOutFile+"(")
   #canvas.SaveAs("calib_"+whichScan+".root")

   #canvas.SaveAs(pdfOutFile+"(")
   canvas.SaveAs(pdfOutFile+"]")

   

   rfile.Write()
   rfile.Close()

if __name__ == '__main__':

   makeCalibPlot("X1", "LScalib_X.root", "plotsLScalib_X.pdf")

   makeCalibPlot("Y1", "LScalib_Y.root", "plotsLScalib_Y.pdf")

print (datetime.datetime.now())



