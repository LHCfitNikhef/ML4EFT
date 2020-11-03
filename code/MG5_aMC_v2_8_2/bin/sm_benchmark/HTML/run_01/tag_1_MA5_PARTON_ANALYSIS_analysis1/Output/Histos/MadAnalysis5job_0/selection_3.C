void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,700,500);
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
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",40,0.0,500.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,53541.9778885);
  S4_PT_0->SetBinContent(2,166343.99344);
  S4_PT_0->SetBinContent(3,259392.68977);
  S4_PT_0->SetBinContent(4,321251.887331);
  S4_PT_0->SetBinContent(5,372194.685322);
  S4_PT_0->SetBinContent(6,423657.383292);
  S4_PT_0->SetBinContent(7,451208.082206);
  S4_PT_0->SetBinContent(8,413780.683682);
  S4_PT_0->SetBinContent(9,387269.584728);
  S4_PT_0->SetBinContent(10,345163.786388);
  S4_PT_0->SetBinContent(11,308256.187844);
  S4_PT_0->SetBinContent(12,263551.289606);
  S4_PT_0->SetBinContent(13,237040.190652);
  S4_PT_0->SetBinContent(14,193894.692354);
  S4_PT_0->SetBinContent(15,167383.693399);
  S4_PT_0->SetBinContent(16,145550.99426);
  S4_PT_0->SetBinContent(17,113321.895531);
  S4_PT_0->SetBinContent(18,93568.49631);
  S4_PT_0->SetBinContent(19,82652.1767405);
  S4_PT_0->SetBinContent(20,65497.947417);
  S4_PT_0->SetBinContent(21,55101.447827);
  S4_PT_0->SetBinContent(22,51462.6779705);
  S4_PT_0->SetBinContent(23,40026.5284215);
  S4_PT_0->SetBinContent(24,22352.4791185);
  S4_PT_0->SetBinContent(25,21312.8291595);
  S4_PT_0->SetBinContent(26,18193.8792825);
  S4_PT_0->SetBinContent(27,18193.8792825);
  S4_PT_0->SetBinContent(28,17154.2293235);
  S4_PT_0->SetBinContent(29,10396.49959);
  S4_PT_0->SetBinContent(30,11955.9795285);
  S4_PT_0->SetBinContent(31,12995.6294875);
  S4_PT_0->SetBinContent(32,9876.6746105);
  S4_PT_0->SetBinContent(33,5198.249795);
  S4_PT_0->SetBinContent(34,5198.249795);
  S4_PT_0->SetBinContent(35,1559.4749385);
  S4_PT_0->SetBinContent(36,4678.4248155);
  S4_PT_0->SetBinContent(37,1559.4749385);
  S4_PT_0->SetBinContent(38,3638.7748565);
  S4_PT_0->SetBinContent(39,3638.7748565);
  S4_PT_0->SetBinContent(40,519.8249795);
  S4_PT_0->SetBinContent(41,18713.699262); // overflow
  S4_PT_0->SetEntries(10000);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ t~_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
