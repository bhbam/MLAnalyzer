#ifndef SCRegressor_h
#define SCRegressor_h
// -*- C++ -*-
//
// Package:    MLAnalyzer/SCRegressor
// Class:      SCRegressor
//
//
// Original Author:  Michael Andrews
//         Created:  Mon, 17 Jul 2017 15:59:54 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
#include "DataFormats/EcalDetId/interface/EcalTrigTowerDetId.h"
#include "Geometry/CaloTopology/interface/EcalBarrelTopology.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h" // reco::PhotonCollection defined here
#include "DataFormats/PatCandidates/interface/Photon.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TTree.h"
#include "TStyle.h"
#include "TMath.h"
#include "TProfile2D.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "Calibration/IsolatedParticles/interface/DetIdFromEtaPhi.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

//
// class declaration
//
using pat::PhotonCollection;
using pat::PhotonRef;
//using reco::PhotonCollection;
//using reco::PhotonRef;

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class SCRegressor : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
  public:
    explicit SCRegressor(const edm::ParameterSet&);
    ~SCRegressor();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


  private:
    virtual void beginJob() override;
    virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;

    // ----------member data ---------------------------
    //edm::EDGetTokenT<edm::View<reco::GsfElectron>> electronCollectionT_;
    edm::EDGetTokenT<reco::GsfElectronCollection> electronCollectionT_;
    edm::EDGetTokenT<PhotonCollection> photonCollectionT_;
    edm::EDGetTokenT<EcalRecHitCollection> EBRecHitCollectionT_;
    edm::EDGetTokenT<EcalRecHitCollection> EERecHitCollectionT_;
    edm::EDGetTokenT<EcalRecHitCollection> ESRecHitCollectionT_;
    edm::EDGetTokenT<reco::GenParticleCollection> genParticleCollectionT_;
    edm::EDGetTokenT<reco::GenJetCollection> genJetCollectionT_;
    edm::EDGetTokenT<reco::TrackCollection> trackCollectionT_;
    edm::EDGetTokenT<double> rhoLabel_;

    static const int nPhotons = 2;
    //static const int nPhotons = 1;

    TProfile2D *hEB_energy;
    TProfile2D *hEB_time;
    std::vector<float> vEB_energy_;
    std::vector<float> vEB_time_;

    //TH1D * histo;
    TProfile2D * hSC_energy;
    TProfile2D * hSC_time;
    TH1F * hSC_mass;
    TH1F * hDR;
    TH1F * hdEta;
    TH1F * hdPhi;
    TH3F * hdPhidEta;
    TH1F * hSC_pT;

    TTree* RHTree;

    unsigned int nPho;
    unsigned long long eventId_;
    unsigned int runId_;
    unsigned int lumiId_;

    void branchesSC ( TTree*, edm::Service<TFileService>& );
    void branchesEB ( TTree*, edm::Service<TFileService>& );
    void branchesTracksAtEBEE ( TTree*, edm::Service<TFileService>& );
    void branchesPhoVars ( TTree*, edm::Service<TFileService>& );

    void fillSC     ( const edm::Event&, const edm::EventSetup& );
    void fillEB     ( const edm::Event&, const edm::EventSetup& );
    void fillTracksAtEBEE ( const edm::Event&, const edm::EventSetup& );
    void fillPhoVars ( const edm::Event&, const edm::EventSetup& );

    void branchesPiSel       ( TTree*, edm::Service<TFileService>& );
    void branchesPhotonSel   ( TTree*, edm::Service<TFileService>& );
    void branchesDiPhotonSel ( TTree*, edm::Service<TFileService>& );
    bool runPiSel        ( const edm::Event&, const edm::EventSetup& );
    bool runPhotonSel    ( const edm::Event&, const edm::EventSetup& );
    bool runDiPhotonSel  ( const edm::Event&, const edm::EventSetup& );
    void fillPiSel       ( const edm::Event&, const edm::EventSetup& );
    void fillPhotonSel   ( const edm::Event&, const edm::EventSetup& );
    void fillDiPhotonSel ( const edm::Event&, const edm::EventSetup& );

    std::map<unsigned int, std::vector<unsigned int>> mGenPi0_RecoPho;
    std::vector<int> vPreselPhoIdxs_;
    std::vector<int> vRegressPhoIdxs_;
    std::vector<float> vIphi_Emax_;
    std::vector<float> vIeta_Emax_;

    //std::vector<std::vector<float>> vEB_SCenergy_;
    std::vector<std::vector<float>> vSC_energy_;
    std::vector<std::vector<float>> vSC_energyT_;
    std::vector<std::vector<float>> vSC_energyZ_;
    std::vector<std::vector<float>> vSC_time_;

    //TH2F *hTracks_EE[nEE];
    TH2F *hTracks_EB;
    //TH2F *hTracksPt_EE[nEE];
    TH2F *hTracksPt_EB;
    //std::vector<float> vTracksPt_EE_[nEE];
    //std::vector<float> vTracksQPt_EE_[nEE];
    //std::vector<float> vTracks_EE_[nEE];
    std::vector<float> vTracksPt_EB_;
    std::vector<float> vTracksQPt_EB_;
    std::vector<float> vTracks_EB_;

    std::vector<float> vPho_pT_;
    std::vector<float> vPho_E_;
    std::vector<float> vPho_eta_;
    std::vector<float> vPho_phi_;
    std::vector<float> vPho_r9_;
    std::vector<float> vPho_sieie_;
    std::vector<float> vPho_phoIso_; 
    std::vector<float> vPho_chgIso_; 
    std::vector<float> vPho_chgIsoWrongVtx_; 
    std::vector<float> vPho_Eraw_; 
    std::vector<float> vPho_phiWidth_; 
    std::vector<float> vPho_etaWidth_; 
    std::vector<float> vPho_scEta_; 
    std::vector<float> vPho_sieip_; 
    std::vector<float> vPho_s4_; 

    std::vector<float> vSC_mass_;
    std::vector<float> vSC_DR_;
    std::vector<float> vSC_pT_;

    int nTotal, nPassed;

    //TProfile2D * hnPho;
    TH2F * hnPho;
    TH2F * hnPhoGt2;
    TH1F * hdR_nPhoGt2;
    TH2F * hdPhidEta_nPhoGt2;
    TProfile2D * hdPhidEta_jphoPt_o_iphoPt;
    TH1F * hjphoPt_o_iphoPt;

    float m0_;
    std::vector<float> vFC_inputs_;

};

//
// constants, enums and typedefs
//
static const float zs = 0.;

static const int crop_size = 32;
//static const bool debug = true;
static const bool debug = false;

static const int EB_IPHI_MIN = EBDetId::MIN_IPHI;//1;
static const int EB_IPHI_MAX = EBDetId::MAX_IPHI;//360;
static const int EB_IETA_MIN = EBDetId::MIN_IETA;//1;
static const int EB_IETA_MAX = EBDetId::MAX_IETA;//85;
static const int EE_MIN_IX = EEDetId::IX_MIN;//1;
static const int EE_MIN_IY = EEDetId::IY_MIN;//1;
static const int EE_MAX_IX = EEDetId::IX_MAX;//100;
static const int EE_MAX_IY = EEDetId::IY_MAX;//100;
static const int EE_NC_PER_ZSIDE = EEDetId::IX_MAX*EEDetId::IY_MAX; // 100*100
//
// static data member definitions
//

#endif
