void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo139","canvas_plotflow_tempo139",0,0,700,500);
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
  TH1F* S7_ETA_0 = new TH1F("S7_ETA_0","S7_ETA_0",40,-10.0,10.0);
  // Content
  S7_ETA_0->SetBinContent(0,0.0); // underflow
  S7_ETA_0->SetBinContent(1,0.0);
  S7_ETA_0->SetBinContent(2,0.0);
  S7_ETA_0->SetBinContent(3,0.0);
  S7_ETA_0->SetBinContent(4,0.0);
  S7_ETA_0->SetBinContent(5,0.0);
  S7_ETA_0->SetBinContent(6,0.0);
  S7_ETA_0->SetBinContent(7,660.48901014);
  S7_ETA_0->SetBinContent(8,0.0);
  S7_ETA_0->SetBinContent(9,3962.93386084);
  S7_ETA_0->SetBinContent(10,6604.8901014);
  S7_ETA_0->SetBinContent(11,15191.2456332);
  S7_ETA_0->SetBinContent(12,41610.8080388);
  S7_ETA_0->SetBinContent(13,109641.168483);
  S7_ETA_0->SetBinContent(14,176350.549307);
  S7_ETA_0->SetBinContent(15,290615.116462);
  S7_ETA_0->SetBinContent(16,478854.562351);
  S7_ETA_0->SetBinContent(17,560094.638999);
  S7_ETA_0->SetBinContent(18,554150.240707);
  S7_ETA_0->SetBinContent(19,555471.240328);
  S7_ETA_0->SetBinContent(20,531693.647163);
  S7_ETA_0->SetBinContent(21,509237.053618);
  S7_ETA_0->SetBinContent(22,527070.248492);
  S7_ETA_0->SetBinContent(23,577927.833873);
  S7_ETA_0->SetBinContent(24,540940.544505);
  S7_ETA_0->SetBinContent(25,457058.368617);
  S7_ETA_0->SetBinContent(26,312411.310196);
  S7_ETA_0->SetBinContent(27,192202.344751);
  S7_ETA_0->SetBinContent(28,103036.270382);
  S7_ETA_0->SetBinContent(29,38308.3589881);
  S7_ETA_0->SetBinContent(30,15851.7354434);
  S7_ETA_0->SetBinContent(31,4623.42267098);
  S7_ETA_0->SetBinContent(32,660.48901014);
  S7_ETA_0->SetBinContent(33,660.48901014);
  S7_ETA_0->SetBinContent(34,0.0);
  S7_ETA_0->SetBinContent(35,0.0);
  S7_ETA_0->SetBinContent(36,0.0);
  S7_ETA_0->SetBinContent(37,0.0);
  S7_ETA_0->SetBinContent(38,0.0);
  S7_ETA_0->SetBinContent(39,0.0);
  S7_ETA_0->SetBinContent(40,0.0);
  S7_ETA_0->SetBinContent(41,0.0); // overflow
  S7_ETA_0->SetEntries(10000);
  // Style
  S7_ETA_0->SetLineColor(9);
  S7_ETA_0->SetLineStyle(1);
  S7_ETA_0->SetLineWidth(1);
  S7_ETA_0->SetFillColor(9);
  S7_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_140","mystack");
  stack->Add(S7_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
