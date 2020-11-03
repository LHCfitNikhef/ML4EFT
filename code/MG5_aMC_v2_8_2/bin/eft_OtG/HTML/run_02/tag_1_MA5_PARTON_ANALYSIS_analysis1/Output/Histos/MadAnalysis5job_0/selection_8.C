void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo143","canvas_plotflow_tempo143",0,0,700,500);
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
  S9_DELTAR_0->SetBinContent(13,2558734.33112);
  S9_DELTAR_0->SetBinContent(14,1698777.55592);
  S9_DELTAR_0->SetBinContent(15,815043.486938);
  S9_DELTAR_0->SetBinContent(16,429978.387598);
  S9_DELTAR_0->SetBinContent(17,301183.021267);
  S9_DELTAR_0->SetBinContent(18,223905.741468);
  S9_DELTAR_0->SetBinContent(19,154554.459598);
  S9_DELTAR_0->SetBinContent(20,111622.67082);
  S9_DELTAR_0->SetBinContent(21,73314.2808347);
  S9_DELTAR_0->SetBinContent(22,56141.5653239);
  S9_DELTAR_0->SetBinContent(23,52839.1261872);
  S9_DELTAR_0->SetBinContent(24,36987.390331);
  S9_DELTAR_0->SetBinContent(25,17172.7155108);
  S9_DELTAR_0->SetBinContent(26,11888.8068921);
  S9_DELTAR_0->SetBinContent(27,11888.8068921);
  S9_DELTAR_0->SetBinContent(28,15191.2460288);
  S9_DELTAR_0->SetBinContent(29,5944.40144606);
  S9_DELTAR_0->SetBinContent(30,7925.86792808);
  S9_DELTAR_0->SetBinContent(31,7265.37910074);
  S9_DELTAR_0->SetBinContent(32,2641.95630936);
  S9_DELTAR_0->SetBinContent(33,1320.97765468);
  S9_DELTAR_0->SetBinContent(34,2641.95630936);
  S9_DELTAR_0->SetBinContent(35,1981.46748202);
  S9_DELTAR_0->SetBinContent(36,2641.95630936);
  S9_DELTAR_0->SetBinContent(37,660.48902734);
  S9_DELTAR_0->SetBinContent(38,660.48902734);
  S9_DELTAR_0->SetBinContent(39,660.48902734);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,1320.97765468); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_144","mystack");
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
