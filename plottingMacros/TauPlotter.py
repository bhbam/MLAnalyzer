#!/usr/bin/env python
  
import numpy as np

import ROOT
from ROOT import TCanvas, TPad, TFile, TPaveText, TLegend
from ROOT import gBenchmark, gStyle, gROOT, TStyle
from ROOT import TH1D, TF1, TGraphErrors, TMultiGraph

from math import sqrt

from array import array

import tdrstyle
tdrstyle.setTDRStyle()

import CMS_lumi

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.lumi_13TeV = '13 TeV'
CMS_lumi.writeExtraText = 1
#CMS_lumi.extraText = 'Preliminary'
CMS_lumi.extraText = 'Simulation'

iPos    = 0
iPeriod = 0

gStyle.SetOptFit(0)

def loadcanvas(name):
  canvas = TCanvas(name,name,400,20,1400,1000)
  canvas.SetFillColor(0)
  canvas.SetBorderMode(0)
  canvas.SetFrameFillStyle(0)
  canvas.SetFrameBorderMode(0)
  canvas.SetTickx(0)
  canvas.SetTicky(0)
  return canvas

def loadlegend(top, bottom, left, right):
  relPosX    = 0.001
  relPosY    = 0.005
  posX = -1
  posX = 1 - right - relPosX*(1-left-right)
  posY = 1 - top - relPosY*(1-top-bottom)
  legendOffsetX = 0.0
  legendOffsetY = 0.
  textSize   = 0.05
  textFont   = 60
  legendSizeX = 0.4
  legendSizeY = 0.2
  legend = TLegend(posX-legendSizeX+legendOffsetX,posY-legendSizeY+legendOffsetY,posX+legendOffsetX,posY+legendOffsetY)
  legend.SetTextSize(textSize)
  legend.SetLineStyle(0)
  legend.SetBorderSize(0)
  return legend

TauHistos = {}
Histos = ['h_jet_E','h_jet_eta','h_jet_m0','h_jet_ma','h_jet_dR','h_jet_TaudR','h_jet_Tau1dR','h_jet_Tau2dR','h_jet_n1dR','h_jet_n2dR','h_jet_recoTau1dR','h_jet_recoTau2dR','h_jet_NrecoTaus']
histos={}
TauHistos['M3p7'] = {
                    'file'  : 'HToAAToTauTau_Hadronic_M3p7_13TeV_2018_RHAnalyzer.root',
                    }
TauHistos['M5']   = {
                    'file'  : 'HToAAToTauTau_Hadronic_M5_13TeV_2018_RHAnalyzer.root',
                    }
TauHistos['M10']  = {
                    'file'  : 'HToAAToTauTau_Hadronic_M10_13TeV_2018_RHAnalyzer.root',
                    }
TauHistos['M15']  = {
                    'file'  : 'HToAAToTauTau_Hadronic_M15_13TeV_2018_RHAnalyzer.root',
                    }
TauHistos['M20'] =  {
                    'file'  : 'HToAAToTauTau_Hadronic_M20_13TeV_2018_RHAnalyzer.root',
                    }

files_ = []
for iMass in TauHistos:
  iFile = TauHistos[iMass]['file']
  files_.append( TFile(iFile) )
  for iHisto in Histos:
    tmp_ = files_[-1].Get('fevt/'+iHisto)
    #print(iHisto+'_'+iMass)
    histos[iHisto+'_'+iMass] = tmp_.Clone(iHisto+'_'+iMass)

