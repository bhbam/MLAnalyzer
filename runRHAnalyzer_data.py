import os

cfg='RecHitAnalyzer/python/ConfFile_data_cfg.py'
# cfg='RecHitAnalyzer/python/ConfFile_cfg.py'
#inputFiles_='file:/eos/cms/store/group/phys_heavyions/rchudasa/e2e/eventGenerationChecks/digiToRecoStep_753_QCD_Pt-15to7000.root' #QCD
#inputFiles_='file:/eos/cms/store/group/phys_heavyions/rchudasa/e2e/eventGenerationChecks/digiToRecoStep_318_Wjets.root' #QCD
#inputFiles_='file:/eos/uscms/store/group/lpcml/bbbam/MCGeneration/gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/sim_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/230512_123635/0000/SIM_HToAAToTauTau_M10_2018UL_withPU_66.root' #H->AA->4Tau
#inputFiles_='file:/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_pythia8/GJet_Pt-20to40_DoubleEMEnriched_DIGI-RECO-v2/230226_161718/0000/digiToReco_withPileup_605.root' #GJet
#inputFiles_='file:/eos/uscms/store/group/lpcml/bbbam/MCGeneration/TTToHadronic_TuneCP5_13TeV_powheg-pythia8/TTToHadronic_TuneCP5_13TeV_powheg-pythia8_DIGI-RECO/230225_224742/0000/digiToReco_GluGluHtoTauTau_126.root' #TTbar hadronic
#inputFiles_='file:/eos/uscms/store/group/lpcml/bbbam/MCGeneration/GluGluHToTauTau_Hadronic_M125_13TeV_powheg_pythia8/GluGluHToTauTau_Hadronic_M125_13TeV_powheg_pythia_DIGI-RECO/230225_224255/0000/digiToReco_GluGluHtoTauTau_54.root'
#inputFiles_='file:/eos/uscms/store/group/lpcml/bbbam/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/DYToTauTau_M-50_13TeV-powheg_pythia8_DIGI-RECO/230228_103050/0000/digiToReco_GluGluHtoTauTau_221.root'#DY To TauTau
# inputFiles_='file/eos/user/b/bhbam/CMSSW_10_6_20/src/data_Run2018D_Tau_AOD_12Nov2019_UL2018_v1_00000_01173695_E460_C84F_9261_3A7EDF30E7AC.root'
# inputFiles_='file:/uscms/home/bbbam/nobackup/analysis/data_without_siLayer_full_hcal/CMSSW_10_6_20/src/MLAnalyzer/data_Run2018B_Tau_AOD_15Feb2022_UL2018_v1_2820000_0C6EC09F_736E_B640_AD5A_E99536E72323.root'
# inputFiles_='file:/uscms/home/bbbam/nobackup/analysis/MCGeneration/CMSSW_10_6_20/src/MCProduction_with_trigger/AODSIM_HToAATo4Tau.root'
inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/signal_withTrigger/GEN_PreMix_HToAATo4Tau_M_3p7_pythia8_2018UL/sim_HToAATo4Tau_M_3p7/240407_130328/0000/AODSIM_HToAATo4Tau_99.root'
# maxEvents_=100
maxEvents_=-1
skipEvents_=0#
#outputFile_='qcd.root'
#outputFile_='ttbar.root'
outputFile_='trigger_test_H_AA_4Tau_signal.root'


cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d outputFile=%s"%(cfg,inputFiles_,maxEvents_,skipEvents_,outputFile_)
print '%s'%cmd
os.system(cmd)
