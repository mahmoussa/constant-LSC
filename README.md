# constant-LSC
This code used to calculate Constant Length scale calibration for the 2018 pp Run fill 6868
1- run "legacy_data/find_files.py"  to get the input files for analysis for both the timestamp and lumisection sellection
2- check "stepsize.ods" which contains all the calculations for the two beams positions with/without step size & with/without outliers removals
3- as the difference in results coming from the lumisection and timestamp sellection is very small so it can be neglected. I consentrated here in the timestamp calculation. 
4- calculate the LS correction and its uncertainty using different ways, for example,  if you want to calculate the LS correction and its uncertainty using timestamp sellection after scaling the beam positions with the step size and using outlier removal method and the luminos region errors are scalled with the function max(1,sqrt(chi2/ndf)) run "legacy_data/analysis_time_stepsize_using_outlierremoval.py"
5- To calculate the constant LSC using old data use the same procedure with "old_data" directory.
