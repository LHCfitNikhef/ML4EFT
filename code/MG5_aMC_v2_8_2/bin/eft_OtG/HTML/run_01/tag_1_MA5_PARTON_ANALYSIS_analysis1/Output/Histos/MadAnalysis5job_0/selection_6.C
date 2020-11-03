void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo121","canvas_plotflow_tempo121",0,0,700,500);
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
  S7_ETA_0->SetBinContent(7,1317.2688781);
  S7_ETA_0->SetBinContent(8,2634.5377562);
  S7_ETA_0->SetBinContent(9,1975.90281715);
  S7_ETA_0->SetBinContent(10,7244.97832955);
  S7_ETA_0->SetBinContent(11,18441.7582934);
  S7_ETA_0->SetBinContent(12,38859.426404);
  S7_ETA_0->SetBinContent(13,91550.181528);
  S7_ETA_0->SetBinContent(14,169269.084336);
  S7_ETA_0->SetBinContent(15,319437.670439);
  S7_ETA_0->SetBinContent(16,463678.657091);
  S7_ETA_0->SetBinContent(17,563132.447888);
  S7_ETA_0->SetBinContent(18,589477.74545);
  S7_ETA_0->SetBinContent(19,541397.449899);
  S7_ETA_0->SetBinContent(20,522955.751606);
  S7_ETA_0->SetBinContent(21,501879.453556);
  S7_ETA_0->SetBinContent(22,536787.050326);
  S7_ETA_0->SetBinContent(23,556546.048497);
  S7_ETA_0->SetBinContent(24,558521.948314);
  S7_ETA_0->SetBinContent(25,432722.759956);
  S7_ETA_0->SetBinContent(26,324706.769952);
  S7_ETA_0->SetBinContent(27,182441.683117);
  S7_ETA_0->SetBinContent(28,86281.1020156);
  S7_ETA_0->SetBinContent(29,45445.7757944);
  S7_ETA_0->SetBinContent(30,17783.1283544);
  S7_ETA_0->SetBinContent(31,5269.0755124);
  S7_ETA_0->SetBinContent(32,3951.8066343);
  S7_ETA_0->SetBinContent(33,1975.90281715);
  S7_ETA_0->SetBinContent(34,658.63443905);
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
  THStack* stack = new THStack("mystack_122","mystack");
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
