// -*- C++ -*-
//
// Package:    MLAnalyzer/RecHitAnalyzer
// Class:      RecHitAnalyzer
//
//
// Original Author:  Michael Andrews
//         Created:  Sat, 14 Jan 2017 17:45:54 GMT
//
//

#include "MLAnalyzer/RecHitAnalyzer/interface/RecHitAnalyzer.h"

//
// constructors and destructor
//

float Jet_pt_all_;
float Jet_m_all_;
float Jet_E_all_;
float Jet_eta_all_;

float Tau_pt_all_;
float Tau_E_all_;
float Tau_eta_all_;

float Jet_pt_passtrig_;
float Jet_m_passtrig_;
float Jet_E_passtrig_;
float Jet_eta_passtrig_;

float Tau_pt_passtrig_;
float Tau_E_passtrig_;
float Tau_eta_passtrig_;

bool matchPattern(const std::string& trigger, const std::string& pattern) {
    size_t pos = pattern.find("*");
    if (pos == std::string::npos) {
        return trigger == pattern; // Exact match if no wildcard
    } else {
        std::string prefix = pattern.substr(0, pos);
        std::string suffix = pattern.substr(pos + 1);
        return trigger.size() >= prefix.size() + suffix.size() &&
               trigger.substr(0, prefix.size()) == prefix &&
               trigger.substr(trigger.size() - suffix.size()) == suffix;
    }
}

