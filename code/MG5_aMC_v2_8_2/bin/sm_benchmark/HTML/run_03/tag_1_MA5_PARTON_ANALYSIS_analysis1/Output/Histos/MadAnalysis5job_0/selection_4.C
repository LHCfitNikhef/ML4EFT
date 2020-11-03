void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo99","canvas_plotflow_tempo99",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",40,-10.0,10.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,1036.7279396);
  S5_ETA_0->SetBinContent(9,5702.0036678);
  S5_ETA_0->SetBinContent(10,3628.5477886);
  S5_ETA_0->SetBinContent(11,15550.919094);
  S5_ETA_0->SetBinContent(12,37322.2078256);
  S5_ETA_0->SetBinContent(13,82938.235168);
  S5_ETA_0->SetBinContent(14,168468.290185);
  S5_ETA_0->SetBinContent(15,270585.984236);
  S5_ETA_0->SetBinContent(16,360781.378981);
  S5_ETA_0->SetBinContent(17,426613.575145);
  S5_ETA_0->SetBinContent(18,429723.774964);
  S5_ETA_0->SetBinContent(19,407952.476233);
  S5_ETA_0->SetBinContent(20,383070.977682);
  S5_ETA_0->SetBinContent(21,398621.876776);
  S5_ETA_0->SetBinContent(22,424021.775296);
  S5_ETA_0->SetBinContent(23,441646.07427);
  S5_ETA_0->SetBinContent(24,419356.475568);
  S5_ETA_0->SetBinContent(25,360781.378981);
  S5_ETA_0->SetBinContent(26,258145.28496);
  S5_ETA_0->SetBinContent(27,160174.490668);
  S5_ETA_0->SetBinContent(28,78272.9654398);
  S5_ETA_0->SetBinContent(29,27991.6583692);
  S5_ETA_0->SetBinContent(30,11922.3693054);
  S5_ETA_0->SetBinContent(31,4665.2757282);
  S5_ETA_0->SetBinContent(32,4146.9117584);
  S5_ETA_0->SetBinContent(33,518.3639698);
  S5_ETA_0->SetBinContent(34,0.0);
  S5_ETA_0->SetBinContent(35,0.0);
  S5_ETA_0->SetBinContent(36,0.0);
  S5_ETA_0->SetBinContent(37,0.0);
  S5_ETA_0->SetBinContent(38,0.0);
  S5_ETA_0->SetBinContent(39,0.0);
  S5_ETA_0->SetBinContent(40,0.0);
  S5_ETA_0->SetBinContent(41,0.0); // overflow
  S5_ETA_0->SetEntries(10000);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_100","mystack");
  stack->Add(S5_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ t~_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
