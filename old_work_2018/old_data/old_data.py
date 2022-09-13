import os, sys
import ROOT
import math
import numpy as np

#no step size first item "slope" second "stat err" third "chi2/dof"
no_step_av_xscan_forward =  [-0.9975, 0.002982, 0.3484 / 3] 
no_step_av_xscan_backward =  [-0.9987, 0.003184, 0.08146 / 3]
no_step_av_yscan_forward =  [1.006, 0.003939, 0.1439 / 3]
no_step_av_yscan_backward =  [1.005, 0.003854, 0.02045 / 3]

no_step_nom_xscan_forward =  [-0.9916, 0.002965, 1.098 / 3] 
no_step_nom_xscan_backward =  [-0.9954, 0.003173, 0.1085 / 3]
no_step_nom_yscan_forward =  [0.999, 0.003912, 0.4586 / 3]
no_step_nom_yscan_backward =  [0.9998, 0.003834, 0.01231 / 3]

no_step_dor_xscan_forward =  [-0.9992, 0.002987, 0.1162 / 3] 
no_step_dor_xscan_backward =  [-1.001, 0.003191, 0.02038 / 3]
no_step_dor_yscan_forward =  [1.004, 0.003933, 0.1972 / 3]
no_step_dor_yscan_backward =  [1.004, 0.003852, 0.05594 / 3]

no_step_arc_xscan_forward =  [-0.9958, 0.002977, 0.762 / 3] 
no_step_arc_xscan_backward =  [-0.9965, 0.003177, 0.3031 / 3]
no_step_arc_yscan_forward =  [1.007, 0.003945, 0.1856 / 3]
no_step_arc_yscan_backward =  [1.006, 0.003856, 0.00956 / 3]

#step size without outlier removal first item "slope" second "stat err" third "chi2/dof"
no_joscha_av_xscan_forward =  [-0.9925, 0.002967, 0.3507 / 3] 
no_joscha_av_xscan_backward =  [-0.9937, 0.003168, 0.08149 / 3]
no_joscha_av_yscan_forward =  [0.9993, 0.003914, 0.1443 / 3]
no_joscha_av_yscan_backward =  [0.9986, 0.003829, 0.02019 / 3]

no_joscha_nom_xscan_forward =  [-0.9916, 0.002965, 1.098 / 3] 
no_joscha_nom_xscan_backward =  [-0.9954, 0.003173, 0.1085 / 3]
no_joscha_nom_yscan_forward =  [0.999, 0.003912, 0.4586 / 3]
no_joscha_nom_yscan_backward =  [0.9998, 0.003834, 0.01231 / 3]

no_joscha_dor_xscan_forward =  [-0.9922, 0.002967, 0.1186 / 3] 
no_joscha_dor_xscan_backward =  [-0.9939, 0.003169, 0.01998 / 3]
no_joscha_dor_yscan_forward =  []
no_joscha_dor_yscan_backward =  []

no_joscha_arc_xscan_forward =  [-0.9928, 0.002968, 0.7627 / 3] 
no_joscha_arc_xscan_backward =  [-0.9936, 0.003168, 0.3023 / 3]
no_joscha_arc_yscan_forward =  [0.9999, 0.003916, 0.1844 / 3]
no_joscha_arc_yscan_backward =  [0.9983, 0.003828, 0.009497 / 3]

#step size with outlier removal first item "slope" second "stat err" third "chi2/dof"
joscha_av_xscan_forward =  [-0.9936, 0.002971, 0.3502 / 3] 
joscha_av_xscan_backward =  [-0.9948, 0.003172, 0.08149 / 3]
joscha_av_yscan_forward =  [1, 0.003918, 0.1442 / 3]
joscha_av_yscan_backward =  [0.9998, 0.003834, 0.02024 / 3]

joscha_nom_xscan_forward =  [-0.9916, 0.002965, 1.098 / 3] 
joscha_nom_xscan_backward =  [-0.9954, 0.003173, 0.1085 / 3]
joscha_nom_yscan_forward =  [0.999, 0.003912, 0.4586 / 3]
joscha_nom_yscan_backward =  [0.9998, 0.003834, 0.01231 / 3]

joscha_dor_xscan_forward =  [-0.9938, 0.002971, 0.118 / 3] 
joscha_dor_xscan_backward =  [-0.9954, 0.003174, 0.02007 / 3]
joscha_dor_yscan_forward =  [0.9988, 0.003912, 0.1978 / 3]
joscha_dor_yscan_backward =  [0.999, 0.003831, 0.05528 / 3]

joscha_arc_xscan_forward =  [-0.9928, 0.002968, 0.7627 / 3] 
joscha_arc_xscan_backward =  [-0.9936, 0.003168, 0.3023 / 3]
joscha_arc_yscan_forward =  [1.001, 0.00392, 0.1846 / 3]
joscha_arc_yscan_backward =  [0.9993, 0.003832, 0.009506 / 3]



