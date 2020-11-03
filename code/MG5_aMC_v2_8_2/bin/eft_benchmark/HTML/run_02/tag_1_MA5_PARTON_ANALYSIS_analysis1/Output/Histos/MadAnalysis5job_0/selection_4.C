void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo63","canvas_plotflow_tempo63",0,0,700,500);
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
  S5_ETA_0->SetBinContent(7,6.4066820184);
  S5_ETA_0->SetBinContent(8,12.8133600368);
  S5_ETA_0->SetBinContent(9,12.8133600368);
  S5_ETA_0->SetBinContent(10,64.066820184);
  S5_ETA_0->SetBinContent(11,83.2868702392);
  S5_ETA_0->SetBinContent(12,237.047200681);
  S5_ETA_0->SetBinContent(13,589.414701693);
  S5_ETA_0->SetBinContent(14,1262.11600362);
  S5_ETA_0->SetBinContent(15,2677.99300769);
  S5_ETA_0->SetBinContent(16,3959.32901137);
  S5_ETA_0->SetBinContent(17,4913.92501411);
  S5_ETA_0->SetBinContent(18,5830.08101674);
  S5_ETA_0->SetBinContent(19,6381.05501833);
  S5_ETA_0->SetBinContent(20,6489.96901864);
  S5_ETA_0->SetBinContent(21,6009.46801726);
  S5_ETA_0->SetBinContent(22,6284.95501805);
  S5_ETA_0->SetBinContent(23,5714.76001641);
  S5_ETA_0->SetBinContent(24,4843.45201391);
  S5_ETA_0->SetBinContent(25,3709.46901065);
  S5_ETA_0->SetBinContent(26,2402.5060069);
  S5_ETA_0->SetBinContent(27,1409.47000405);
  S5_ETA_0->SetBinContent(28,711.141702042);
  S5_ETA_0->SetBinContent(29,288.300700828);
  S5_ETA_0->SetBinContent(30,89.6935502576);
  S5_ETA_0->SetBinContent(31,51.2534601472);
  S5_ETA_0->SetBinContent(32,19.2200500552);
  S5_ETA_0->SetBinContent(33,6.4066820184);
  S5_ETA_0->SetBinContent(34,0.0);
  S5_ETA_0->SetBinContent(35,6.4066820184);
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
  THStack* stack = new THStack("mystack_64","mystack");
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