RecHitAnalyzer::RecHitAnalyzer(const edm::ParameterSet& iConfig)
{
  //EBRecHitCollectionT_    = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("EBRecHitCollection"));
  EBRecHitCollectionT_    = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("reducedEBRecHitCollection"));
  //EBDigiCollectionT_      = consumes<EBDigiCollection>(iConfig.getParameter<edm::InputTag>("selectedEBDigiCollection"));
  //EBDigiCollectionT_      = consumes<EBDigiCollection>(iConfig.getParameter<edm::InputTag>("EBDigiCollection"));
  EERecHitCollectionT_    = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("reducedEERecHitCollection"));
  //EERecHitCollectionT_    = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("EERecHitCollection"));
  HBHERecHitCollectionT_  = consumes<HBHERecHitCollection>(iConfig.getParameter<edm::InputTag>("reducedHBHERecHitCollection"));
  TRKRecHitCollectionT_   = consumes<TrackingRecHitCollection>(iConfig.getParameter<edm::InputTag>("trackRecHitCollection"));

  genParticleCollectionT_ = consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("genParticleCollection"));
  photonCollectionT_      = consumes<reco::PhotonCollection>(iConfig.getParameter<edm::InputTag>("gedPhotonCollection"));
  jetCollectionT_         = consumes<reco::PFJetCollection>(iConfig.getParameter<edm::InputTag>("ak4PFJetCollection"));
  pfjetsToken_            = consumes<edm::View<reco::Jet> >(iConfig.getParameter<edm::InputTag>("srcPfJets"));
  genJetCollectionT_      = consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("genJetCollection"));
  trackCollectionT_       = consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("trackCollection"));
  transientTrackBuilderT_ = iConfig.getParameter<edm::ESInputTag>("transTrackBuilder");
  pfCollectionT_          = consumes<PFCollection>(iConfig.getParameter<edm::InputTag>("pfCollection"));

  pfCandidatesToken_      = consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("srcPFCandidates"));

  vertexCollectionT_      = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertexCollection"));
  secVertexCollectionT_   = consumes<reco::VertexCompositePtrCandidateCollection>(iConfig.getParameter<edm::InputTag>("secVertexCollection"));

  recoJetsT_              = consumes<edm::View<reco::Jet> >(iConfig.getParameter<edm::InputTag>("recoJetsForBTagging"));
  jetTagCollectionT_      = consumes<reco::JetTagCollection>(iConfig.getParameter<edm::InputTag>("jetTagCollection"));
  ipTagInfoCollectionT_   = consumes<std::vector<reco::CandIPTagInfo> > (iConfig.getParameter<edm::InputTag>("ipTagInfoCollection"));

  //siPixelRecHitCollectionT_ = consumes<SiPixelRecHitCollection>(iConfig.getParameter<edm::InputTag>("siPixelRecHitCollection"));
  //siStripRecHitCollectionT_ = iConfig.getParameter<std::vector<edm::InputTag> >("siStripRecHitCollection");
  //siStripMatchedRecHitCollectionT_ = consumes<SiStripMatchedRecHit2DCollection>(iConfig.getParameter<edm::InputTag>("siStripMatchedRecHitCollection"));
  //siStripRPhiRecHitCollectionT_    = consumes<SiStripRecHit2DCollection>(iConfig.getParameter<edm::InputTag>("siStripRphiRecHits"));
  //siStripStereoRecHitCollectionT_  = consumes<SiStripRecHit2DCollection>(iConfig.getParameter<edm::InputTag>("siStripStereoRecHits"));

  metCollectionT_           = consumes<reco::PFMETCollection>(iConfig.getParameter<edm::InputTag>("metCollection"));

  tauCollectionT_           = consumes<reco::PFTauCollection>(iConfig.getParameter<edm::InputTag>("tauCollection"));
  tauDecayMode_             = consumes<reco::PFTauDiscriminator>(iConfig.getParameter<edm::InputTag>("tauDecayMode"));
  tauMVAIsolation_          = consumes<reco::PFTauDiscriminator>(iConfig.getParameter<edm::InputTag>("tauMVAIsolationRaw"));
  tauMuonRejection_         = consumes<reco::PFTauDiscriminator>(iConfig.getParameter<edm::InputTag>("tauMuonRejectionLoose"));
  tauElectronRejectionMVA6_ = consumes<reco::PFTauDiscriminator>(iConfig.getParameter<edm::InputTag>("tauElectronRejectionMVA6VLoose"));

  eleCollectionT_           = consumes<reco::GsfElectronCollection>(iConfig.getParameter<edm::InputTag>("eleCollection"));

  processName_              = iConfig.getUntrackedParameter<std::string>("processName","HLT");
  //triggerResultsToken_      = consumes<edm::TriggerResults> (iConfig.getUntrackedParameter<edm::InputTag>("triggerResultsTag", edm::InputTag("TriggerResults", "", "HLT")));
  triggerResultsToken_      = consumes<edm::TriggerResults> (iConfig.getParameter<edm::InputTag>("triggerResultsTag"));

  jetSFType_                = iConfig.getParameter<std::string>("srcJetSF");
  jetResPtType_             = iConfig.getParameter<std::string>("srcJetResPt");
  jetResPhiType_            = iConfig.getParameter<std::string>("srcJetResPhi");
  rhoLabel_                 = consumes<double>(iConfig.getParameter<edm::InputTag>("rhoLabel"));

  std::vector<edm::InputTag> srcLeptonsTags        = iConfig.getParameter< std::vector<edm::InputTag> >("srcLeptons");
  for(std::vector<edm::InputTag>::const_iterator it=srcLeptonsTags.begin();it!=srcLeptonsTags.end();it++) {
    lepTokens_.push_back( consumes<edm::View<reco::Candidate> >( *it ) );
  }

  metSigAlgo_               = new metsig::METSignificance(iConfig);

  //johnda add configuration
  //debug      = iConfig.getParameter<bool>("isDebug");
  mode_      = iConfig.getParameter<std::string>("mode");
  task_      = iConfig.getParameter<std::string>("task");
  isSignal_  = iConfig.getParameter<bool>("isSignal");
  isW_       = iConfig.getParameter<bool>("isW");
  isBoostedTop_   = iConfig.getParameter<bool>("isBoostedTop");
  minJetPt_  = iConfig.getParameter<double>("minJetPt");
  maxJetEta_ = iConfig.getParameter<double>("maxJetEta");
  z0PVCut_   = iConfig.getParameter<double>("z0PVCut");




  std::cout << " >> Mode set to " << mode_ << std::endl;
  if ( mode_ == "JetLevel" ) {
    doJets_ = true;
    nJets_ = iConfig.getParameter<int>("nJets");
    std::cout << "\t>> nJets set to " << nJets_ << std::endl;
  } else if ( mode_ == "EventLevel" ) {
    doJets_ = false;
  } else {
    std::cout << " >> Assuming EventLevel Config. " << std::endl;
    doJets_ = false;
  }



  // Initialize file writer
  // NOTE: initializing dynamic-memory histograms outside of TFileService
  // will cause memory leaks
  usesResource("TFileService");
  edm::Service<TFileService> fs;
  h_sel = fs->make<TH1F>("h_sel", "isSelected;isSelected;Events", 2, 0., 2.);

  h_passreftrig = fs->make<TH1F>("h_passreftrig" , "; passed ref trigger" , 2 , 0. , 2. );
  h_met_all = fs->make<TH1F>("h_met_all" , "; E_{T}^{miss} [GeV]" , 40, 100., 500. );
  h_met_passtrig = fs->make<TH1F>("h_met_passtrig" , "; E_{T}^{miss} [GeV]" , 40, 100., 500. );


  h_tau_att_jet_E_all          = fs->make<TH1D>("h_jet_E_all"        , "E;E;Jets"                                       ,  50,  0., 500.);
  h_tau_att_jet_pT_all         = fs->make<TH1D>("h_jet_pT_all"       , "p_{T};p_{T};Jets"                               ,  30,  0., 300.);
  h_tau_att_jet_eta_all        = fs->make<TH1D>("h_jet_eta_all"      , "#eta;#eta;Jets"                                 ,  30, -3.,   3.);
  h_tau_att_jet_m0_all         = fs->make<TH1D>("h_jet_m0_all"       , "m_{jet};m_{jet};Jets"                           ,  50,  0.,  100.);
  h_tau_att_tau_pT_all         = fs->make<TH1D>("h_tau_pT_all"       , "p_{T}^{#tau};p_{T}^{#tau};Jets"                 ,  40,  0., 200.);
  h_tau_att_tau_E_all         = fs->make<TH1D>("h_tau_E_all"       , "E^{#tau};E^{#tau};Jets"                 ,  50,  0., 500.);
  h_tau_att_tau_eta_all         = fs->make<TH1D>("h_tau_eta_all"       , "eta^{#tau};eta^{#tau};Jets"                 ,  30, -3.,   3.);


  h_tau_att_jet_E_passtrig          = fs->make<TH1D>("h_jet_E_passtrig"        , "E;E;Jets"                                       ,  50,  0., 500.);
  h_tau_att_jet_pT_passtrig         = fs->make<TH1D>("h_jet_pT_passtrig"       , "p_{T};p_{T};Jets"                               ,  30,  0., 300.);
  h_tau_att_jet_eta_passtrig        = fs->make<TH1D>("h_jet_eta_passtrig"      , "#eta;#eta;Jets"                                 ,  30, -3.,   3.);
  h_tau_att_jet_m0_passtrig         = fs->make<TH1D>("h_jet_m0_passtrig"       , "m_{jet};m_{jet};Jets"                           ,  50,  0.,  100.);
  h_tau_att_tau_pT_passtrig         = fs->make<TH1D>("h_tau_pT_passtrig"       , "p_{T}^{#tau};p_{T}^{#tau};Jets"                 ,  40,  0., 200.);
  h_tau_att_tau_E_passtrig         = fs->make<TH1D>("h_tau_E_passtrig"       , "E^{#tau};E^{#tau};Jets"                 ,  50,  0., 500.);
  h_tau_att_tau_eta_passtrig         = fs->make<TH1D>("h_tau_eta_passtrig"       , "eta^{#tau};eta^{#tau};Jets"                 ,  30, -3.,   3.);


  //////////// TTree //////////

  // These will be use to create the actual images
  RHTree = fs->make<TTree>("RHTree", "RecHit tree");

  // branchesEB           ( RHTree, fs );
   RHTree->Branch("jet_pt_all",  &Jet_pt_all_);
   RHTree->Branch("jet_pt_passtrig",  &Jet_pt_passtrig_);
   RHTree->Branch("jet_eta_all",  &Jet_eta_all_);
   RHTree->Branch("jet_eta_passtrig",  &Jet_eta_passtrig_);
   RHTree->Branch("jet_m_all",  &Jet_m_all_);
   RHTree->Branch("jet_m_passtrig",  &Jet_m_passtrig_);
   RHTree->Branch("jet_E_all",  &Jet_E_all_);
   RHTree->Branch("jet_E_passtrig",  &Jet_E_passtrig_);
   RHTree->Branch("tau_pt_all",  &Tau_pt_all_);
   RHTree->Branch("tau_pt_passtrig",  &Tau_pt_passtrig_);
   RHTree->Branch("tau_eta_all",  &Tau_eta_all_);
   RHTree->Branch("tau_eta_passtrig",  &Tau_eta_passtrig_);
   RHTree->Branch("tau_E_all",  &Tau_E_all_);
   RHTree->Branch("tau_E_passtrig",  &Tau_E_passtrig_);

} // constructor
//
RecHitAnalyzer::~RecHitAnalyzer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  delete metSigAlgo_;  //FIXME
}
//
// member functions
//
// ------------ method called for each event  ------------
void
RecHitAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

