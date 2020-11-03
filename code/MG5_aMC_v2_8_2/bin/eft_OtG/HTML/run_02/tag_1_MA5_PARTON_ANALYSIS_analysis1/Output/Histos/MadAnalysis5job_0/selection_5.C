void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo137","canvas_plotflow_tempo137",0,0,700,500);
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
  TH1F* S6_PT_0 = new TH1F("S6_PT_0","S6_PT_0",40,0.0,500.0);
  // Content
  S6_PT_0->SetBinContent(0,0.0); // underflow
  S6_PT_0->SetBinContent(1,71993.2984725);
  S6_PT_0->SetBinContent(2,210696.036997);
  S6_PT_0->SetBinContent(3,345435.696708);
  S6_PT_0->SetBinContent(4,421391.973995);
  S6_PT_0->SetBinContent(5,488761.85385);
  S6_PT_0->SetBinContent(6,532354.140815);
  S6_PT_0->SetBinContent(7,543582.437458);
  S6_PT_0->SetBinContent(8,554150.234298);
  S6_PT_0->SetBinContent(9,511878.946938);
  S6_PT_0->SetBinContent(10,441867.167872);
  S6_PT_0->SetBinContent(11,408842.677748);
  S6_PT_0->SetBinContent(12,336849.399275);
  S6_PT_0->SetBinContent(13,307127.408162);
  S6_PT_0->SetBinContent(14,233152.630282);
  S6_PT_0->SetBinContent(15,196165.241342);
  S6_PT_0->SetBinContent(16,157196.352995);
  S6_PT_0->SetBinContent(17,131437.360697);
  S6_PT_0->SetBinContent(18,121529.96366);
  S6_PT_0->SetBinContent(19,91807.9725475);
  S6_PT_0->SetBinContent(20,77277.2168925);
  S6_PT_0->SetBinContent(21,74635.2576825);
  S6_PT_0->SetBinContent(22,64727.920645);
  S6_PT_0->SetBinContent(23,35005.9195325);
  S6_PT_0->SetBinContent(24,40950.317755);
  S6_PT_0->SetBinContent(25,35666.409335);
  S6_PT_0->SetBinContent(26,25098.582495);
  S6_PT_0->SetBinContent(27,26419.5621);
  S6_PT_0->SetBinContent(28,22456.623285);
  S6_PT_0->SetBinContent(29,11228.3166425);
  S6_PT_0->SetBinContent(30,8586.3574325);
  S6_PT_0->SetBinContent(31,15851.73526);
  S6_PT_0->SetBinContent(32,6604.890025);
  S6_PT_0->SetBinContent(33,4623.4226175);
  S6_PT_0->SetBinContent(34,2641.95621);
  S6_PT_0->SetBinContent(35,7265.3788275);
  S6_PT_0->SetBinContent(36,7925.86763);
  S6_PT_0->SetBinContent(37,5283.91242);
  S6_PT_0->SetBinContent(38,3962.933815);
  S6_PT_0->SetBinContent(39,4623.4226175);
  S6_PT_0->SetBinContent(40,1981.4674075);
  S6_PT_0->SetBinContent(41,15851.73526); // overflow
  S6_PT_0->SetEntries(10000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_138","mystack");
  stack->Add(S6_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ t_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
