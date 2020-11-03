void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
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
  TH1F* S9_DELTAR_0 = new TH1F("S9_DELTAR_0","S9_DELTAR_0",40,0.0,10.0);
  // Content
  S9_DELTAR_0->SetBinContent(0,0.0); // underflow
  S9_DELTAR_0->SetBinContent(1,0.0);
  S9_DELTAR_0->SetBinContent(2,0.0);
  S9_DELTAR_0->SetBinContent(3,0.0);
  S9_DELTAR_0->SetBinContent(4,0.0);
  S9_DELTAR_0->SetBinContent(5,0.0);
  S9_DELTAR_0->SetBinContent(6,0.0);
  S9_DELTAR_0->SetBinContent(7,0.0);
  S9_DELTAR_0->SetBinContent(8,0.0);
  S9_DELTAR_0->SetBinContent(9,0.0);
  S9_DELTAR_0->SetBinContent(10,0.0);
  S9_DELTAR_0->SetBinContent(11,0.0);
  S9_DELTAR_0->SetBinContent(12,0.0);
  S9_DELTAR_0->SetBinContent(13,2004070.26589);
  S9_DELTAR_0->SetBinContent(14,1275035.16917);
  S9_DELTAR_0->SetBinContent(15,648375.786024);
  S9_DELTAR_0->SetBinContent(16,369170.94898);
  S9_DELTAR_0->SetBinContent(17,256454.834026);
  S9_DELTAR_0->SetBinContent(18,154079.720443);
  S9_DELTAR_0->SetBinContent(19,109096.714475);
  S9_DELTAR_0->SetBinContent(20,93068.292348);
  S9_DELTAR_0->SetBinContent(21,71869.4095354);
  S9_DELTAR_0->SetBinContent(22,43948.915831);
  S9_DELTAR_0->SetBinContent(23,31539.8141846);
  S9_DELTAR_0->SetBinContent(24,31022.764116);
  S9_DELTAR_0->SetBinContent(25,16545.4721952);
  S9_DELTAR_0->SetBinContent(26,17579.5623324);
  S9_DELTAR_0->SetBinContent(27,9823.8753034);
  S9_DELTAR_0->SetBinContent(28,7755.691029);
  S9_DELTAR_0->SetBinContent(29,8789.7831662);
  S9_DELTAR_0->SetBinContent(30,8272.7370976);
  S9_DELTAR_0->SetBinContent(31,4136.3685488);
  S9_DELTAR_0->SetBinContent(32,1551.1382058);
  S9_DELTAR_0->SetBinContent(33,2068.1842744);
  S9_DELTAR_0->SetBinContent(34,2585.230343);
  S9_DELTAR_0->SetBinContent(35,1034.0921372);
  S9_DELTAR_0->SetBinContent(36,1034.0921372);
  S9_DELTAR_0->SetBinContent(37,517.0460686);
  S9_DELTAR_0->SetBinContent(38,517.0460686);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,517.0460686); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ t~_{1}, t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
