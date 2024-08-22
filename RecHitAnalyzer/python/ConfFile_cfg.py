
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing('analysis')
options.register('skipEvents', 
    default=0, 
    mult=VarParsing.VarParsing.multiplicity.singleton,
    mytype=VarParsing.VarParsing.varType.int,
    info = "skipEvents")
# TODO: put this option in cmsRun scripts
options.register('processMode', 
    default='JetLevel', 
    #default='EventLevel', 
    mult=VarParsing.VarParsing.multiplicity.singleton,
    mytype=VarParsing.VarParsing.varType.string,
    info = "process mode: JetLevel or EventLevel")
options.parseArguments()

process = cms.Process("FEVTAnalyzer")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitConverter_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('106X_upgrade2018_realistic_v11_L1v1')
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

process.TrackRefitter.TTRHBuilder = 'WithAngleAndTemplate'

process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(options.maxEvents) 
    )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      options.inputFiles
      )
    , skipEvents = cms.untracked.uint32(options.skipEvents)
    )
print (" >> Loaded",len(options.inputFiles),"input files from list.")

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.load("MLAnalyzer.RecHitAnalyzer.RHAnalyzer_cfi")
process.fevt.mode = cms.string(options.processMode)
print (" >> Processing as:",(process.fevt.mode))

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
    )

############################
# Event Analysis
############################
process.load('MLAnalyzer.RecHitAnalyzer.hltanalysis_cfi')
process.load('MLAnalyzer.RecHitAnalyzer.hltobject_cfi')
#process.load('MLAnalyzer.RecHitAnalyzer.l1object_cfi')

from MLAnalyzer.RecHitAnalyzer.hltobject_cfi import trigger_list_data
process.hltobject.triggerNames = trigger_list_data

process.hltFilter = cms.EDFilter("HLTHighLevel",
                                          eventSetupPathsKey = cms.string(''),
                                          TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                          #HLTPaths = cms.vstring('HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v*','HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v*','HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v*'),
					  HLTPaths = cms.vstring('HLT_DiPFJetAve*','HLT_AK8PFJet*'),
					  #HLTPaths = cms.vstring('HLT_Double*PFTau*'),
                                          #HLTPaths = cms.vstring('*'),
                                          andOr = cms.bool(True),
                                          throw = cms.bool(False)
                                          )

#process.SimpleMemoryCheck = cms.Service( "SimpleMemoryCheck", ignoreTotal = cms.untracked.int32(1) )

process.p = cms.Path(
  process.siStripMatchedRecHits*process.siPixelRecHits*process.MeasurementTrackerEvent*process.TrackRefitter*
#  process.hltFilter*
#  process.patDefaultSequence*
  process.hltanalysis*
  process.fevt
)
