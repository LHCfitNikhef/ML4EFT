void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,700,500);
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
  S7_ETA_0->SetBinContent(6,518.9789759);
  S7_ETA_0->SetBinContent(7,518.9789759);
  S7_ETA_0->SetBinContent(8,518.9789759);
  S7_ETA_0->SetBinContent(9,2075.9159036);
  S7_ETA_0->SetBinContent(10,6746.7266867);
  S7_ETA_0->SetBinContent(11,15569.369277);
  S7_ETA_0->SetBinContent(12,27505.8887227);
  S7_ETA_0->SetBinContent(13,71619.0966742);
  S7_ETA_0->SetBinContent(14,169187.192143);
  S7_ETA_0->SetBinContent(15,241325.188794);
  S7_ETA_0->SetBinContent(16,358614.483347);
  S7_ETA_0->SetBinContent(17,431271.579973);
  S7_ETA_0->SetBinContent(18,441132.179515);
  S7_ETA_0->SetBinContent(19,435942.379756);
  S7_ETA_0->SetBinContent(20,379892.582359);
  S7_ETA_0->SetBinContent(21,388715.281949);
  S7_ETA_0->SetBinContent(22,432309.479925);
  S7_ETA_0->SetBinContent(23,459815.378647);
  S7_ETA_0->SetBinContent(24,431271.579973);
  S7_ETA_0->SetBinContent(25,370550.982793);
  S7_ETA_0->SetBinContent(26,242363.188745);
  S7_ETA_0->SetBinContent(27,161402.492505);
  S7_ETA_0->SetBinContent(28,75770.9264814);
  S7_ETA_0->SetBinContent(29,30100.7786022);
  S7_ETA_0->SetBinContent(30,10379.579518);
  S7_ETA_0->SetBinContent(31,3113.8738554);
  S7_ETA_0->SetBinContent(32,518.9789759);
  S7_ETA_0->SetBinContent(33,518.9789759);
  S7_ETA_0->SetBinContent(34,518.9789759);
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
  THStack* stack = new THStack("mystack_14","mystack");
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
