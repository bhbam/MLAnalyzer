#include "TFile.h"
#include "TH1.h"
#include "TH2F.h"
#include "TLegend.h"
#include "TString.h"
#include "TCanvas.h"
#include "TEfficiency.h"
#include "TStyle.h"

void plot_triger_eff_from_same_file (const TString& infile = "merged_H_AA_4Tau_M3p7_trigger_test.root")
{

  gStyle->SetPadTopMargin(0.08);
  gStyle->SetPadBottomMargin(0.12);
  gStyle->SetPadLeftMargin(0.15);
  gStyle->SetPadRightMargin(0.05);
  gStyle->SetOptStat(0);

  TH1::SetDefaultSumw2();

  TFile* f_in = new TFile(infile);


  // ---- efficiency vs met

  TH1F* h_met_denom = (TH1F*) f_in->Get("fevt/h_jet_eta_all");
  TH1F* h_met_num = (TH1F*) f_in->Get("fevt/h_jet_eta_passtrig");

  // TCanvas* c_met = new TCanvas("tau_pt","tau_pt");
  // c_met->SetGrid(1,1);
  // c_met->cd();
  // TH2F* h_met_axis = new TH2F("h_met_axis",";tau_pT [GeV];Efficiency",20,10,200,20,0,1);
  // h_met_axis->GetYaxis()->SetTitleOffset(1);
  // h_met_axis->Draw();
  // c_met->SetLogy();
  // TCanvas* c_met = new TCanvas("tau_eta","tau_eta");
  // c_met->SetGrid(1,1);
  // c_met->cd();
  // TH2F* h_met_axis = new TH2F("h_met_axis",";tau_eta; Efficiency",20,-3,3,20,0,1);
  // h_met_axis->GetYaxis()->SetTitleOffset(0.98);
  // h_met_axis->Draw();

  // TCanvas* c_met = new TCanvas("tau_E","tau_E");
  // c_met->SetGrid(1,1);
  // c_met->cd();
  // TH2F* h_met_axis = new TH2F("h_met_axis",";tau_E [GeV];Efficiency",20,0,500,20,0,1);
  // h_met_axis->GetYaxis()->SetTitleOffset(0.98);
  // h_met_axis->Draw();

  // TCanvas* c_met = new TCanvas("jet_E","jet_E");
  // c_met->SetGrid(1,1);
  // c_met->cd();
  // TH2F* h_met_axis = new TH2F("h_met_axis",";Jet_E [GeV];Efficiency",20,0,500,20,0,1);
  // h_met_axis->GetYaxis()->SetTitleOffset(0.98);
  // h_met_axis->Draw();

  // TCanvas* c_met = new TCanvas("jet_pt","jet_pt");
  // c_met->SetGrid(1,1);
  // c_met->cd();
  // TH2F* h_met_axis = new TH2F("h_met_axis",";jet_pT [GeV];Efficiency",20,10,200,20,0,1);
  // h_met_axis->GetYaxis()->SetTitleOffset(0.98);
  // h_met_axis->Draw();

  TCanvas* c_met = new TCanvas("jet_eta","jet_eta");
  c_met->SetGrid(1,1);
  c_met->cd();
  TH2F* h_met_axis = new TH2F("h_met_axis",";jet_eta; Efficiency",20,-3,3,20,0,1);
  h_met_axis->GetYaxis()->SetTitleOffset(0.98);
  h_met_axis->Draw();

  TEfficiency* h_met_eff = new TEfficiency(*h_met_num, *h_met_denom);
  h_met_eff->SetLineColor(kRed);
  h_met_eff->SetMarkerColor(kRed);

  h_met_eff->Draw("pe same");
  c_met->SaveAs("trigger_plots/eff_jet_eta.png");
  // c_met->SaveAs("eff_tau_E.pdf");

  return;
}
