void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo83","canvas_plotflow_tempo83",0,0,700,500);
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
  TH1F* S6_PT_0 = new TH1F("S6_PT_0","S6_PT_0",40,0.0,500.0);
  // Content
  S6_PT_0->SetBinContent(0,0.0); // underflow
  S6_PT_0->SetBinContent(1,60500.520276);
  S6_PT_0->SetBinContent(2,161838.900738);
  S6_PT_0->SetBinContent(3,236960.401081);
  S6_PT_0->SetBinContent(4,299477.601366);
  S6_PT_0->SetBinContent(5,369053.201684);
  S6_PT_0->SetBinContent(6,406361.801854);
  S6_PT_0->SetBinContent(7,423503.601932);
  S6_PT_0->SetBinContent(8,418461.901909);
  S6_PT_0->SetBinContent(9,366532.301672);
  S6_PT_0->SetBinContent(10,361994.801651);
  S6_PT_0->SetBinContent(11,313594.401431);
  S6_PT_0->SetBinContent(12,265698.101212);
  S6_PT_0->SetBinContent(13,218810.200998);
  S6_PT_0->SetBinContent(14,197130.900899);
  S6_PT_0->SetBinContent(15,162847.200743);
  S6_PT_0->SetBinContent(16,136126.200621);
  S6_PT_0->SetBinContent(17,110413.400504);
  S6_PT_0->SetBinContent(18,88734.0904048);
  S6_PT_0->SetBinContent(19,77138.1603519);
  S6_PT_0->SetBinContent(20,55458.810253);
  S6_PT_0->SetBinContent(21,47896.2402185);
  S6_PT_0->SetBinContent(22,43358.7101978);
  S6_PT_0->SetBinContent(23,35291.970161);
  S6_PT_0->SetBinContent(24,32771.1101495);
  S6_PT_0->SetBinContent(25,25208.550115);
  S6_PT_0->SetBinContent(26,17645.9800805);
  S6_PT_0->SetBinContent(27,14620.9600667);
  S6_PT_0->SetBinContent(28,18654.3300851);
  S6_PT_0->SetBinContent(29,12100.1000552);
  S6_PT_0->SetBinContent(30,7058.3940322);
  S6_PT_0->SetBinContent(31,8066.7360368);
  S6_PT_0->SetBinContent(32,5545.8810253);
  S6_PT_0->SetBinContent(33,5545.8810253);
  S6_PT_0->SetBinContent(34,7562.5650345);
  S6_PT_0->SetBinContent(35,5041.710023);
  S6_PT_0->SetBinContent(36,2520.8550115);
  S6_PT_0->SetBinContent(37,4537.5390207);
  S6_PT_0->SetBinContent(38,2520.8550115);
  S6_PT_0->SetBinContent(39,0.0);
  S6_PT_0->SetBinContent(40,504.1710023);
  S6_PT_0->SetBinContent(41,14620.9600667); // overflow
  S6_PT_0->SetEntries(10000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_84","mystack");
  stack->Add(S6_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ t_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