nTotal++;
using namespace edm;
// ----- Apply event selection cuts ----- //

edm::Handle<edm::TriggerResults> hltresults;
iEvent.getByToken(triggerResultsToken_,hltresults);



edm::Handle<reco::PFJetCollection> jets;
iEvent.getByToken(jetCollectionT_, jets);


edm::Handle<reco::PFTauCollection> taus;
iEvent.getByToken(tauCollectionT_, taus);

edm::Handle<reco::PFMETCollection> pfmet;
iEvent.getByToken(metCollectionT_, pfmet);



float tau_sel_pT          = 10;
bool triger_valid = true;




std::vector<std::string> patterns = {
     "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v*",
     "HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v*",
     "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v*"
   };

if (!hltresults.isValid()) {
   std::cout << "!!! Error in getting TriggerResults product from Event !!!" << std::endl;
   triger_valid = false;
 }

 int ntrigs = hltresults->size();
 edm::TriggerNames const& triggerNames = iEvent.triggerNames(*hltresults);
 int passTrigger = 0;
 for (int itrig = 0; itrig != ntrigs; ++itrig)
 {
   std::string trigName = triggerNames.triggerName(itrig);
   // std::cout << ">>>>>>>>>>>>>>>>Available Trigger: " << trigName << std::endl;
   bool accept = hltresults->accept(itrig);
   if (!(accept)) continue;
   // std::cout << " Accept >>>>>>>>>>>>>>>>>>>>" << trigName << std::endl;


    for (const std::string& pattern : patterns) {
      // std::cout << "Trying to Match Trigger: " << pattern << std::endl;

     if (matchPattern(trigName, pattern)) {
         std::cout << ">>>>>>>>>>>>>>>>Matched Trigger:-------- " << trigName << std::endl;

         passTrigger = passTrigger+1;

          }
         }



   }

 std::cout << " >>number of trigger passed >>>>>>>>>>>>>>>>>" << passTrigger << std::endl;

