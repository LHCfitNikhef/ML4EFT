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
  S9_DELTAR_0->SetBinContent(13,1939054.8532);
  S9_DELTAR_0->SetBinContent(14,1248805.90545);
  S9_DELTAR_0->SetBinContent(15,638278.451677);
  S9_DELTAR_0->SetBinContent(16,359756.972763);
  S9_DELTAR_0->SetBinContent(17,249761.181091);
  S9_DELTAR_0->SetBinContent(18,173066.786897);
  S9_DELTAR_0->SetBinContent(19,115041.49129);
  S9_DELTAR_0->SetBinContent(20,83758.2836588);
  S9_DELTAR_0->SetBinContent(21,59539.0154924);
  S9_DELTAR_0->SetBinContent(22,36833.4572114);
  S9_DELTAR_0->SetBinContent(23,35824.3272878);
  S9_DELTAR_0->SetBinContent(24,24219.2581664);
  S9_DELTAR_0->SetBinContent(25,18164.4486248);
  S9_DELTAR_0->SetBinContent(26,17155.3087012);
  S9_DELTAR_0->SetBinContent(27,15641.6088158);
  S9_DELTAR_0->SetBinContent(28,11100.4991596);
  S9_DELTAR_0->SetBinContent(29,5550.2475798);
  S9_DELTAR_0->SetBinContent(30,3531.9757326);
  S9_DELTAR_0->SetBinContent(31,2522.839809);
  S9_DELTAR_0->SetBinContent(32,2018.2718472);
  S9_DELTAR_0->SetBinContent(33,504.5679618);
  S9_DELTAR_0->SetBinContent(34,2018.2718472);
  S9_DELTAR_0->SetBinContent(35,2018.2718472);
  S9_DELTAR_0->SetBinContent(36,504.5679618);
  S9_DELTAR_0->SetBinContent(37,0.0);
  S9_DELTAR_0->SetBinContent(38,504.5679618);
  S9_DELTAR_0->SetBinContent(39,504.5679618);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,0.0); // overflow
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