#LSC calculations and its error:
x_scan_LSC = (joscha_av_xscan_forward[0] + joscha_av_xscan_backward[0])/2
y_scan_LSC = (joscha_av_yscan_forward[0] + joscha_av_yscan_backward[0])/2


arc_B1_B2_x = (joscha_arc_xscan_forward[0] + joscha_arc_xscan_backward[0])/2
arc_B1_B2_y = (joscha_arc_yscan_forward[0] + joscha_arc_yscan_backward[0])/2
dor_B1_B2_x = (joscha_dor_xscan_forward[0] + joscha_dor_xscan_backward[0])/2
dor_B1_B2_y = (joscha_dor_yscan_forward[0] + joscha_dor_yscan_backward[0])/2


stat_err_xscan = np.sqrt(((joscha_av_xscan_forward[1])**2 * max(joscha_av_xscan_forward[2],1)) + ((joscha_av_xscan_backward[1])**2 * max(joscha_av_xscan_backward[2],1))) / 2
stat_err_yscan = np.sqrt(((joscha_av_yscan_forward[1])**2 * max(joscha_av_yscan_forward[2],1)) + ((joscha_av_yscan_backward[1])**2 * max(joscha_av_yscan_backward[2],1))) / 2

OD_max_arc_dor_from_xscanLSC= max (abs(arc_B1_B2_x - x_scan_LSC), abs(dor_B1_B2_x - x_scan_LSC))
OD_max_arc_dor_from_yscanLSC= max (abs(arc_B1_B2_y - y_scan_LSC), abs(dor_B1_B2_y - y_scan_LSC))

OD_with_without_outliers_removals_xscan = abs(((no_joscha_av_xscan_forward[0]+no_joscha_av_xscan_backward[0])/2) - x_scan_LSC)
OD_with_without_outliers_removals_yscan = abs(((no_joscha_av_yscan_forward[0]+no_joscha_av_yscan_backward[0])/2) - y_scan_LSC)

OD_forward_backward_xscan= abs(joscha_av_xscan_forward[0] - x_scan_LSC)
OD_forward_backward_yscan= abs(joscha_av_yscan_forward[0] - y_scan_LSC)

'''
#  end of the year data ( no legacy data)
old_data_xscan = -0.9979330
old_data_yscan = 0.9940015

vtx_recostruction_err_xscan = abs(x_scan_LSC - old_data_xscan)
vtx_recostruction_err_yscan = abs(y_scan_LSC - old_data_yscan)
'''
tot_err_xscan = np.sqrt(stat_err_xscan**2 + OD_max_arc_dor_from_xscanLSC**2 + OD_with_without_outliers_removals_xscan**2 + OD_forward_backward_xscan**2 )
tot_err_yscan = np.sqrt(stat_err_yscan**2 + OD_max_arc_dor_from_yscanLSC**2 + OD_with_without_outliers_removals_yscan**2 + OD_forward_backward_xscan**2 )


corr_sigma_vis_const = ((abs(x_scan_LSC)-1) + (abs(y_scan_LSC)-1)) * 100
err_sigma_vis_const = np.sqrt(tot_err_xscan**2 + tot_err_yscan**2)* 100


print ('constant LSC calculations using old data ')
print ('LSC in X scan = %0.7f' %x_scan_LSC)
print ('LSC in Y scan = %0.7f' %y_scan_LSC)
print ('stat. err. X scan = %0.7f' %stat_err_xscan)
print ('stat. err. Y scan = %0.7f' %stat_err_yscan)
print ('OD from the diff. between arc and dor from average X scan = %0.7f' %OD_max_arc_dor_from_xscanLSC)
print ('OD from the diff. between arc and dor from average Y scan = %0.7f' %OD_max_arc_dor_from_yscanLSC)
print ('OD from the diff. with and without outliers removals X scan = %0.7f' %OD_with_without_outliers_removals_xscan)
print ('OD from the diff. with and without outliers removals Y scan = %0.7f' %OD_with_without_outliers_removals_yscan)
print ('OD from the diff. between forward and backward X scan = %0.7f' %OD_forward_backward_xscan)
print ('OD from the diff. between forward and backward Y scan = %0.7f' %OD_forward_backward_yscan)
print ('=============================================================================================')
print ('constant LSC in X scan +- errors = ', '%0.7f' %x_scan_LSC , '+-' , '%0.7f' %tot_err_xscan)
print ('constant LSC in Y scan +- errors = ', '%0.7f' %y_scan_LSC , '+-' , '%0.7f' %tot_err_yscan)
print ('=============================================================================================')
print ('corr. to sigma visible from constant LSC +- errors in % = ' , '%0.7f' % corr_sigma_vis_const, '+-' , '%0.7f' %err_sigma_vis_const)




