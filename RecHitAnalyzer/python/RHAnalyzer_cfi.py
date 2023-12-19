

import FWCore.ParameterSet.Config as cms

from RecoMET.METProducers.METSignificanceParams_cfi import METSignificanceParams

fevt = cms.EDAnalyzer('RecHitAnalyzer'
    #, tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
    #, EBRecHitCollection             = cms.InputTag('ecalRecHit:EcalRecHitsEB')
    , reducedEBRecHitCollection      = cms.InputTag('reducedEcalRecHitsEB')
    #, EERecHitCollection             = cms.InputTag('ecalRecHit:EcalRecHitsEE')
    , reducedEERecHitCollection      = cms.InputTag('reducedEcalRecHitsEE')
    #, EBDigiCollection               = cms.InputTag('simEcalDigis:ebDigis')
    #, selectedEBDigiCollection       = cms.InputTag('selectDigi:selectedEcalEBDigiCollection')
    # , reducedHBHERecHitCollection    = cms.InputTag('hbhereco') # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Not present in Data
    , reducedHBHERecHitCollection    = cms.InputTag('reducedHcalRecHits:hbhereco')
    , genParticleCollection          = cms.InputTag('genParticles')
    , gedPhotonCollection            = cms.InputTag('gedPhotons')
    , ak4PFJetCollection             = cms.InputTag('ak4PFJets')
    , genJetCollection               = cms.InputTag('ak4GenJets')
    , trackRecHitCollection          = cms.InputTag('generalTracks')
    , trackCollection                = cms.InputTag("generalTracks")
    , transTrackBuilder              = cms.ESInputTag("TransientTrackBuilder")
    , vertexCollection               = cms.InputTag("offlinePrimaryVertices")
    #, siPixelRecHitCollection        = cms.InputTag("siPixelRecHits") # >>>>>>>>>>>>>>>>>>>>>>>>>not present in data
    # , siPixelRecHitCollection        = cms.InputTag("ctppsPixelRecHits") # >>>>>>>>>>>>>>>>>>>>>>>>>not present in data
    #, siStripMatchedRecHitCollection = cms.InputTag("siStripMatchedRecHits", "matchedRecHit")# >>>>>>>>>>>>>>>>>>>>>>>>>not present in data
    #, siStripRphiRecHits             = cms.InputTag("siStripMatchedRecHits", "rphiRecHit")# >>>>>>>>>>>>>>>>>>>>>>>>>not present in data
    #, siStripStereoRecHits           = cms.InputTag("siStripMatchedRecHits", "stereoRecHit")# >>>>>>>>>>>>>>>>>>>>>>>>>not present in data
    , secVertexCollection            = cms.InputTag("inclusiveCandidateSecondaryVertices")
    , pfCollection                   = cms.InputTag("particleFlow")
    , srcPFCandidates                = cms.InputTag("particleFlow")
    , recoJetsForBTagging            = cms.InputTag("ak4PFJetsCHS")
    , jetTagCollection               = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags")
    , srcPfJets                      = cms.InputTag("ak4PFJets")
    , metCollection                  = cms.InputTag("pfMet")
    , eleCollection                  = cms.InputTag("gedGsfElectrons")
    , tauCollection                  = cms.InputTag("hpsPFTauProducer")
    #, tauMVAIsolationLoose           = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT")
    , tauMVAIsolationLoose           = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT")
    , tauMVAIsolationTight           = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT")
    #, tauMVAIsolationRaw             = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw")
    , tauMVAIsolationRaw             = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw")
    , tauMuonRejectionLoose          = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection3")
    , tauElectronRejectionMVA6Loose  = cms.InputTag("hpsPFTauDiscriminationByMVA6LooseElectronRejection")
    , tauElectronRejectionMVA6VLoose = cms.InputTag("hpsPFTauDiscriminationByMVA6VLooseElectronRejection")
    #, tauDecayMode                   = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
    , tauDecayMode                   = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingOldDMs")
    , triggerResultsTag              = cms.InputTag("TriggerResults", "", "HLT")
    , ipTagInfoCollection            = cms.InputTag("pfImpactParameterTagInfos")
    , mode                           = cms.string("JetLevel")
    , rhoLabel                       = cms.InputTag('fixedGridRhoAll')
    , srcJetSF                       = cms.string('AK4PFchs')
    , srcJetResPt                    = cms.string('AK4PFchs_pt')
    , srcJetResPhi                   = cms.string('AK4PFchs_phi')
    #, srcLeptons                     = cms.VInputTag("slimmedElectrons","slimmedMuons","slimmedPhotons"),
    , srcLeptons                     = cms.VInputTag("gedGsfElectrons","muons","gedPhotons")

    # Jet level cfg
    # , isDebug                        = cms.bool(True)
    , isDebug                        = cms.bool(False)
    # , task                           = cms.string("tau_classification")
    #, task                           = cms.string("jet_ele_classification")
    , task                           = cms.string("dijet_ditau")
    , isSignal                       = cms.bool(False)
    , isW                            = cms.bool(False)
    , isBoostedTop                   = cms.bool(False)
    , nJets     = cms.int32(-1)
    , minJetPt  = cms.double(15.)
    , maxJetEta = cms.double(2.4)
    , z0PVCut   = cms.double(0.1)

    # MET parameter
    , parameters = METSignificanceParams

    #granularity multiplier wrt ECAL maps for tracker and tracking RH images
    , granularityMultiPhi = cms.int32(5)
    , granularityMultiEta = cms.int32(5)
    )
