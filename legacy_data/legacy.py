import os, sys
import ROOT
import math
import numpy as np

#no step size first item "slope" second "stat err" third "chi2/dof"
no_step_av_xscan_forward =  [-0.9978, 0.00299 , 0.368 / 3] 
no_step_av_xscan_backward =  [-0.999, 0.003127 , 0.1067 / 3]
no_step_av_yscan_forward =  [1.006 , 0.003937, 0.1299 / 3]
no_step_av_yscan_backward =  [1.005, 0.003753, 0.02875 / 3]
print(no_step_av_xscan_forward[0]-1,no_step_av_xscan_forward[1]-1,no_step_av_xscan_forward[2]-1)

no_step_nom_xscan_forward =  [-0.9919, 0.002973, 1.12 / 3] 
no_step_nom_xscan_backward =  [-0.9958, 0.003117, 0.1446 / 3]
no_step_nom_yscan_forward =  [0.9989, 0.003911, 0.4671 / 3]
no_step_nom_yscan_backward =  [0.9996, 0.003733, 0.02573 / 3]

no_step_dor_xscan_forward =  [-0.9995, 0.002995, 0.1475 / 3] 
no_step_dor_xscan_backward =  [-1.001, 0.003134, 0.02246 / 3]
no_step_dor_yscan_forward =  [1.004, 0.003931, 0.1903 / 3]
no_step_dor_yscan_backward =  [1.004, 0.003751, 0.06596 / 3]

no_step_arc_xscan_forward =  [-0.9961, 0.002985 , 0.7726 / 3] 
no_step_arc_xscan_backward =  [-0.9969, 0.00312 , 0.3567 / 3]
no_step_arc_yscan_forward =  [1.007, 0.003943 , 0.1649 / 3]
no_step_arc_yscan_backward =  [1.005, 0.003755, 0.0176 / 3]

#step size without outlier removal first item "slope" second "stat err" third "chi2/dof"
no_joscha_av_xscan_forward =  [-0.9929, 0.002975 , 0.3703 / 3] 
no_joscha_av_xscan_backward =  [-0.9941, 0.003112, 0.1068 / 3]
no_joscha_av_yscan_forward =  [0.9992, 0.003912, 0.1305 / 3]
no_joscha_av_yscan_backward =  [0.9985, 0.003729, 0.02852 / 3]

no_joscha_nom_xscan_forward =  [-0.9919, 0.002973 , 1.12 / 3] 
no_joscha_nom_xscan_backward =  [-0.9958, 0.003117, 0.1446 / 3]
no_joscha_nom_yscan_forward =  [0.9989, 0.003911, 0.4671 / 3]
no_joscha_nom_yscan_backward =  [0.9996, 0.003733, 0.02573 / 3]

no_joscha_dor_xscan_forward =  [-0.9925, 0.002974, 0.1497 / 3] 
no_joscha_dor_xscan_backward =  [-0.9942, 0.003112, 0.02226 / 3]
no_joscha_dor_yscan_forward =  []
no_joscha_dor_yscan_backward =  []

no_joscha_arc_xscan_forward =  [-0.9932, 0.002976, 0.7733 / 3] 
no_joscha_arc_xscan_backward =  [-0.994, 0.003111, 0.356 / 3]
no_joscha_arc_yscan_forward =  [0.9998, 0.003914, 0.1639 / 3]
no_joscha_arc_yscan_backward =  [0.9981, 0.003728, 0.01758 / 3]

#step size with outlier removal first item "slope" second "stat err" third "chi2/dof"
joscha_av_xscan_forward =  [-0.994, 0.002979, 0.3698 / 3] 
joscha_av_xscan_backward =  [-0.9952, 0.003115, 0.1068 / 3]
joscha_av_yscan_forward =  [1, 0.003916, 0.1304 / 3]
joscha_av_yscan_backward =  [0.9996, 0.003733, 0.02856 / 3]

joscha_nom_xscan_forward =  [-0.9919, 0.002973, 1.12 / 3] 
joscha_nom_xscan_backward =  [-0.9958, 0.003117, 0.1446 / 3]
joscha_nom_yscan_forward =  [0.9989, 0.003911, 0.4671 / 3]
joscha_nom_yscan_backward =  [0.9996, 0.003733, 0.02573 / 3]

joscha_dor_xscan_forward =  [-0.9941, 0.002979, 0.1492 / 3] 
joscha_dor_xscan_backward =  [-0.9958, 0.003117, 0.02231 / 3]
joscha_dor_yscan_forward =  [0.9987, 0.00391, 0.191 / 3]
joscha_dor_yscan_backward =  [0.9988, 0.00373, 0.06529 / 3]

joscha_arc_xscan_forward =  [-0.9932, 0.002976, 0.7733 / 3] 
joscha_arc_xscan_backward =  [-0.994, 0.003111, 0.356 / 3]
joscha_arc_yscan_forward =  [1.001, 0.003918, 0.1641 / 3]
joscha_arc_yscan_backward =  [0.9991, 0.003731, 0.01758 / 3]



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


#  end of the year data ( no legacy data)
old_data_xscan = -0.9979330
old_data_yscan = 0.9940015

vtx_recostruction_err_xscan = abs(x_scan_LSC - old_data_xscan)
vtx_recostruction_err_yscan = abs(y_scan_LSC - old_data_yscan)

tot_err_xscan = np.sqrt(stat_err_xscan**2 + OD_max_arc_dor_from_xscanLSC**2 + OD_with_without_outliers_removals_xscan**2 + OD_forward_backward_xscan**2 + vtx_recostruction_err_xscan**2)
tot_err_yscan = np.sqrt(stat_err_yscan**2 + OD_max_arc_dor_from_yscanLSC**2 + OD_with_without_outliers_removals_yscan**2 + OD_forward_backward_xscan**2 + vtx_recostruction_err_yscan**2)


corr_sigma_vis_const = ((abs(x_scan_LSC)-1) + (abs(y_scan_LSC)-1)) * 100
err_sigma_vis_const = np.sqrt(tot_err_xscan**2 + tot_err_yscan**2)* 100


print ('constant LSC calculations using legacy data ')
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
print ('vtx reconstruction err. X scan = %0.7f' %vtx_recostruction_err_xscan)
print ('vtx reconstruction err. Y scan = %0.7f' %vtx_recostruction_err_yscan)
print ('=============================================================================================')
print ('constant LSC in X scan +- errors = ', '%0.7f' %x_scan_LSC , '+-' , '%0.7f' %tot_err_xscan)
print ('constant LSC in Y scan +- errors = ', '%0.7f' %y_scan_LSC , '+-' , '%0.7f' %tot_err_yscan)
print ('=============================================================================================')
print ('corr. to sigma visible from constant LSC +- errors in % = ' , '%0.7f' % corr_sigma_vis_const, '+-' , '%0.7f' %err_sigma_vis_const)




