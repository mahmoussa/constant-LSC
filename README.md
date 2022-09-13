# constant-LSC
This code used to calculate Constant Length scale calibration for the 2017 pp Run fill 6016 and 2018 data fill 6868
1- run "analysis_code_constant2017/find_files.py"  to get the input files used for both the timestamp and lumisection sellection
2- run "analysis_code_constant2017/analysis_timestamp.py" to get the LS correction and its uncertainty using timestamp sellection
3- run "analysis_code_constant2017/analysis_lumisection.py" to get the LS correction and its uncertainty using lumisection sellection
4- "doros_arc.ods" file contains the Arc & DOROS beam position values.
5- check "step_size_constant_2017.ods" which contains all the calculations for the two beams positions with/without step size & with/without outliers removals
6- the timestamp that used for each step is decided according to the stability plots that appears in the "stability_plots" 
