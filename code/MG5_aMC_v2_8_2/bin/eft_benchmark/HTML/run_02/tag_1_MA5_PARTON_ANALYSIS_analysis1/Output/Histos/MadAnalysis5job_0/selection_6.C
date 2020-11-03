void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo67","canvas_plotflow_tempo67",0,0,700,500);
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
  S7_ETA_0->SetBinContent(6,6.4066819718);
  S7_ETA_0->SetBinContent(7,0.0);
  S7_ETA_0->SetBinContent(8,12.8133599436);
  S7_ETA_0->SetBinContent(9,25.6267298872);
  S7_ETA_0->SetBinContent(10,83.2868696334);
  S7_ETA_0->SetBinContent(11,275.487298787);
  S7_ETA_0->SetBinContent(12,602.228097349);
  S7_ETA_0->SetBinContent(13,1050.69599538);
  S7_ETA_0->SetBinContent(14,2428.13198931);
  S7_ETA_0->SetBinContent(15,3530.08198446);
  S7_ETA_0->SetBinContent(16,5138.15897738);
  S7_ETA_0->SetBinContent(17,5368.79997637);
  S7_ETA_0->SetBinContent(18,5189.41197716);
  S7_ETA_0->SetBinContent(19,4362.9499808);
  S7_ETA_0->SetBinContent(20,4138.71698178);
  S7_ETA_0->SetBinContent(21,4228.40998139);
  S7_ETA_0->SetBinContent(22,4657.6579795);
  S7_ETA_0->SetBinContent(23,4945.95897823);
  S7_ETA_0->SetBinContent(24,5099.71897755);
  S7_ETA_0->SetBinContent(25,4638.43797958);
  S7_ETA_0->SetBinContent(26,3536.48798443);
  S7_ETA_0->SetBinContent(27,2460.16598917);
  S7_ETA_0->SetBinContent(28,1242.89599453);
  S7_ETA_0->SetBinContent(29,723.955096813);
  S7_ETA_0->SetBinContent(30,160.167099295);
  S7_ETA_0->SetBinContent(31,70.4734996898);
  S7_ETA_0->SetBinContent(32,44.8467698026);
  S7_ETA_0->SetBinContent(33,32.033409859);
  S7_ETA_0->SetBinContent(34,0.0);
  S7_ETA_0->SetBinContent(35,12.8133599436);
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
  THStack* stack = new THStack("mystack_68","mystack");
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