float Jet_pt=-9999.9999;
float Jet_m=-9999.9999;
float Jet_E=-9999.9999;
float Jet_eta= -9999.9999;

float Tau_pt=-9999.9999;
float Tau_E=-9999.9999;
float Tau_eta= -9999.9999;

Jet_pt_all_= -9999.9999;
Jet_m_all_= -9999.9999;
Jet_E_all_= -9999.9999;
Jet_eta_all_= -9999.9999;

Tau_pt_all_= -9999.9999;
Tau_E_all_= -9999.9999;
Tau_eta_all_= -9999.9999;

Jet_pt_passtrig_= -9999.9999;
Jet_m_passtrig_= -9999.9999;
Jet_E_passtrig_= -9999.9999;
Jet_eta_passtrig_= -9999.9999;

Tau_pt_passtrig_= -9999.9999;
Tau_E_passtrig_= -9999.9999;
Tau_eta_passtrig_= -9999.9999;

if (triger_valid)
{




for ( unsigned iJ(0); iJ != jets->size(); ++iJ )
{
    reco::PFJetRef iJet( jets, iJ );
    if ( std::abs(iJet->pt())  < minJetPt_ ) continue;
    if ( std::abs(iJet->eta()) > maxJetEta_ ) continue;
    if (Jet_pt < iJet->pt())
    {
      Jet_pt = iJet->pt();
      Jet_E = iJet->energy();
      Jet_m = iJet->mass();
      Jet_eta = iJet->eta();
    }
// std::cout << " >>Jet_pt_all >>>>>>>>>>>>>>>>>>>>>>" << iJet->pt() << std::endl;

} // jet loop
Jet_pt_all_ = Jet_pt;
Jet_eta_all_ = Jet_eta;
Jet_E_all_ = Jet_E;
Jet_m_all_ = Jet_m;

for ( unsigned iT(0); iT != taus->size(); ++iT )
{
      reco::PFTauRef iTau( taus, iT );
      if ( iTau->pt() < tau_sel_pT ) continue;
      if (Tau_pt < iTau->pt())
    {
      Tau_pt = iTau->pt();
      Tau_E = iTau->energy();
      Tau_eta = iTau->eta();
    }
}// tau loop
Tau_pt_all_ = Tau_pt;
Tau_eta_all_ = Tau_eta;
Tau_E_all_ = Tau_E;
h_passreftrig->Fill(1);
float met = ( pfmet->front() ).pt();;

h_met_all->Fill(met);
h_tau_att_jet_pT_all->Fill(Jet_pt);
h_tau_att_jet_E_all->Fill(Jet_E);
h_tau_att_jet_eta_all->Fill(Jet_eta);
h_tau_att_jet_m0_all->Fill(Jet_m);
h_tau_att_tau_pT_all->Fill(Tau_pt);
h_tau_att_tau_E_all->Fill(Tau_E);
h_tau_att_tau_eta_all->Fill(Tau_eta);

if (passTrigger > 0){
  h_met_passtrig->Fill(met);
  h_tau_att_jet_pT_passtrig->Fill(Jet_pt);
  h_tau_att_jet_E_passtrig->Fill(Jet_E);
  h_tau_att_jet_eta_passtrig->Fill(Jet_eta);
  h_tau_att_jet_m0_passtrig->Fill(Jet_m);
  h_tau_att_tau_pT_passtrig->Fill(Tau_pt);
  h_tau_att_tau_E_passtrig->Fill(Tau_E);
  h_tau_att_tau_eta_passtrig->Fill(Tau_eta);


  Jet_pt_passtrig_ = Jet_pt;
  Jet_eta_passtrig_ = Jet_eta;
  Jet_E_passtrig_ = Jet_E;
  Jet_m_passtrig_ = Jet_m;
  Tau_pt_passtrig_ = Tau_pt;
  Tau_eta_passtrig_ = Tau_eta;
  Tau_E_passtrig_ = Tau_E;
 }
// std::cout << " >>Jet_pt_all_ >>>>>>>>>>>>>>>>>>>>>>" << Jet_pt_all_ << std::endl;
// std::cout << " >>Jet_pt_passtrig_ >>>>>>>>>>>>>>>>>" << Jet_pt_passtrig_ << std::endl;
 RHTree->Fill();
 nPassed++;
} // triger_valid

  h_sel->Fill( 1. );


} // analyze()


