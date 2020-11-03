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
  S7_ETA_0->SetBinContent(6,0.0);
  S7_ETA_0->SetBinContent(7,0.0);
  S7_ETA_0->SetBinContent(8,517.0459798);
  S7_ETA_0->SetBinContent(9,2068.1839192);
  S7_ETA_0->SetBinContent(10,6204.5517576);
  S7_ETA_0->SetBinContent(11,14994.3294142);
  S7_ETA_0->SetBinContent(12,24818.2090304);
  S7_ETA_0->SetBinContent(13,75488.7170508);
  S7_ETA_0->SetBinContent(14,133397.894788);
  S7_ETA_0->SetBinContent(15,262142.289759);
  S7_ETA_0->SetBinContent(16,368136.785618);
  S7_ETA_0->SetBinContent(17,424494.783416);
  S7_ETA_0->SetBinContent(18,453449.382285);
  S7_ETA_0->SetBinContent(19,402778.784264);
  S7_ETA_0->SetBinContent(20,403812.884224);
  S7_ETA_0->SetBinContent(21,390369.684749);
  S7_ETA_0->SetBinContent(22,453966.382264);
  S7_ETA_0->SetBinContent(23,426045.883355);
  S7_ETA_0->SetBinContent(24,423460.683456);
  S7_ETA_0->SetBinContent(25,364000.385779);
  S7_ETA_0->SetBinContent(26,249216.190264);
  S7_ETA_0->SetBinContent(27,148909.294182);
  S7_ETA_0->SetBinContent(28,77556.89697);
  S7_ETA_0->SetBinContent(29,40846.6384042);
  S7_ETA_0->SetBinContent(30,16028.4293738);
  S7_ETA_0->SetBinContent(31,2585.229899);
  S7_ETA_0->SetBinContent(32,3619.3218586);
  S7_ETA_0->SetBinContent(33,1034.0919596);
  S7_ETA_0->SetBinContent(34,0.0);
  S7_ETA_0->SetBinContent(35,0.0);
  S7_ETA_0->SetBinContent(36,0.0);
  S7_ETA_0->SetBinContent(37,0.0);
  S7_ETA_0->SetBinContent(38,517.0459798);
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
