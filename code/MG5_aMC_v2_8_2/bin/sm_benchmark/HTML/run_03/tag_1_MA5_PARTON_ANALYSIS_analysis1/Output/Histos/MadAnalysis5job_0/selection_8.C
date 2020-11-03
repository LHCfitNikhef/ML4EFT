void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo107","canvas_plotflow_tempo107",0,0,700,500);
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
  S9_DELTAR_0->SetBinContent(13,1978595.29467);
  S9_DELTAR_0->SetBinContent(14,1347746.20072);
  S9_DELTAR_0->SetBinContent(15,643808.195882);
  S9_DELTAR_0->SetBinContent(16,355597.752959);
  S9_DELTAR_0->SetBinContent(17,237929.135435);
  S9_DELTAR_0->SetBinContent(18,163803.024395);
  S9_DELTAR_0->SetBinContent(19,120778.817988);
  S9_DELTAR_0->SetBinContent(20,89158.6232784);
  S9_DELTAR_0->SetBinContent(21,60130.2389552);
  S9_DELTAR_0->SetBinContent(22,41987.4962532);
  S9_DELTAR_0->SetBinContent(23,28510.024246);
  S9_DELTAR_0->SetBinContent(24,31101.844632);
  S9_DELTAR_0->SetBinContent(25,22808.0233968);
  S9_DELTAR_0->SetBinContent(26,11404.0116984);
  S9_DELTAR_0->SetBinContent(27,9848.9174668);
  S9_DELTAR_0->SetBinContent(28,6738.7330036);
  S9_DELTAR_0->SetBinContent(29,7775.461158);
  S9_DELTAR_0->SetBinContent(30,5702.0048492);
  S9_DELTAR_0->SetBinContent(31,6738.7330036);
  S9_DELTAR_0->SetBinContent(32,3628.5485404);
  S9_DELTAR_0->SetBinContent(33,2591.820386);
  S9_DELTAR_0->SetBinContent(34,518.3640772);
  S9_DELTAR_0->SetBinContent(35,1555.0922316);
  S9_DELTAR_0->SetBinContent(36,1036.7281544);
  S9_DELTAR_0->SetBinContent(37,0.0);
  S9_DELTAR_0->SetBinContent(38,1036.7281544);
  S9_DELTAR_0->SetBinContent(39,1036.7281544);
  S9_DELTAR_0->SetBinContent(40,518.3640772);
  S9_DELTAR_0->SetBinContent(41,1555.0922316); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_108","mystack");
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
