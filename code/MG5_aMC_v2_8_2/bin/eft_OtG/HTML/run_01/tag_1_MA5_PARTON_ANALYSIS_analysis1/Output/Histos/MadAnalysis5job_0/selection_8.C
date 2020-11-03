void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo125","canvas_plotflow_tempo125",0,0,700,500);
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
  S9_DELTAR_0->SetBinContent(13,2471196.21255);
  S9_DELTAR_0->SetBinContent(14,1687421.14514);
  S9_DELTAR_0->SetBinContent(15,824610.370926);
  S9_DELTAR_0->SetBinContent(16,509124.44379);
  S9_DELTAR_0->SetBinContent(17,295068.225379);
  S9_DELTAR_0->SetBinContent(18,210104.418071);
  S9_DELTAR_0->SetBinContent(19,161365.413879);
  S9_DELTAR_0->SetBinContent(20,109333.309404);
  S9_DELTAR_0->SetBinContent(21,79036.146798);
  S9_DELTAR_0->SetBinContent(22,63887.5454951);
  S9_DELTAR_0->SetBinContent(23,50714.8543621);
  S9_DELTAR_0->SetBinContent(24,32931.7228325);
  S9_DELTAR_0->SetBinContent(25,27004.0123227);
  S9_DELTAR_0->SetBinContent(26,15148.591303);
  S9_DELTAR_0->SetBinContent(27,10538.1509064);
  S9_DELTAR_0->SetBinContent(28,6586.3455665);
  S9_DELTAR_0->SetBinContent(29,9879.51784975);
  S9_DELTAR_0->SetBinContent(30,3951.8073399);
  S9_DELTAR_0->SetBinContent(31,3951.8073399);
  S9_DELTAR_0->SetBinContent(32,1975.90316995);
  S9_DELTAR_0->SetBinContent(33,3293.17228325);
  S9_DELTAR_0->SetBinContent(34,1317.2691133);
  S9_DELTAR_0->SetBinContent(35,1317.2691133);
  S9_DELTAR_0->SetBinContent(36,1317.2691133);
  S9_DELTAR_0->SetBinContent(37,1317.2691133);
  S9_DELTAR_0->SetBinContent(38,658.63455665);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,3293.17228325); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_126","mystack");
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
