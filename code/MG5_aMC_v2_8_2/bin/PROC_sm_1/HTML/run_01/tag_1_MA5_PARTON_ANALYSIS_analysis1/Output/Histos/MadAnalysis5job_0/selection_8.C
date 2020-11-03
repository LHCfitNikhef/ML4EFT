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
  S9_DELTAR_0->SetBinContent(13,1973695.10689);
  S9_DELTAR_0->SetBinContent(14,1226919.06645);
  S9_DELTAR_0->SetBinContent(15,627373.133976);
  S9_DELTAR_0->SetBinContent(16,377941.720468);
  S9_DELTAR_0->SetBinContent(17,250949.21359);
  S9_DELTAR_0->SetBinContent(18,166962.209042);
  S9_DELTAR_0->SetBinContent(19,108778.405891);
  S9_DELTAR_0->SetBinContent(20,88540.554795);
  S9_DELTAR_0->SetBinContent(21,51606.4927948);
  S9_DELTAR_0->SetBinContent(22,37440.0120276);
  S9_DELTAR_0->SetBinContent(23,34404.3318632);
  S9_DELTAR_0->SetBinContent(24,27827.031507);
  S9_DELTAR_0->SetBinContent(25,23779.4612878);
  S9_DELTAR_0->SetBinContent(26,19225.9510412);
  S9_DELTAR_0->SetBinContent(27,13154.6007124);
  S9_DELTAR_0->SetBinContent(28,9612.9745206);
  S9_DELTAR_0->SetBinContent(29,5565.4063014);
  S9_DELTAR_0->SetBinContent(30,4047.5682192);
  S9_DELTAR_0->SetBinContent(31,3035.6761644);
  S9_DELTAR_0->SetBinContent(32,1517.8380822);
  S9_DELTAR_0->SetBinContent(33,2023.7841096);
  S9_DELTAR_0->SetBinContent(34,1011.8920548);
  S9_DELTAR_0->SetBinContent(35,1011.8920548);
  S9_DELTAR_0->SetBinContent(36,505.9460274);
  S9_DELTAR_0->SetBinContent(37,505.9460274);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,1011.8920548);
  S9_DELTAR_0->SetBinContent(41,1011.8920548); // overflow
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
