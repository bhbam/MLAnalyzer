import os

#cfg='RecHitAnalyzer/python/ConfFile_data_cfg.py'
cfg='RecHitAnalyzer/python/ConfFile_cfg.py'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO/230209_184732/0000/aToTauTau_digiToRecoStep_99.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/ddicroce/Run2018_GENtoAODSIM_unbiased/sim_HToTauTau_m3p6To15p2_pT30To180_ctau0To3_2018_unbiased_ext2/211125_222504/0000/SIM_HToTauTau_m3p6To15p2_pT30To180_ctau0To3_unbiased_997.root'
#inputFiles_='file:root://cmsxrootd.fnal.gov//store/mc/RunIISummer20UL18RECO/GluGluHToTauTau_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/2820000/00F87F4B-78ED-044E-9413-47D1BECD4A64.root'
# inputFiles_='file:/afs/cern.ch/user/b/bhbam/public/CMSSW_10_6_20/src/aToTauTau_digiToRecoStep.root'
# inputFiles_='file:/afs/cern.ch/user/b/bhbam/public/CMSSW_10_6_20/src/MCProduction/E2E-BoostedUpsilon/Upsilon1SToTauTau_digiToRecoStep.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO/230307_231105/0000/digiToReco_withPileup_91.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO/230307_231105/0000/digiToReco_withPileup_91.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/Upsilon1s_ToTauTau_Hadronic_tauDR0p4_eta0To2p4_pythia8_validationML/Upsilon1s_ToTauTau_Hadronic_tauDR0p4_pythia8_validationML_DIGI_RECO/230313_060801/0000/Upsilon1SToTauTau_digiToRecoStep_9.root'
# inputFiles_='file:/afs/cern.ch/user/b/bhbam/public/CMSSW_10_6_20/src/MCProduction/E2E-BoostedTau/aToTauTau_digiToReco_withPileup.root'
# inputFiles_='root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO/230307_231105/0000/digiToReco_withPileup_99.root'
# inputFiles_='root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO/230209_184732/0000/digiToRecoStep_withPU_38.root'
# inputFiles_='root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/Upsilon1s_ToTauTau_Hadronic_tauDR0p4_eta0To2p4_pythia8_validationML_dataset_1/Upsilon1s_ToTauTau_Hadronic_tauDR0p4_pythia8_validationML_DIGI_RECO_dataset_1/230411_173637/0000/Upsilon1SToTauTau_digiToRecoStep_989.root'
# inputFiles_='root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO/230209_184732/0000/digiToRecoStep_90.root'
# inputFiles_='root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/GluGluHToTauTau_Hadronic_M125_13TeV_powheg_pythia8/GluGluHToTauTau_Hadronic_M125_13TeV_powheg_pythia_DIGI-RECO/230225_224255/0000/digiToReco_GluGluHtoTauTau_997.root'
# inputFiles_='file:/afs/cern.ch/user/b/bhbam/public/CMSSW_10_6_20/src/MCProduction/E2E-BoostedTau/digiToReco_withPU.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pT30To180_ctau0To3_eta0To1p4_pythia8_unbiased4ML_dataset_1/aToTauTau_Hadronic_tauDR0p4_m3p6To16_pythia8_DIGI_RECO_dataset_1/230406_074210/0000/digiToReco_withPU_99.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/sim_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/230512_123635/0000/SIM_HToAAToTauTau_M10_2018UL_withPU_1.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/gen_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/sim_HToAATo4Tau_Hadronic_tauDR0p4_M10_ctau0To3_eta0To2p4_pythia8_2018UL/230512_123635/0000/SIM_HToAAToTauTau_M10_2018UL_withPU_90.root'
# inputFiles_='file:root://cmsxrootd.fnal.gov//store/group/lpcml/bbbam/MCGeneration/aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pythia8_DIGI_RECO_unphysical/sim_aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pythia8_DIGI_RECO_unphysical/231004_233237/0000/digiToReco_withPU_43.root'
inputFiles_='file:/uscms/home/bbbam/nobackup/analysis/MCGeneration/CMSSW_10_6_20/src/MCProduction/E2E-HToAATo4Tau/SIM_HToAAToTauTau_M10_2018UL_withPU.root'
# maxEvents_=20
maxEvents_=-1
skipEvents_=0#
#outputFile_='MLAnal_PhaseI_TTbar_13TeVu_trackRefitter.root'
#outputFile_='GJet.root'
#outputFile_='ttbar_qcdCode.root'
# outputFile_='aToTauTau_Hadronic_tauDR0p4_m3p6To14_pT30To180_ctau0To3_eta0To2p4_pythia8_ntuples.root'
# outputFile_='aToTauTau_Hadronic_tauDR0p4_m1p2To3p6_pT30To180_unphysical_ntuples.root'
#outputFile_='WJets_erroredPixelStripLayers.root'
#outputFile_='dyToEE.root'
#outputFile_='acd_EmEnriched.root'
outputFile_='Unboosted_HToAAToTauTau_signal_M8.root'

cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d outputFile=%s"%(cfg,inputFiles_,maxEvents_,skipEvents_,outputFile_)
print '%s'%cmd
os.system(cmd)
