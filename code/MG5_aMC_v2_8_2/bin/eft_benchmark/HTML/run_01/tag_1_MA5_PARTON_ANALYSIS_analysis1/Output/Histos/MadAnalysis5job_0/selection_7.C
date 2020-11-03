void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo51","canvas_plotflow_tempo51",0,0,700,500);
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
  TH1F* S8_M_0 = new TH1F("S8_M_0","S8_M_0",40,0.0,500.0);
  // Content
  S8_M_0->SetBinContent(0,0.0); // underflow
  S8_M_0->SetBinContent(1,0.0);
  S8_M_0->SetBinContent(2,0.0);
  S8_M_0->SetBinContent(3,0.0);
  S8_M_0->SetBinContent(4,0.0);
  S8_M_0->SetBinContent(5,0.0);
  S8_M_0->SetBinContent(6,0.0);
  S8_M_0->SetBinContent(7,0.0);
  S8_M_0->SetBinContent(8,0.0);
  S8_M_0->SetBinContent(9,0.0);
  S8_M_0->SetBinContent(10,0.0);
  S8_M_0->SetBinContent(11,0.0);
  S8_M_0->SetBinContent(12,0.0);
  S8_M_0->SetBinContent(13,0.0);
  S8_M_0->SetBinContent(14,0.0);
  S8_M_0->SetBinContent(15,0.0);
  S8_M_0->SetBinContent(16,0.0);
  S8_M_0->SetBinContent(17,0.0);
  S8_M_0->SetBinContent(18,0.0);
  S8_M_0->SetBinContent(19,0.0);
  S8_M_0->SetBinContent(20,0.0);
  S8_M_0->SetBinContent(21,0.0);
  S8_M_0->SetBinContent(22,0.0);
  S8_M_0->SetBinContent(23,0.0);
  S8_M_0->SetBinContent(24,0.0);
  S8_M_0->SetBinContent(25,0.0);
  S8_M_0->SetBinContent(26,0.0);
  S8_M_0->SetBinContent(27,0.0);
  S8_M_0->SetBinContent(28,15500.6233279);
  S8_M_0->SetBinContent(29,66984.8347315);
  S8_M_0->SetBinContent(30,81378.2649227);
  S8_M_0->SetBinContent(31,88159.7873662);
  S8_M_0->SetBinContent(32,81101.4756868);
  S8_M_0->SetBinContent(33,80686.2718368);
  S8_M_0->SetBinContent(34,79855.884133);
  S8_M_0->SetBinContent(35,74735.143296);
  S8_M_0->SetBinContent(36,67261.6339654);
  S8_M_0->SetBinContent(37,63248.0800662);
  S8_M_0->SetBinContent(38,59926.5092547);
  S8_M_0->SetBinContent(39,45809.8782974);
  S8_M_0->SetBinContent(40,45394.6844455);
  S8_M_0->SetBinContent(41,532833.92867); // overflow
  S8_M_0->SetEntries(10000);
  // Style
  S8_M_0->SetLineColor(9);
  S8_M_0->SetLineStyle(1);
  S8_M_0->SetLineWidth(1);
  S8_M_0->SetFillColor(9);
  S8_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_52","mystack");
  stack->Add(S8_M_0);
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
  stack->GetXaxis()->SetTitle("M [ t_{1} t~_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
