#include "MLAnalyzer/RecHitAnalyzer/interface/SCRegressor.h"

// Initialize branches _____________________________________________________//
void SCRegressor::branchesDiPhotonSel ( TTree* tree, edm::Service<TFileService> &fs )
{
  tree->Branch("m0",        &m0_);
  tree->Branch("FC_inputs", &vFC_inputs_);
}

struct pho_obj {
  unsigned int idx;
  double pt;
};

// Run event selection ___________________________________________________________________//
bool SCRegressor::runDiPhotonSel ( const edm::Event& iEvent, const edm::EventSetup& iSetup ) {

  edm::Handle<reco::PhotonCollection> photons;
  iEvent.getByToken(photonCollectionT_, photons);

  ////////// Apply selection //////////

  // Ensure two reco photons 
  if ( debug ) std::cout << " Pho collection size:" << photons->size() << std::endl;
  //std::vector<int> vPhoIdxs;
  //math::PtEtaPhiELorentzVectorD vDiPho;
  std::vector<pho_obj> vPhos;
  for ( unsigned int iP = 0; iP < photons->size(); iP++ ) {

    reco::PhotonRef iPho( photons, iP );

    if ( std::abs(iPho->pt()) < 18. ) continue;
    if ( std::abs(iPho->eta()) > 1.44 ) continue;
    if ( iPho->full5x5_r9() < 0.5 ) continue;
    //if ( iPho->hadTowOverEm() > 0.07 ) continue;
    if ( iPho->full5x5_sigmaIetaIeta() > 0.0105 ) continue;
    //if ( iPho->hasPixelSeed() == true ) continue;
    if ( debug ) std::cout << " >> pT:" << iPho->pt() << " eta:" << iPho->eta() << " phi: " << iPho->phi() << " E:" << iPho->energy() << std::endl;

    //vDiPho += iPho->p4();
    //vPhoIdxs.push_back( iP );
    pho_obj Pho_obj = { iP, std::abs(iPho->pt()) };
    vPhos.push_back( Pho_obj );

  } // reco photons
  if ( debug ) std::cout << " Reco pho size:" << vPhos.size() << std::endl;
  if ( vPhos.size() < 2 ) return false;

  // Sort photons by pT, for abitrary N 
  std::sort( vPhos.begin(), vPhos.end(), [](auto const &a, auto const &b) { return a.pt > b.pt; } );
  for ( unsigned int iP = 0; iP < vPhos.size(); iP++ ) {
    reco::PhotonRef iPho( photons, vPhos[iP].idx );
    if ( debug ) std::cout << " >> pT:" << iPho->pt() << " eta:" << iPho->eta() << " phi: " << iPho->phi() << " E:" << iPho->energy() << std::endl;
  }
  // Check if any photon pairing passes invariant mass cut
  std::vector<int> vPhoIdxs;
  bool passedMassCut = false;
  for ( unsigned int j = 0; j < vPhos.size()-1; j++ ) {

    reco::PhotonRef jPho( photons, vPhos[j].idx );

    for ( unsigned int k = 1; k < vPhos.size(); k++ ) {

      if ( k <= j ) continue;
      reco::PhotonRef kPho( photons, vPhos[k].idx );
      ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > vDiPho = jPho->p4() + kPho->p4();
      if ( debug ) std::cout << " >> m0:" << vDiPho.mass() << std::endl;

      if ( vDiPho.mass() > 80. ) {
        vPhoIdxs.push_back( vPhos[j].idx );
        vPhoIdxs.push_back( vPhos[k].idx );
        m0_ = vDiPho.mass();
        passedMassCut = true;
        break;
      }

    } //k
    if ( passedMassCut ) break;
  } // j
  if ( !passedMassCut ) return false;
  if ( debug ) std::cout << " >> m0:" << m0_ << std::endl;

  // Apply diphoton pT cuts
  float ptCut[2]   = { 30., 18. };
  float ptOmCut[2] = {  3.,  4. };
  vPreselPhoIdxs_.clear();
  for ( unsigned int iP = 0; iP < vPhoIdxs.size(); iP++ ) {

    reco::PhotonRef iPho( photons, vPhoIdxs[iP] );

    if ( std::abs(iPho->pt()) < ptCut[iP] ) continue;
    if ( std::abs(iPho->pt()) < m0_/ptOmCut[iP] ) continue;
    if ( debug ) std::cout << " >> pT:" << iPho->pt() << " eta:" << iPho->eta() << " phi: " << iPho->phi() << " E:" << iPho->energy() << std::endl;

    vPreselPhoIdxs_.push_back( vPhoIdxs[iP] );

  } // vPhoIdxs
  if ( vPreselPhoIdxs_.size() != 2 ) return false;
  if ( debug ) std::cout << " Reco pho size:" << vPhos.size() << std::endl;

  if ( debug ) std::cout << " >> Passed selection. " << std::endl;
  return true;
}

// Fill branches ___________________________________________________________________//
void SCRegressor::fillDiPhotonSel ( const edm::Event& iEvent, const edm::EventSetup& iSetup )
{

  edm::Handle<reco::PhotonCollection> photons;
  iEvent.getByToken(photonCollectionT_, photons);

  // Fill kinematic variables
  float dphi[2] = { 0., 0. };
  vFC_inputs_.clear();
  for ( unsigned int iP = 0; iP < vRegressPhoIdxs_.size(); iP++ ) {
    reco::PhotonRef iPho( photons, vRegressPhoIdxs_[iP] );
    vFC_inputs_.push_back( iPho->pt()/m0_ );
    vFC_inputs_.push_back( iPho->eta() );
    dphi[iP] = iPho->phi();
  }
  vFC_inputs_.push_back( TMath::Cos(reco::deltaPhi(dphi[0], dphi[1])) );

}
