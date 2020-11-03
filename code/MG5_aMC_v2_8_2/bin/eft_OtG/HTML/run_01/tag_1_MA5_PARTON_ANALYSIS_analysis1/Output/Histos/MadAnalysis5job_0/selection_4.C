void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo117","canvas_plotflow_tempo117",0,0,700,500);
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
  S5_ETA_0->SetBinContent(8,658.63445095);
  S5_ETA_0->SetBinContent(9,3293.17175475);
  S5_ETA_0->SetBinContent(10,3951.8067057);
  S5_ETA_0->SetBinContent(11,21076.2984304);
  S5_ETA_0->SetBinContent(12,43469.8667627);
  S5_ETA_0->SetBinContent(13,92867.4530839);
  S5_ETA_0->SetBinContent(14,196273.085383);
  S5_ETA_0->SetBinContent(15,317461.776358);
  S5_ETA_0->SetBinContent(16,464995.865371);
  S5_ETA_0->SetBinContent(17,564449.657964);
  S5_ETA_0->SetBinContent(18,579598.256836);
  S5_ETA_0->SetBinContent(19,521638.461152);
  S5_ETA_0->SetBinContent(20,509124.362084);
  S5_ETA_0->SetBinContent(21,508465.762133);
  S5_ETA_0->SetBinContent(22,524931.660907);
  S5_ETA_0->SetBinContent(23,553252.858798);
  S5_ETA_0->SetBinContent(24,520321.161251);
  S5_ETA_0->SetBinContent(25,468289.065125);
  S5_ETA_0->SetBinContent(26,317461.776358);
  S5_ETA_0->SetBinContent(27,196931.685334);
  S5_ETA_0->SetBinContent(28,109991.991809);
  S5_ETA_0->SetBinContent(29,38200.7971551);
  S5_ETA_0->SetBinContent(30,15148.5888719);
  S5_ETA_0->SetBinContent(31,10538.1492152);
  S5_ETA_0->SetBinContent(32,2634.5378038);
  S5_ETA_0->SetBinContent(33,658.63445095);
  S5_ETA_0->SetBinContent(34,658.63445095);
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
  THStack* stack = new THStack("mystack_118","mystack");
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
