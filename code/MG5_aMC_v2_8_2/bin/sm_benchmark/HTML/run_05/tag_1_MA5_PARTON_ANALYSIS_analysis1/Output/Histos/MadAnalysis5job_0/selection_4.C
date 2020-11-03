void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  S5_ETA_0->SetBinContent(8,1034.091914);
  S5_ETA_0->SetBinContent(9,1034.091914);
  S5_ETA_0->SetBinContent(10,6204.551484);
  S5_ETA_0->SetBinContent(11,11892.059011);
  S5_ETA_0->SetBinContent(12,35676.177033);
  S5_ETA_0->SetBinContent(13,76005.763679);
  S5_ETA_0->SetBinContent(14,148909.287616);
  S5_ETA_0->SetBinContent(15,253352.57893);
  S5_ETA_0->SetBinContent(16,344352.571362);
  S5_ETA_0->SetBinContent(17,416221.965385);
  S5_ETA_0->SetBinContent(18,446727.762848);
  S5_ETA_0->SetBinContent(19,410017.465901);
  S5_ETA_0->SetBinContent(20,415187.965471);
  S5_ETA_0->SetBinContent(21,415187.965471);
  S5_ETA_0->SetBinContent(22,411568.565772);
  S5_ETA_0->SetBinContent(23,447761.862762);
  S5_ETA_0->SetBinContent(24,411568.565772);
  S5_ETA_0->SetBinContent(25,347971.971061);
  S5_ETA_0->SetBinContent(26,277136.676952);
  S5_ETA_0->SetBinContent(27,160284.28667);
  S5_ETA_0->SetBinContent(28,78590.993464);
  S5_ETA_0->SetBinContent(29,31539.807377);
  S5_ETA_0->SetBinContent(30,14994.328753);
  S5_ETA_0->SetBinContent(31,5170.45957);
  S5_ETA_0->SetBinContent(32,1034.091914);
  S5_ETA_0->SetBinContent(33,1034.091914);
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
  THStack* stack = new THStack("mystack_10","mystack");
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
