void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo85","canvas_plotflow_tempo85",0,0,700,500);
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
  S7_ETA_0->SetBinContent(7,1008.3420388);
  S7_ETA_0->SetBinContent(8,504.1710194);
  S7_ETA_0->SetBinContent(9,1008.3420388);
  S7_ETA_0->SetBinContent(10,9579.2493686);
  S7_ETA_0->SetBinContent(11,14620.9605626);
  S7_ETA_0->SetBinContent(12,30754.4311834);
  S7_ETA_0->SetBinContent(13,71592.2827548);
  S7_ETA_0->SetBinContent(14,144192.905548);
  S7_ETA_0->SetBinContent(15,259143.909972);
  S7_ETA_0->SetBinContent(16,358465.613793);
  S7_ETA_0->SetBinContent(17,403336.81552);
  S7_ETA_0->SetBinContent(18,440645.416956);
  S7_ETA_0->SetBinContent(19,393757.515151);
  S7_ETA_0->SetBinContent(20,409386.815753);
  S7_ETA_0->SetBinContent(21,381657.414686);
  S7_ETA_0->SetBinContent(22,409891.015772);
  S7_ETA_0->SetBinContent(23,436612.1168);
  S7_ETA_0->SetBinContent(24,414428.615947);
  S7_ETA_0->SetBinContent(25,339811.213076);
  S7_ETA_0->SetBinContent(26,244018.80939);
  S7_ETA_0->SetBinContent(27,156293.006014);
  S7_ETA_0->SetBinContent(28,72600.6227936);
  S7_ETA_0->SetBinContent(29,30250.261164);
  S7_ETA_0->SetBinContent(30,12100.1004656);
  S7_ETA_0->SetBinContent(31,2016.6840776);
  S7_ETA_0->SetBinContent(32,1512.5130582);
  S7_ETA_0->SetBinContent(33,1008.3420388);
  S7_ETA_0->SetBinContent(34,1512.5130582);
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
  THStack* stack = new THStack("mystack_86","mystack");
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
