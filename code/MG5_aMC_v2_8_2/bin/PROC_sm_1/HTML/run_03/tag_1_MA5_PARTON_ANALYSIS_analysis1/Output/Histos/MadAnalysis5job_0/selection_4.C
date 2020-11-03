void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo99","canvas_plotflow_tempo99",0,0,700,500);
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
  S5_ETA_0->SetBinContent(7,504.5679922);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,3027.4079532);
  S5_ETA_0->SetBinContent(10,6559.3838986);
  S5_ETA_0->SetBinContent(11,11605.0598206);
  S5_ETA_0->SetBinContent(12,26742.0995866);
  S5_ETA_0->SetBinContent(13,79217.1687754);
  S5_ETA_0->SetBinContent(14,142792.697793);
  S5_ETA_0->SetBinContent(15,256825.09603);
  S5_ETA_0->SetBinContent(16,359252.394446);
  S5_ETA_0->SetBinContent(17,417782.293542);
  S5_ETA_0->SetBinContent(18,437460.493237);
  S5_ETA_0->SetBinContent(19,418286.893534);
  S5_ETA_0->SetBinContent(20,365811.794345);
  S5_ETA_0->SetBinContent(21,406681.793713);
  S5_ETA_0->SetBinContent(22,409709.193666);
  S5_ETA_0->SetBinContent(23,426359.993409);
  S5_ETA_0->SetBinContent(24,431910.193323);
  S5_ETA_0->SetBinContent(25,362784.394392);
  S5_ETA_0->SetBinContent(26,230587.596435);
  S5_ETA_0->SetBinContent(27,133205.997941);
  S5_ETA_0->SetBinContent(28,66602.9789704);
  S5_ETA_0->SetBinContent(29,30778.6495242);
  S5_ETA_0->SetBinContent(30,13118.7697972);
  S5_ETA_0->SetBinContent(31,3027.4079532);
  S5_ETA_0->SetBinContent(32,3027.4079532);
  S5_ETA_0->SetBinContent(33,2018.2719688);
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
  THStack* stack = new THStack("mystack_100","mystack");
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
