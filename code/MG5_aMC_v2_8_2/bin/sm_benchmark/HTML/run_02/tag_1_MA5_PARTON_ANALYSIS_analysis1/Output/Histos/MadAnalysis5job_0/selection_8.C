void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo35","canvas_plotflow_tempo35",0,0,700,500);
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
  S9_DELTAR_0->SetBinContent(13,1978754.13221);
  S9_DELTAR_0->SetBinContent(14,1320551.08823);
  S9_DELTAR_0->SetBinContent(15,641114.442835);
  S9_DELTAR_0->SetBinContent(16,370272.024739);
  S9_DELTAR_0->SetBinContent(17,242877.716227);
  S9_DELTAR_0->SetBinContent(18,167269.711176);
  S9_DELTAR_0->SetBinContent(19,117037.00782);
  S9_DELTAR_0->SetBinContent(20,83893.8056052);
  S9_DELTAR_0->SetBinContent(21,65768.6043942);
  S9_DELTAR_0->SetBinContent(22,50232.7133562);
  S9_DELTAR_0->SetBinContent(23,37804.0025258);
  S9_DELTAR_0->SetBinContent(24,25375.2916954);
  S9_DELTAR_0->SetBinContent(25,20196.6613494);
  S9_DELTAR_0->SetBinContent(26,11910.8507958);
  S9_DELTAR_0->SetBinContent(27,9839.3976574);
  S9_DELTAR_0->SetBinContent(28,8285.8085536);
  S9_DELTAR_0->SetBinContent(29,6214.3564152);
  S9_DELTAR_0->SetBinContent(30,4660.7673114);
  S9_DELTAR_0->SetBinContent(31,4660.7673114);
  S9_DELTAR_0->SetBinContent(32,3107.1782076);
  S9_DELTAR_0->SetBinContent(33,1035.7260692);
  S9_DELTAR_0->SetBinContent(34,2589.315173);
  S9_DELTAR_0->SetBinContent(35,517.8630346);
  S9_DELTAR_0->SetBinContent(36,1553.5891038);
  S9_DELTAR_0->SetBinContent(37,3107.1782076);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,0.0); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_36","mystack");
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
