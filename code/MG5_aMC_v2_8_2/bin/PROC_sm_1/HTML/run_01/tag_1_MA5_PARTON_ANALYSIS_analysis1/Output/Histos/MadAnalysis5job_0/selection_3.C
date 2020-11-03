void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo61","canvas_plotflow_tempo61",0,0,700,500);
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
  S4_PT_0->SetBinContent(1,45535.138704);
  S4_PT_0->SetBinContent(2,155325.395579);
  S4_PT_0->SetBinContent(3,256008.692714);
  S4_PT_0->SetBinContent(4,332406.490539);
  S4_PT_0->SetBinContent(5,396155.688725);
  S4_PT_0->SetBinContent(6,414875.688192);
  S4_PT_0->SetBinContent(7,400203.28861);
  S4_PT_0->SetBinContent(8,399191.388638);
  S4_PT_0->SetBinContent(9,379459.4892);
  S4_PT_0->SetBinContent(10,354162.18992);
  S4_PT_0->SetBinContent(11,320769.79087);
  S4_PT_0->SetBinContent(12,253984.892771);
  S4_PT_0->SetBinContent(13,242348.093102);
  S4_PT_0->SetBinContent(14,182140.594816);
  S4_PT_0->SetBinContent(15,171009.795133);
  S4_PT_0->SetBinContent(16,118391.39663);
  S4_PT_0->SetBinContent(17,117379.496659);
  S4_PT_0->SetBinContent(18,88540.54748);
  S4_PT_0->SetBinContent(19,77915.6877824);
  S4_PT_0->SetBinContent(20,59195.6783152);
  S4_PT_0->SetBinContent(21,57677.8483584);
  S4_PT_0->SetBinContent(22,35416.218992);
  S4_PT_0->SetBinContent(23,35922.1689776);
  S4_PT_0->SetBinContent(24,26815.1392368);
  S4_PT_0->SetBinContent(25,19225.9494528);
  S4_PT_0->SetBinContent(26,21755.6793808);
  S4_PT_0->SetBinContent(27,17202.1595104);
  S4_PT_0->SetBinContent(28,8601.0817552);
  S4_PT_0->SetBinContent(29,8095.1357696);
  S4_PT_0->SetBinContent(30,4553.5138704);
  S4_PT_0->SetBinContent(31,10624.8696976);
  S4_PT_0->SetBinContent(32,7589.189784);
  S4_PT_0->SetBinContent(33,5059.459856);
  S4_PT_0->SetBinContent(34,2529.729928);
  S4_PT_0->SetBinContent(35,4047.5678848);
  S4_PT_0->SetBinContent(36,2023.7839424);
  S4_PT_0->SetBinContent(37,2023.7839424);
  S4_PT_0->SetBinContent(38,4553.5138704);
  S4_PT_0->SetBinContent(39,1517.8379568);
  S4_PT_0->SetBinContent(40,2023.7839424);
  S4_PT_0->SetBinContent(41,17202.1595104); // overflow
  S4_PT_0->SetEntries(10000);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_62","mystack");
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
