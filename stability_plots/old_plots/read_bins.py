import os, sys
import ROOT
import math
import numpy as np
from decimal import Decimal

f_xscan = ROOT.TFile.Open("stability_plots_constant_2017_onlystablexscan.root")
h_timestamp_x = f_xscan.Get("timestamp_x")
timestamps_x_begin=[1501261177,1501261293,1501261409,1501261524,1501261639,1501261769,1501261884,1501261999,1501262114,1501262229]
timestamps_x_end=  [1501261247,1501261362,1501261477,1501261592,1501261707,1501261837,1501261952,1501262067,1501262182,1501262297]
for j in range (int(h_timestamp_x.GetEntries())):
   if h_timestamp_x.GetXaxis().GetBinCenter(j) >=timestamps_x_begin[0] and h_timestamp_x.GetXaxis().GetBinCenter(j) <=timestamps_x_end[0]:
      print("timestamp" , "vtx" )
      print(h_timestamp_x.GetXaxis().GetBinCenter(j) , h_timestamp_x.GetBinContent(j))

