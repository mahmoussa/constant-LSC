import ROOT as r
import datetime

print (datetime.datetime.now())

def pruneTrees(filename):
    file= r.TFile.Open(filename)
    print 'filename :', filename
    import sys
    whichZeroBias = filename[69:91] #hard-coded -14 root://eoscms/
    if 'ZeroBias' not in whichZeroBias:
        print "Problem with form of filename, assumed to be of a form such that filename[93:105] == ZeroBias, please check"
        sys.exit(1)

    namePrunedNtupleFile = whichZeroBias +"_"+ filename.split('/')[-1]

    oldtree = file.Get("lumi/tree")

    from array import array

    event = array('i', [0])

    oldtree.SetBranchAddress("event",event)
    oldtree.SetBranchStatus("*",0);
    oldtree.SetBranchStatus("run",1);
    oldtree.SetBranchStatus("bunchCrossing",1)
    oldtree.SetBranchStatus("LS",1)
    oldtree.SetBranchStatus("timeStamp_begin",1)
    oldtree.SetBranchStatus("timeStamp_end",1)
    oldtree.SetBranchStatus("event",1)
    oldtree.SetBranchStatus("nVtx",1)
    oldtree.SetBranchStatus("vtx_x",1)
    oldtree.SetBranchStatus("vtx_y",1)
    oldtree.SetBranchStatus("vtx_z",1)
    oldtree.SetBranchStatus("vtx_xError",1)
    oldtree.SetBranchStatus("vtx_yError",1)
    oldtree.SetBranchStatus("vtx_isGood",1)
    oldtree.SetBranchStatus("vtx_isValid",1)
    oldtree.SetBranchStatus("vtx_isFake",1)
    oldtree.SetBranchStatus("vtx_nTrk",1)


#Create a new file + a clone of old tree header. Do not copy events
    newfile = r.TFile(namePrunedNtupleFile,"recreate")
    newtree = oldtree.CloneTree(0);

    newtree.GetBranch("event")
    newtree.GetBranch("run")
    newtree.GetBranch("LS")
    newtree.GetBranch("bunchCrossing")
    newtree.GetBranch("timeStamp_begin")
    newtree.GetBranch("timeStamp_end")
    newtree.GetBranch("nVtx")
    newtree.GetBranch("vtx_x")
    newtree.GetBranch("vtx_y")
    newtree.GetBranch("vtx_z")
    newtree.GetBranch("vtx_xError")
    newtree.GetBranch("vtx_yError")
    newtree.GetBranch("vtx_isGood")
    newtree.GetBranch("vtx_isValid")
    newtree.GetBranch("vtx_isFake")
    newtree.GetBranch("vtx_nTrk")

    newtree.CopyEntries(oldtree);

    newtree.Write()
    newfile.Close()

    return

if __name__ == '__main__':
   constant_scan = ['X1', 'Y1']
   constant_run = {'X1': 319019, 'Y1': 319019}
   constant_ls_range = {'X1': [326, 385], 'Y1': [386, 445]} 
   constant_timestamp_range = {'X1': [1530413201, 1530414593], 'Y1': [1530414594, 1530415971]}

   #prefix = "root://eoscms//eos/cms"
   constant_dirListEOS = [
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias1/crab_CMSSW_10_3_2_ZeroBias1_splitPerBXTrue/190130_015032/0000',
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias2/crab_CMSSW_10_3_2_ZeroBias2_splitPerBXTrue/190130_015051/0000',
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias3/crab_CMSSW_10_3_2_ZeroBias3_splitPerBXTrue/190203_194352/0000',
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias4/crab_CMSSW_10_3_2_ZeroBias4_splitPerBXTrue/190130_015127/0000',
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias5/crab_CMSSW_10_3_2_ZeroBias5_splitPerBXTrue/190203_194427/0000',
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias7/crab_CMSSW_10_3_2_ZeroBias7_splitPerBXTrue/190203_194457/0000',
    '/eos/cms/store/group/comm_luminosity/PCC/ForLumiComputation/2018/NormalFills/'+
    '6847_And_6854_And_6868/ZeroBias8/crab_CMSSW_10_3_2_ZeroBias8_splitPerBXTrue/190130_015238/0000'
   ]
   constant_filesFor_ls_Scan = {"X1":[], "Y1":[]}
   constant_filesFor_timestamp_Scan = {"X1":[], "Y1":[]}
   constant_fileswithLSinfo = []
   constant_fileswithtimestampinfo = []
# subprocess exists only from python 2.7 onwards, so need to do cmsenv under a CMSSW release before running this script
   import subprocess

   for entry in constant_dirListEOS:

        print ">>>> Now at dir ", entry
        constant_filenames=[]
        constant_fileinfos=subprocess.check_output(["ls", entry])
        print constant_fileinfos
        constant_fileinfos=constant_fileinfos.split("\n")
        
        for fileinfo in constant_fileinfos:
            info=fileinfo.split()
            if len(info)!=1:
                continue
            filename=info[0]
            if filename.find(".root") != -1:
                constant_filenames.append(entry+"/"+filename)
# here we have all root files now inside the constant_filenames
   
        print constant_filenames

   
        for filename in constant_filenames:
            tfile=r.TFile.Open(filename)
            ttree = tfile.Get("lumi/tree")
            
            searchCond_lumisection = ""
            searchCond_timestamp = ""
            for scanName in constant_scan:
               
                searchCond_lumisection = "run==" + str(constant_run[scanName]) + \
                    "&&LS>=" + str(constant_ls_range[scanName][0]) + \
                    "&&LS<=" + str(constant_ls_range[scanName][1])

                searchCond_timestamp = "run==" + str(constant_run[scanName]) + \
                    "&&timeStamp_begin>=" + str(constant_timestamp_range[scanName][0]) + \
                    "&&timeStamp_begin<=" + str(constant_timestamp_range[scanName][1])
                
                print searchCond_lumisection
                found_ls = 0
                try:
                    found_ls = ttree.GetEntries(searchCond_lumisection)
                except:
                    print "Failed to GetEntries for",filename
                else:
                    if found_ls:
                        constant_fileswithLSinfo.append(filename)
                        constant_filesFor_ls_Scan[scanName].append(filename)
                        # here he found a root file belonging to the ls condition
                        print 'found for ls~~~~~~~~~~~', filename, scanName, constant_filesFor_ls_Scan[scanName]
                        #break

                print searchCond_timestamp
                found_time = 0
                try:
                    found_time = ttree.GetEntries(searchCond_timestamp)
                except:
                    print "Failed to GetEntries for",filename
                else:
                    if found_time:
                        constant_fileswithtimestampinfo.append(filename)
                        constant_filesFor_timestamp_Scan[scanName].append(filename)
                        # here he found a root file belonging to the ls condition
                        print 'found for timestsmp~~~~~~~~~~~', filename, scanName, constant_filesFor_timestamp_Scan[scanName]
                        #break

   import pickle
   with open('./filesFor_ls_Scan.pkl', 'wb') as f1:
        pickle.dump(constant_filesFor_ls_Scan, f1)

   with open('./filesFor_time_Scan.pkl', 'wb') as f2:
        pickle.dump(constant_filesFor_timestamp_Scan, f2)


   print constant_fileswithLSinfo
   print constant_fileswithtimestampinfo


print (datetime.datetime.now())


