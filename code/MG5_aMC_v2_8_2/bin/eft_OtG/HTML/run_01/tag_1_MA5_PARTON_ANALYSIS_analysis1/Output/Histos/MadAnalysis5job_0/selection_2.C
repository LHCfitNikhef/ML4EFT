void selection_2()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo113","canvas_plotflow_tempo113",0,0,700,500);
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
  TH1F* S3_SQRTS_0 = new TH1F("S3_SQRTS_0","S3_SQRTS_0",40,0.0,500.0);
  // Content
  S3_SQRTS_0->SetBinContent(0,0.0); // underflow
  S3_SQRTS_0->SetBinContent(1,0.0);
  S3_SQRTS_0->SetBinContent(2,0.0);
  S3_SQRTS_0->SetBinContent(3,0.0);
  S3_SQRTS_0->SetBinContent(4,0.0);
  S3_SQRTS_0->SetBinContent(5,0.0);
  S3_SQRTS_0->SetBinContent(6,0.0);
  S3_SQRTS_0->SetBinContent(7,0.0);
  S3_SQRTS_0->SetBinContent(8,0.0);
  S3_SQRTS_0->SetBinContent(9,0.0);
  S3_SQRTS_0->SetBinContent(10,0.0);
  S3_SQRTS_0->SetBinContent(11,0.0);
  S3_SQRTS_0->SetBinContent(12,0.0);
  S3_SQRTS_0->SetBinContent(13,0.0);
  S3_SQRTS_0->SetBinContent(14,0.0);
  S3_SQRTS_0->SetBinContent(15,0.0);
  S3_SQRTS_0->SetBinContent(16,0.0);
  S3_SQRTS_0->SetBinContent(17,0.0);
  S3_SQRTS_0->SetBinContent(18,0.0);
  S3_SQRTS_0->SetBinContent(19,0.0);
  S3_SQRTS_0->SetBinContent(20,0.0);
  S3_SQRTS_0->SetBinContent(21,0.0);
  S3_SQRTS_0->SetBinContent(22,0.0);
  S3_SQRTS_0->SetBinContent(23,0.0);
  S3_SQRTS_0->SetBinContent(24,0.0);
  S3_SQRTS_0->SetBinContent(25,0.0);
  S3_SQRTS_0->SetBinContent(26,0.0);
  S3_SQRTS_0->SetBinContent(27,0.0);
  S3_SQRTS_0->SetBinContent(28,67180.707858);
  S3_SQRTS_0->SetBinContent(29,272015.991327);
  S3_SQRTS_0->SetBinContent(30,337879.489227);
  S3_SQRTS_0->SetBinContent(31,398473.787295);
  S3_SQRTS_0->SetBinContent(32,370811.188177);
  S3_SQRTS_0->SetBinContent(33,387277.087652);
  S3_SQRTS_0->SetBinContent(34,343148.589059);
  S3_SQRTS_0->SetBinContent(35,324706.789647);
  S3_SQRTS_0->SetBinContent(36,312192.690046);
  S3_SQRTS_0->SetBinContent(37,293750.990634);
  S3_SQRTS_0->SetBinContent(38,278602.391117);
  S3_SQRTS_0->SetBinContent(39,235132.492503);
  S3_SQRTS_0->SetBinContent(40,234473.892524);
  S3_SQRTS_0->SetBinContent(41,2730697.91293); // overflow
  S3_SQRTS_0->SetEntries(10000);
  // Style
  S3_SQRTS_0->SetLineColor(9);
  S3_SQRTS_0->SetLineStyle(1);
  S3_SQRTS_0->SetLineWidth(1);
  S3_SQRTS_0->SetFillColor(9);
  S3_SQRTS_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_114","mystack");
  stack->Add(S3_SQRTS_0);
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
  stack->GetXaxis()->SetTitle("#sqrt{#hat{s}} (GeV) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_2.eps");

}