// ------------ method called once each job just before starting event loop  ------------
void
RecHitAnalyzer::beginJob()
{
  nTotal = 0;
  nPassed = 0;
}

// ------------ method called once each job just after ending the event loop  ------------
void
RecHitAnalyzer::endJob()
{
  std::cout << " selected: " << nPassed << "/" << nTotal << std::endl;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
RecHitAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

const reco::PFCandidate*
RecHitAnalyzer::getPFCand(edm::Handle<PFCollection> pfCands, float eta, float phi, float& minDr, bool debug ) {

  minDr = 10;
  const reco::PFCandidate* minDRCand = nullptr;

  for ( PFCollection::const_iterator iPFC = pfCands->begin();
        iPFC != pfCands->end(); ++iPFC ) {

    const reco::Track* thisTrk = iPFC->bestTrack();
    if ( !thisTrk ) continue;

    float thisdR = reco::deltaR( eta, phi, thisTrk->eta(), thisTrk->phi() );
    if (debug) std::cout << "\tthisdR: " << thisdR << " " << thisTrk->pt() << " " << iPFC->particleId() << std::endl;

    const reco::PFCandidate& thisPFCand = (*iPFC);

    if ( (thisdR < 0.01) && (thisdR <minDr) ) {
      minDr    = thisdR;
      minDRCand = &thisPFCand;
    }
  }

  return minDRCand;
}

const reco::Track*
RecHitAnalyzer::getTrackCand(edm::Handle<reco::TrackCollection> trackCands, float eta, float phi, float& minDr, bool debug ) {

  minDr = 10;
  const reco::Track* minDRCand = nullptr;
  reco::Track::TrackQuality tkQt_ = reco::Track::qualityByName("highPurity");

  for ( reco::TrackCollection::const_iterator iTk = trackCands->begin();
        iTk != trackCands->end(); ++iTk ) {
    if ( !(iTk->quality(tkQt_)) ) continue;

    float thisdR = reco::deltaR( eta, phi, iTk->eta(),iTk->phi() );
    if (debug) std::cout << "\tthisdR: " << thisdR << " " << iTk->pt() << std::endl;

    const reco::Track& thisTrackCand = (*iTk);

    if ( (thisdR < 0.01) && (thisdR <minDr) ) {
      minDr    = thisdR;
      minDRCand = &thisTrackCand;
    }
  }

  return minDRCand;
}




int RecHitAnalyzer::getTruthLabel(const reco::PFJetRef& recJet, edm::Handle<reco::GenParticleCollection> genParticles, float dRMatch , bool debug ){
  if ( debug ) {
    std::cout << " Mathcing reco jetPt:" << recJet->pt() << " jetEta:" << recJet->eta() << " jetPhi:" << recJet->phi() << std::endl;
  }

  for (reco::GenParticleCollection::const_iterator iGen = genParticles->begin();
       iGen != genParticles->end();
       ++iGen) {

    // Do not want to match to the final particles in the shower
    if ( iGen->status() > 99 ) continue;

    // Only want to match to partons/leptons/bosons
    if ( iGen->pdgId() > 25 ) continue;

    float dR = reco::deltaR( recJet->eta(),recJet->phi(), iGen->eta(),iGen->phi() );

    if ( debug ) std::cout << " \t >> dR " << dR << " id:" << iGen->pdgId() << " status:" << iGen->status() << " nDaught:" << iGen->numberOfDaughters() << " pt:"<< iGen->pt() << " eta:" <<iGen->eta() << " phi:" <<iGen->phi() << " nMoms:" <<iGen->numberOfMothers()<< std::endl;

    if ( dR > dRMatch ) continue;
    if ( debug ) std::cout << " Matched pdgID " << iGen->pdgId() << std::endl;

    return iGen->pdgId();

  } // gen particles

  return -99;
}


float RecHitAnalyzer::getBTaggingValue(const reco::PFJetRef& recJet, edm::Handle<edm::View<reco::Jet> >& recoJetCollection, edm::Handle<reco::JetTagCollection>& btagCollection, float dRMatch, bool debug ){

  // loop over jets
  for( edm::View<reco::Jet>::const_iterator jetToMatch = recoJetCollection->begin(); jetToMatch != recoJetCollection->end(); ++jetToMatch )
    {
      reco::Jet thisJet = *jetToMatch;
      float dR = reco::deltaR( recJet->eta(),recJet->phi(), thisJet.eta(),thisJet.phi() );
      if(dR > 0.1) continue;

      size_t idx = (jetToMatch - recoJetCollection->begin());
      edm::RefToBase<reco::Jet> jetRef = recoJetCollection->refAt(idx);

      if(debug) std::cout << "btag discriminator value = " << (*btagCollection)[jetRef] << std::endl;
      return (*btagCollection)[jetRef];

    }

  if(debug){
    std::cout << "ERROR  No btag match: " << std::endl;

    // loop over jets
    for( edm::View<reco::Jet>::const_iterator jetToMatch = recoJetCollection->begin(); jetToMatch != recoJetCollection->end(); ++jetToMatch )
      {
	const reco::Jet thisJet = *jetToMatch;
	std::cout << "\t Match attempt pt: " <<  thisJet.pt() << " vs " <<  recJet->pt()
		  << " eta: " << thisJet.eta() << " vs " << recJet->eta()
		  << "phi: "<< thisJet.phi() << " vs " << recJet->phi()
		  << std::endl;
	float dR = reco::deltaR( recJet->eta(),recJet->phi(), thisJet.eta(),thisJet.phi() );
	std::cout << "dR " << dR << std::endl;
      }
  }

  return -99;
}


Measurement1D RecHitAnalyzer::vertexDxy(const reco::VertexCompositePtrCandidate &svcand, const reco::Vertex &pv)  {
  VertexDistanceXY dist;
  reco::Vertex::CovarianceMatrix csv; svcand.fillVertexCovariance(csv);
  reco::Vertex svtx(svcand.vertex(), csv);
  return dist.distance(svtx, pv);
}

Measurement1D RecHitAnalyzer::vertexD3d(const reco::VertexCompositePtrCandidate &svcand, const reco::Vertex &pv)  {
  VertexDistance3D dist;
  reco::Vertex::CovarianceMatrix csv; svcand.fillVertexCovariance(csv);
  reco::Vertex svtx(svcand.vertex(), csv);
  return dist.distance(svtx, pv);
}

float RecHitAnalyzer::vertexDdotP(const reco::VertexCompositePtrCandidate &sv, const reco::Vertex &pv)  {
  reco::Candidate::Vector p = sv.momentum();
  reco::Candidate::Vector d(sv.vx() - pv.x(), sv.vy() - pv.y(), sv.vz() - pv.z());
  return p.Unit().Dot(d.Unit());
}

//define this as a plug-in
DEFINE_FWK_MODULE(RecHitAnalyzer);
