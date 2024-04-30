#!/bin/bash
for i in {101..999}
do
  echo "Running  file $i"
  cfg="RecHitAnalyzer/python/ConfFile_data_cfg.py"
  inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/signal_withTrigger/GEN_PreMix_HToAATo4Tau_M_3p7_pythia8_2018UL/sim_HToAATo4Tau_M_3p7/240407_130328/0000/AODSIM_HToAATo4Tau_$i.root'
  maxEvents_=-1
  skipEvents_=0
  outputFile_="trigger_test_H_AA_4Tau_signal_$i.root"
  cmd="cmsRun $cfg inputFiles=$inputFiles_ maxEvents=$maxEvents_ skipEvents=$skipEvents_ outputFile=$outputFile_"
  echo "$cmd"
  eval $cmd
done