canvas = loadcanvas("c10")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_NrecoTaus_M5'].SetLineColor(6)
histos['h_jet_NrecoTaus_M5'].SetLineWidth(3)
histos['h_jet_NrecoTaus_M5'].SetXTitle("#tau^{RECO}")
histos['h_jet_NrecoTaus_M5'].SetYTitle("Jets")
histos['h_jet_NrecoTaus_M5'].Draw()
histos['h_jet_NrecoTaus_M3p7'].SetLineColor(2)
histos['h_jet_NrecoTaus_M3p7'].SetLineWidth(3)
histos['h_jet_NrecoTaus_M3p7'].Draw('same')
histos['h_jet_NrecoTaus_M10'].SetLineColor(95)
histos['h_jet_NrecoTaus_M10'].SetLineWidth(3)
histos['h_jet_NrecoTaus_M10'].Draw('same')
histos['h_jet_NrecoTaus_M15'].SetLineColor(4)
histos['h_jet_NrecoTaus_M15'].SetLineWidth(3)
histos['h_jet_NrecoTaus_M15'].Draw('same')
histos['h_jet_NrecoTaus_M20'].SetLineColor(3)
histos['h_jet_NrecoTaus_M20'].SetLineWidth(3)
histos['h_jet_NrecoTaus_M20'].Draw('same')
legend.AddEntry(histos['h_jet_NrecoTaus_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_NrecoTaus_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_NrecoTaus_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_NrecoTaus_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_NrecoTaus_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('N_recotaus.png')

canvas = loadcanvas("c8")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_recoTau1dR_M3p7'].SetLineColor(2)
histos['h_jet_recoTau1dR_M3p7'].SetLineWidth(3)
histos['h_jet_recoTau1dR_M3p7'].SetXTitle("#DeltaR_{j,#tau_{1}^{RECO}}")
histos['h_jet_recoTau1dR_M3p7'].SetYTitle("Jets")
histos['h_jet_recoTau1dR_M3p7'].Draw()
histos['h_jet_recoTau1dR_M5'].SetLineColor(6)
histos['h_jet_recoTau1dR_M5'].SetLineWidth(3)
histos['h_jet_recoTau1dR_M5'].Draw('same')
histos['h_jet_recoTau1dR_M10'].SetLineColor(95)
histos['h_jet_recoTau1dR_M10'].SetLineWidth(3)
histos['h_jet_recoTau1dR_M10'].Draw('same')
histos['h_jet_recoTau1dR_M15'].SetLineColor(4)
histos['h_jet_recoTau1dR_M15'].SetLineWidth(3)
histos['h_jet_recoTau1dR_M15'].Draw('same')
histos['h_jet_recoTau1dR_M20'].SetLineColor(3)
histos['h_jet_recoTau1dR_M20'].SetLineWidth(3)
histos['h_jet_recoTau1dR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_recoTau1dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau1dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau1dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau1dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau1dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_jrecotau1.png')

canvas = loadcanvas("c9")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_recoTau2dR_M20'].SetLineColor(3)
histos['h_jet_recoTau2dR_M20'].SetLineWidth(3)
histos['h_jet_recoTau2dR_M20'].SetXTitle("#DeltaR_{j,#tau_{2}^{RECO}}")
histos['h_jet_recoTau2dR_M20'].SetYTitle("Jets")
histos['h_jet_recoTau2dR_M20'].GetYaxis().SetRangeUser(0,10)
histos['h_jet_recoTau2dR_M20'].Draw()
histos['h_jet_recoTau2dR_M5'].SetLineColor(6)
histos['h_jet_recoTau2dR_M5'].SetLineWidth(3)
histos['h_jet_recoTau2dR_M5'].Draw('same')
histos['h_jet_recoTau2dR_M10'].SetLineColor(95)
histos['h_jet_recoTau2dR_M10'].SetLineWidth(3)
histos['h_jet_recoTau2dR_M10'].Draw('same')
histos['h_jet_recoTau2dR_M15'].SetLineColor(4)
histos['h_jet_recoTau2dR_M15'].SetLineWidth(3)
histos['h_jet_recoTau2dR_M15'].Draw('same')
histos['h_jet_recoTau2dR_M3p7'].SetLineColor(2)
histos['h_jet_recoTau2dR_M3p7'].SetLineWidth(3)
histos['h_jet_recoTau2dR_M3p7'].Draw('same')
legend.AddEntry(histos['h_jet_recoTau2dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau2dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau2dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau2dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_recoTau2dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_jrecotau2.png')

canvas = loadcanvas("c1")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_ma_M3p7'].SetLineColor(2)
histos['h_jet_ma_M3p7'].SetLineWidth(3)
histos['h_jet_ma_M3p7'].SetXTitle("m_{a} GeV")
histos['h_jet_ma_M3p7'].SetYTitle("Jets")
histos['h_jet_ma_M3p7'].Draw()
histos['h_jet_ma_M5'].SetLineColor(6)
histos['h_jet_ma_M5'].SetLineWidth(3)
histos['h_jet_ma_M5'].Draw('same')
histos['h_jet_ma_M10'].SetLineColor(95)
histos['h_jet_ma_M10'].SetLineWidth(3)
histos['h_jet_ma_M10'].Draw('same')
histos['h_jet_ma_M15'].SetLineColor(4)
histos['h_jet_ma_M15'].SetLineWidth(3)
histos['h_jet_ma_M15'].Draw('same')
histos['h_jet_ma_M20'].SetLineColor(3)
histos['h_jet_ma_M20'].SetLineWidth(3)
histos['h_jet_ma_M20'].Draw('same')
legend.AddEntry(histos['h_jet_ma_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_ma_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_ma_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_ma_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_ma_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('m_a.png')

canvas = loadcanvas("c2")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_dR_M3p7'].SetLineColor(2)
histos['h_jet_dR_M3p7'].SetLineWidth(3)
histos['h_jet_dR_M3p7'].SetXTitle("#DeltaR_{j,a}")
histos['h_jet_dR_M3p7'].SetYTitle("Jets")
histos['h_jet_dR_M3p7'].Draw()
histos['h_jet_dR_M5'].SetLineColor(6)
histos['h_jet_dR_M5'].SetLineWidth(3)
histos['h_jet_dR_M5'].Draw('same')
histos['h_jet_dR_M10'].SetLineColor(95)
histos['h_jet_dR_M10'].SetLineWidth(3)
histos['h_jet_dR_M10'].Draw('same')
histos['h_jet_dR_M15'].SetLineColor(4)
histos['h_jet_dR_M15'].SetLineWidth(3)
histos['h_jet_dR_M15'].Draw('same')
histos['h_jet_dR_M20'].SetLineColor(3)
histos['h_jet_dR_M20'].SetLineWidth(3)
histos['h_jet_dR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_aj.png')

canvas = loadcanvas("c3")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_TaudR_M3p7'].SetLineColor(2)
histos['h_jet_TaudR_M3p7'].SetLineWidth(3)
histos['h_jet_TaudR_M3p7'].SetXTitle("#DeltaR_{#tau,#tau}")
histos['h_jet_TaudR_M3p7'].SetYTitle("Jets")
histos['h_jet_TaudR_M3p7'].Draw()
histos['h_jet_TaudR_M5'].SetLineColor(6)
histos['h_jet_TaudR_M5'].SetLineWidth(3)
histos['h_jet_TaudR_M5'].Draw('same')
histos['h_jet_TaudR_M10'].SetLineColor(95)
histos['h_jet_TaudR_M10'].SetLineWidth(3)
histos['h_jet_TaudR_M10'].Draw('same')
histos['h_jet_TaudR_M15'].SetLineColor(4)
histos['h_jet_TaudR_M15'].SetLineWidth(3)
histos['h_jet_TaudR_M15'].Draw('same')
histos['h_jet_TaudR_M20'].SetLineColor(3)
histos['h_jet_TaudR_M20'].SetLineWidth(3)
histos['h_jet_TaudR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_TaudR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_TaudR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_TaudR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_TaudR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_TaudR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_taus.png')

canvas = loadcanvas("c4")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_Tau1dR_M3p7'].SetLineColor(2)
histos['h_jet_Tau1dR_M3p7'].SetLineWidth(3)
histos['h_jet_Tau1dR_M3p7'].SetXTitle("#DeltaR_{j,#tau_{1}}")
histos['h_jet_Tau1dR_M3p7'].SetYTitle("Jets")
histos['h_jet_Tau1dR_M3p7'].Draw()
histos['h_jet_Tau1dR_M5'].SetLineColor(6)
histos['h_jet_Tau1dR_M5'].SetLineWidth(3)
histos['h_jet_Tau1dR_M5'].Draw('same')
histos['h_jet_Tau1dR_M10'].SetLineColor(95)
histos['h_jet_Tau1dR_M10'].SetLineWidth(3)
histos['h_jet_Tau1dR_M10'].Draw('same')
histos['h_jet_Tau1dR_M15'].SetLineColor(4)
histos['h_jet_Tau1dR_M15'].SetLineWidth(3)
histos['h_jet_Tau1dR_M15'].Draw('same')
histos['h_jet_Tau1dR_M20'].SetLineColor(3)
histos['h_jet_Tau1dR_M20'].SetLineWidth(3)
histos['h_jet_Tau1dR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_Tau1dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_Tau1dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_Tau1dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_Tau1dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_Tau1dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_jtau1.png')

canvas = loadcanvas("c5")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_Tau2dR_M3p7'].SetLineColor(2)
histos['h_jet_Tau2dR_M3p7'].SetLineWidth(3)
histos['h_jet_Tau2dR_M3p7'].SetXTitle("#DeltaR_{j,#tau_{2}}")
histos['h_jet_Tau2dR_M3p7'].SetYTitle("Jets")
histos['h_jet_Tau2dR_M3p7'].Draw()
histos['h_jet_Tau2dR_M5'].SetLineColor(6)
histos['h_jet_Tau2dR_M5'].SetLineWidth(3)
histos['h_jet_Tau2dR_M5'].Draw('same')
histos['h_jet_Tau2dR_M10'].SetLineColor(95)
histos['h_jet_Tau2dR_M10'].SetLineWidth(3)
histos['h_jet_Tau2dR_M10'].Draw('same')
histos['h_jet_Tau2dR_M15'].SetLineColor(4)
histos['h_jet_Tau2dR_M15'].SetLineWidth(3)
histos['h_jet_Tau2dR_M15'].Draw('same')
histos['h_jet_Tau2dR_M20'].SetLineColor(3)
histos['h_jet_Tau2dR_M20'].SetLineWidth(3)
histos['h_jet_Tau2dR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_Tau2dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_Tau2dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_Tau2dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_Tau2dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_Tau2dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_jtau2.png')

canvas = loadcanvas("c6")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_n1dR_M3p7'].SetLineColor(2)
histos['h_jet_n1dR_M3p7'].SetLineWidth(3)
histos['h_jet_n1dR_M3p7'].SetXTitle("#DeltaR_{j,#eta_{1}}")
histos['h_jet_n1dR_M3p7'].SetYTitle("Jets")
histos['h_jet_n1dR_M3p7'].Draw()
histos['h_jet_n1dR_M5'].SetLineColor(6)
histos['h_jet_n1dR_M5'].SetLineWidth(3)
histos['h_jet_n1dR_M5'].Draw('same')
histos['h_jet_n1dR_M10'].SetLineColor(95)
histos['h_jet_n1dR_M10'].SetLineWidth(3)
histos['h_jet_n1dR_M10'].Draw('same')
histos['h_jet_n1dR_M15'].SetLineColor(4)
histos['h_jet_n1dR_M15'].SetLineWidth(3)
histos['h_jet_n1dR_M15'].Draw('same')
histos['h_jet_n1dR_M20'].SetLineColor(3)
histos['h_jet_n1dR_M20'].SetLineWidth(3)
histos['h_jet_n1dR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_n1dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_n1dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_n1dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_n1dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_n1dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_jnu1.png')

canvas = loadcanvas("c7")
canvas.cd()
legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
histos['h_jet_n2dR_M3p7'].SetLineColor(2)
histos['h_jet_n2dR_M3p7'].SetLineWidth(3)
histos['h_jet_n2dR_M3p7'].SetXTitle("#DeltaR_{j,#eta_{2}}")
histos['h_jet_n2dR_M3p7'].SetYTitle("Jets")
histos['h_jet_n2dR_M3p7'].Draw()
histos['h_jet_n2dR_M5'].SetLineColor(6)
histos['h_jet_n2dR_M5'].SetLineWidth(3)
histos['h_jet_n2dR_M5'].Draw('same')
histos['h_jet_n2dR_M10'].SetLineColor(95)
histos['h_jet_n2dR_M10'].SetLineWidth(3)
histos['h_jet_n2dR_M10'].Draw('same')
histos['h_jet_n2dR_M15'].SetLineColor(4)
histos['h_jet_n2dR_M15'].SetLineWidth(3)
histos['h_jet_n2dR_M15'].Draw('same')
histos['h_jet_n2dR_M20'].SetLineColor(3)
histos['h_jet_n2dR_M20'].SetLineWidth(3)
histos['h_jet_n2dR_M20'].Draw('same')
legend.AddEntry(histos['h_jet_n2dR_M3p7'], 'm_{a} = 3.7 GeV','lf')
legend.AddEntry(histos['h_jet_n2dR_M5'],   'm_{a} = 5 GeV','lf')
legend.AddEntry(histos['h_jet_n2dR_M10'],  'm_{a} = 10 GeV','lf')
legend.AddEntry(histos['h_jet_n2dR_M15'],  'm_{a} = 15 GeV','lf')
legend.AddEntry(histos['h_jet_n2dR_M20'],  'm_{a} = 20 GeV','lf')
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
canvas.Update()
legend.Draw()
canvas.SaveAs('dR_jnu2.png')