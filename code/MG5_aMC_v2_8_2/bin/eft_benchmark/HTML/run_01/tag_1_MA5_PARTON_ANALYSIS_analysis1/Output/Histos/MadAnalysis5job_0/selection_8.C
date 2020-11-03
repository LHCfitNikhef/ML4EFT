void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo53","canvas_plotflow_tempo53",0,0,700,500);
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
  S9_DELTAR_0->SetBinContent(13,558437.638669);
  S9_DELTAR_0->SetBinContent(14,358175.089282);
  S9_DELTAR_0->SetBinContent(15,165524.520109);
  S9_DELTAR_0->SetBinContent(16,93142.1383543);
  S9_DELTAR_0->SetBinContent(17,62556.0876316);
  S9_DELTAR_0->SetBinContent(18,36260.3800886);
  S9_DELTAR_0->SetBinContent(19,28233.2722066);
  S9_DELTAR_0->SetBinContent(20,20898.1574176);
  S9_DELTAR_0->SetBinContent(21,14947.0288148);
  S9_DELTAR_0->SetBinContent(22,9549.49068723);
  S9_DELTAR_0->SetBinContent(23,9272.69344999);
  S9_DELTAR_0->SetBinContent(24,8580.70135672);
  S9_DELTAR_0->SetBinContent(25,3875.15532241);
  S9_DELTAR_0->SetBinContent(26,3321.56184776);
  S9_DELTAR_0->SetBinContent(27,2214.37489844);
  S9_DELTAR_0->SetBinContent(28,1937.57766121);
  S9_DELTAR_0->SetBinContent(29,1383.98418655);
  S9_DELTAR_0->SetBinContent(30,1522.38280517);
  S9_DELTAR_0->SetBinContent(31,553.59367462);
  S9_DELTAR_0->SetBinContent(32,415.195255965);
  S9_DELTAR_0->SetBinContent(33,138.398418655);
  S9_DELTAR_0->SetBinContent(34,415.195255965);
  S9_DELTAR_0->SetBinContent(35,553.59367462);
  S9_DELTAR_0->SetBinContent(36,276.79683731);
  S9_DELTAR_0->SetBinContent(37,138.398418655);
  S9_DELTAR_0->SetBinContent(38,0.0);
  S9_DELTAR_0->SetBinContent(39,0.0);
  S9_DELTAR_0->SetBinContent(40,0.0);
  S9_DELTAR_0->SetBinContent(41,553.59367462); // overflow
  S9_DELTAR_0->SetEntries(10000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_54","mystack");
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
