import ROOT as r
import sys
import os
import pickle
import datetime
import math

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
      nomPos_av=[-179.048061317784, -81.3845623211054, 17.3849244342332, 115.739074131749, 213.996033757535, 214.899554788786, 116.48600770166, 17.7667595358507, -80.7363534211701, -179.409381472895]   
      nomPos =[-177.1544348434, -78.735305460925, 19.68382392155, 118.102953304025, 216.5220826865, 216.5220826865, 118.102953304025, 19.68382392155, -78.735305460925, -177.1544348434]
      nomPos_DOR =[-179.710534819639 ,-82.3736886928571 , 16.521695013145, 114.978168935244, 213.357857142857, 214.514285714286, 116.311383220958, 17.6892778288801, -80.8599205769151, -179.770353660219]
      nomPos_arc =[-178.385587815929, -80.3954359493537, 18.2481538553213, 116.499979328253, 214.634210372214, 215.284823863286, 116.660632182361, 17.8442412428213, -80.612786265425, -179.048409285572]
   if "Y1" in whichScan:
      nomPos_av =[-176.1615524655, -78.5137744716666, 19.9986254855094, 118.605839946013, 217.183368932535, 216.808956122791, 118.382432862654, 19.715520391158, -78.92400441059, -177.199153816173]
      nomPos =[-177.1544348434, -78.735305460925, 19.68382392155, 118.102953304025, 216.5220826865, 216.5220826865, 118.102953304025, 19.68382392155, -78.735305460925, -177.1544348434]
      nomPos_DOR =[-176.430835026679, -78.5455895727743, 19.9935959691796, 118.778625715782, 217.096071428571, 216.468478260869, 118.054609152635, 19.3458329202981, -79.2698338791925, -177.357646620882]
      nomPos_arc =[-175.892269904322, -78.481959370559, 20.0036550018392, 118.433054176245, 217.2706664365, 217.149433984714, 118.710256572673, 20.0852078620178, -78.5781749419876, -177.040661011464]
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
  
   rfile = r.TFile(rootOutFile,"recreate")
   print "ok text0-1-2-3"
   canvas = [r.TCanvas() for i in range(0,15)]

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
   chi2_ndfAvVtxPos = [0.0 for entry in beginTS]
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

      stringCond = "run == 319019 " + "&& timeStamp_begin >= " + str(beginTS[index]) + " && timeStamp_begin <= " + str(endTS[index]) + "&& nVtx >= 1 " + " && vtx_isGood"
      print stringCond
      chain.Draw(whichVtx + " >>hist"+str(index), stringCond)
               
      histoList[index]= r.gDirectory.Get("hist"+str(index))
      histoList[index].GetXaxis().SetTitle(whichVtx + " [cm]")
      histoList[index].GetYaxis().SetTitle("Offset in [#mum]")
      histoList[index].SetTitle("%i" %index)
      if histoList[index].GetEntries()==0:
         continue
        
      histoList[index].Fit("gaus")
      fit = histoList[index].GetFunction("gaus")
      avVtxPos[index]=fit.GetParameter(1)*10000
      errAvVtxPos[index] = fit.GetParError(1)*10000
      chi2_ndfAvVtxPos[index] = (fit.GetChisquare()/ fit.GetNDF())
      canvas[index].cd()              
      histoList[index].Draw()
      histoList[index].Write()
      canvas[index].SaveAs(pdfOutFile+"(")

   for i in range(0,5):
      forward_vtxVspos[0].SetPoint(i, Pos_av[i],avVtxPos[i])
      forward_vtxVspos[0].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[1].SetPoint(i, Pos_nom[i],avVtxPos[i])
      forward_vtxVspos[1].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[2].SetPoint(i, Pos_DOR[i],avVtxPos[i])
      forward_vtxVspos[2].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      forward_vtxVspos[3].SetPoint(i, Pos_arc[i],avVtxPos[i])
      forward_vtxVspos[3].SetPointError(i, 0. ,errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))

      backword_vtxVspos[0].SetPoint(i, Pos_av[i+5],avVtxPos[i+5])
      backword_vtxVspos[0].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[1].SetPoint(i, Pos_nom[i+5],avVtxPos[i+5])
      backword_vtxVspos[1].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[2].SetPoint(i, Pos_DOR[i+5],avVtxPos[i+5])
      backword_vtxVspos[2].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      backword_vtxVspos[3].SetPoint(i, Pos_arc[i+5],avVtxPos[i+5])
      backword_vtxVspos[3].SetPointError(i, 0. ,errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      
   for j in range(0,4):
      forward_vtxVspos[j].SetLineWidth(2)
      forward_vtxVspos[j].SetMarkerColor(r.kRed)
      forward_vtxVspos[j].SetMarkerStyle(21)
      forward_vtxVspos[j].SetMarkerSize(0.5)
      forward_vtxVspos[j].Fit("pol1")
      fit_forward_vtxVspos.append(forward_vtxVspos[j].GetFunction("pol1"))
      mg[j].Add(forward_vtxVspos[j]) 

      backword_vtxVspos[j].SetLineWidth(2)
      backword_vtxVspos[j].SetMarkerColor(r.kBlue)
      backword_vtxVspos[j].SetMarkerStyle(20)
      backword_vtxVspos[j].SetMarkerSize(0.5)
      backword_vtxVspos[j].Fit("pol1")
      fit_backword_vtxVspos.append(backword_vtxVspos[j].GetFunction("pol1")) 
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
      resedual_forward_vtxVspos[0].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[1].SetPoint(i,Pos_nom[i],(avVtxPos[i] - y1_forward_fit))
      resedual_forward_vtxVspos[1].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[2].SetPoint(i,Pos_DOR[i],(avVtxPos[i] - y2_forward_fit))
      resedual_forward_vtxVspos[2].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))
      resedual_forward_vtxVspos[3].SetPoint(i,Pos_arc[i],(avVtxPos[i] - y3_forward_fit))
      resedual_forward_vtxVspos[3].SetPointError(i, 0. , errAvVtxPos[i]*max(1,math.sqrt(chi2_ndfAvVtxPos[i])))

      y0_backword_fit = fit_backword_vtxVspos[0].Eval(Pos_av[i+5])
      y1_backword_fit = fit_backword_vtxVspos[1].Eval(Pos_nom[i+5])
      y2_backword_fit = fit_backword_vtxVspos[2].Eval(Pos_DOR[i+5])
      y3_backword_fit = fit_backword_vtxVspos[3].Eval(Pos_arc[i+5])

      resedual_backword_vtxVspos[0].SetPoint(i,Pos_av[i+5],(avVtxPos[i+5] - y0_backword_fit))
      resedual_backword_vtxVspos[0].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[1].SetPoint(i,Pos_nom[i+5],(avVtxPos[i+5] - y1_backword_fit))
      resedual_backword_vtxVspos[1].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[2].SetPoint(i,Pos_DOR[i+5],(avVtxPos[i+5] - y2_backword_fit))
      resedual_backword_vtxVspos[2].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))
      resedual_backword_vtxVspos[3].SetPoint(i,Pos_arc[i+5],(avVtxPos[i+5] - y3_backword_fit))
      resedual_backword_vtxVspos[3].SetPointError(i, 0. , errAvVtxPos[i+5]*max(1,math.sqrt(chi2_ndfAvVtxPos[i+5])))

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
      canvas[j+10].SaveAs("calib_"+whichScan+".root"+"(")
      canvas[j+10].SaveAs(pdfOutFile+"(")

   canvas[14].SaveAs("calib_"+whichScan+".root"+"]")
   canvas[14].SaveAs(pdfOutFile+"]")
   rfile.Write()
   rfile.Close()

if __name__ == '__main__':

   makeCalibPlot("X1", "LScalib_X.root", "plotsLScalib_X.pdf")

   makeCalibPlot("Y1", "LScalib_Y.root", "plotsLScalib_Y.pdf")

print (datetime.datetime.now())




