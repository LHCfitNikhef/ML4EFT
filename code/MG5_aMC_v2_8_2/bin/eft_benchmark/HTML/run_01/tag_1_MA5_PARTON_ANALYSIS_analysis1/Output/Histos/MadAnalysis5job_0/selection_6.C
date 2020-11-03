void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo49","canvas_plotflow_tempo49",0,0,700,500);
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
  S7_ETA_0->SetBinContent(5,138.398415393);
  S7_ETA_0->SetBinContent(6,0.0);
  S7_ETA_0->SetBinContent(7,138.398415393);
  S7_ETA_0->SetBinContent(8,276.796830786);
  S7_ETA_0->SetBinContent(9,691.992076965);
  S7_ETA_0->SetBinContent(10,1107.18692322);
  S7_ETA_0->SetBinContent(11,2906.36692321);
  S7_ETA_0->SetBinContent(12,8719.10016975);
  S7_ETA_0->SetBinContent(13,20482.9630786);
  S7_ETA_0->SetBinContent(14,39166.7461572);
  S7_ETA_0->SetBinContent(15,65739.2423126);
  S7_ETA_0->SetBinContent(16,97986.0776983);
  S7_ETA_0->SetBinContent(17,123174.607696);
  S7_ETA_0->SetBinContent(18,115009.105387);
  S7_ETA_0->SetBinContent(19,112794.663953);
  S7_ETA_0->SetBinContent(20,94941.316159);
  S7_ETA_0->SetBinContent(21,100062.04693);
  S7_ETA_0->SetBinContent(22,116116.302309);
  S7_ETA_0->SetBinContent(23,128433.743082);
  S7_ETA_0->SetBinContent(24,111549.140004);
  S7_ETA_0->SetBinContent(25,98401.2715447);
  S7_ETA_0->SetBinContent(26,65877.6469268);
  S7_ETA_0->SetBinContent(27,42765.1061572);
  S7_ETA_0->SetBinContent(28,20482.9630786);
  S7_ETA_0->SetBinContent(29,8995.89700054);
  S7_ETA_0->SetBinContent(30,4843.94453875);
  S7_ETA_0->SetBinContent(31,1383.98415393);
  S7_ETA_0->SetBinContent(32,415.195246179);
  S7_ETA_0->SetBinContent(33,138.398415393);
  S7_ETA_0->SetBinContent(34,138.398415393);
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
  THStack* stack = new THStack("mystack_50","mystack");
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
