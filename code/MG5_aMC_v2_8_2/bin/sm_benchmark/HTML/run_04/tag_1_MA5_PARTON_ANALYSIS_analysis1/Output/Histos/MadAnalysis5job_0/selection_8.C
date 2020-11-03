void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S9_DELTAR_0 = new TH1F("S9_DELTAR_0","S9_DELTAR_0",40,0.0,10.0);
  // Content
  S9_DELTAR_0->SetBinContent(0,0.0); // underflow
  S9_DELTAR_0->SetBinContent(1,0.0);
  S9_DELTAR_0->SetBinContent(2,0.0);
  S9_DELTAR_0->SetBinContent(3,0.0);
  S9_DELTAR_0->SetBinContent(4,0.0);
  S9_DELTAR_0->SetBinContent(5,0.0);
  S9_DELTAR_0->SetBinContent(6,0.0);
  S9_DELTAR_0->SetBinContent(7,0.0);
  S9_DELTAR_0->SetBinContent(8,0.0);
  S9_DELTAR_0->SetBinContent(9,0.0);
  S9_DELTAR_0->SetBinContent(10,0.0);
  S9_DELTAR_0->SetBinContent(11,0.0);
  S9_DELTAR_0->SetBinContent(12,0.0);
  S9_DELTAR_0->SetBinContent(13,2001183.03625);
  S9_DELTAR_0->SetBinContent(14,1255929.02275);
  S9_DELTAR_0->SetBinContent(15,668445.012107);
  S9_DELTAR_0->SetBinContent(16,380930.6069);
  S9_DELTAR_0->SetBinContent(17,255337.704625);
  S9_DELTAR_0->SetBinContent(18,158288.602867);
  S9_DELTAR_0->SetBinContent(19,116251.302106);
  S9_DELTAR_0->SetBinContent(20,83036.641504);
  S9_DELTAR_0->SetBinContent(21,72657.061316);
  S9_DELTAR_0->SetBinContent(22,51378.9209306);
  S9_DELTAR_0->SetBinContent(23,28543.850517);
  S9_DELTAR_0->SetBinContent(24,24392.0104418);
  S9_DELTAR_0->SetBinContent(25,25429.9704606);
  S9_DELTAR_0->SetBinContent(26,22316.1004042);
  S9_DELTAR_0->SetBinContent(27,12455.5002256);
  S9_DELTAR_0->SetBinContent(28,4670.8110846);
  S9_DELTAR_0->SetBinContent(29,4151.8320752);
  S9_DELTAR_0->SetBinContent(30,3113.8740564);
  S9_DELTAR_0->SetBinContent(31,6746.7271222);
  S9_DELTAR_0->SetBinContent(32,5708.7691034);
  S9_DELTAR_0->SetBinContent(33,2075.9160376);
  S9_DELTAR_0->SetBinContent(34,2075.9160376);
  S9_DELTAR_0->SetBinContent(35,1037.9580188);
  S9_DELTAR_0->SetBinContent(36,1556.9370282);
  S9_DELTAR_0->SetBinContent(37,1037.9580188);
  S9_DELTAR_0->SetBinContent(38,518.9790094);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,518.9790094); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_DELTAR_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("#DeltaR [ t~_{1}, t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
