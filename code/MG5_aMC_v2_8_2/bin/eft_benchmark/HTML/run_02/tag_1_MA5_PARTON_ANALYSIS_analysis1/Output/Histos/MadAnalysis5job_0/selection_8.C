void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo71","canvas_plotflow_tempo71",0,0,700,500);
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
  S9_DELTAR_0->SetBinContent(13,28426.450205);
  S9_DELTAR_0->SetBinContent(14,17567.1201267);
  S9_DELTAR_0->SetBinContent(15,7130.63705142);
  S9_DELTAR_0->SetBinContent(16,3984.95602874);
  S9_DELTAR_0->SetBinContent(17,2139.83201543);
  S9_DELTAR_0->SetBinContent(18,1505.57001086);
  S9_DELTAR_0->SetBinContent(19,1025.06900739);
  S9_DELTAR_0->SetBinContent(20,634.261504574);
  S9_DELTAR_0->SetBinContent(21,435.654403142);
  S9_DELTAR_0->SetBinContent(22,313.927402264);
  S9_DELTAR_0->SetBinContent(23,224.233901617);
  S9_DELTAR_0->SetBinContent(24,147.353701063);
  S9_DELTAR_0->SetBinContent(25,108.913600785);
  S9_DELTAR_0->SetBinContent(26,115.320300832);
  S9_DELTAR_0->SetBinContent(27,64.066820462);
  S9_DELTAR_0->SetBinContent(28,57.6601404158);
  S9_DELTAR_0->SetBinContent(29,38.4400902772);
  S9_DELTAR_0->SetBinContent(30,25.6267301848);
  S9_DELTAR_0->SetBinContent(31,32.033410231);
  S9_DELTAR_0->SetBinContent(32,12.8133600924);
  S9_DELTAR_0->SetBinContent(33,19.2200501386);
  S9_DELTAR_0->SetBinContent(34,32.033410231);
  S9_DELTAR_0->SetBinContent(35,6.4066820462);
  S9_DELTAR_0->SetBinContent(36,0.0);
  S9_DELTAR_0->SetBinContent(37,6.4066820462);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,6.4066820462);
  S9_DELTAR_0->SetBinContent(41,6.4066820462); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_72","mystack");
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
