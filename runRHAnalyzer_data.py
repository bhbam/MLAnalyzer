import os

cfg='RecHitAnalyzer/python/ConfFile_data_cfg.py'
inputFiles_='file:data_Run2018B_Tau_AOD_15Feb2022_UL2018_v1_2820000_0C6EC09F_736E_B640_AD5A_E99536E72323.root'
#inputFiles_='file:../Run2018A_Tau_AOD_12Nov2019_UL2018_D0938794-D6B0-594C-BB05-5CEE65208347.root'

maxEvents_=10
skipEvents_=0#


cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d"%(cfg,inputFiles_,maxEvents_,skipEvents_)
print '%s'%cmd
os.system(cmd)
