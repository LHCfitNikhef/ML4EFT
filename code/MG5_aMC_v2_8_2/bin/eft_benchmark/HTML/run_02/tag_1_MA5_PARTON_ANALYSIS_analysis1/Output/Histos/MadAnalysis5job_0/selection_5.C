void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo65","canvas_plotflow_tempo65",0,0,700,500);
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
  S6_PT_0->SetBinContent(1,371.5876087);
  S6_PT_0->SetBinContent(2,1255.7100294);
  S6_PT_0->SetBinContent(3,1870.7510438);
  S6_PT_0->SetBinContent(4,2857.3800669);
  S6_PT_0->SetBinContent(5,2690.806063);
  S6_PT_0->SetBinContent(6,2959.8870693);
  S6_PT_0->SetBinContent(7,3196.93407485);
  S6_PT_0->SetBinContent(8,3267.4080765);
  S6_PT_0->SetBinContent(9,3280.2210768);
  S6_PT_0->SetBinContent(10,3228.9680756);
  S6_PT_0->SetBinContent(11,3055.98707155);
  S6_PT_0->SetBinContent(12,2677.9930627);
  S6_PT_0->SetBinContent(13,2613.9260612);
  S6_PT_0->SetBinContent(14,2626.7400615);
  S6_PT_0->SetBinContent(15,2133.42504995);
  S6_PT_0->SetBinContent(16,2152.6450504);
  S6_PT_0->SetBinContent(17,2075.7650486);
  S6_PT_0->SetBinContent(18,1864.34404365);
  S6_PT_0->SetBinContent(19,1684.95703945);
  S6_PT_0->SetBinContent(20,1691.3640396);
  S6_PT_0->SetBinContent(21,1364.62303195);
  S6_PT_0->SetBinContent(22,1255.7100294);
  S6_PT_0->SetBinContent(23,1069.91602505);
  S6_PT_0->SetBinContent(24,909.7488213);
  S6_PT_0->SetBinContent(25,922.5622216);
  S6_PT_0->SetBinContent(26,800.83531875);
  S6_PT_0->SetBinContent(27,826.46201935);
  S6_PT_0->SetBinContent(28,653.4816153);
  S6_PT_0->SetBinContent(29,723.95511695);
  S6_PT_0->SetBinContent(30,659.88821545);
  S6_PT_0->SetBinContent(31,531.75461245);
  S6_PT_0->SetBinContent(32,550.9747129);
  S6_PT_0->SetBinContent(33,474.0945111);
  S6_PT_0->SetBinContent(34,384.400909);
  S6_PT_0->SetBinContent(35,377.99420885);
  S6_PT_0->SetBinContent(36,320.3341075);
  S6_PT_0->SetBinContent(37,269.0806063);
  S6_PT_0->SetBinContent(38,313.92740735);
  S6_PT_0->SetBinContent(39,288.30070675);
  S6_PT_0->SetBinContent(40,281.8940066);
  S6_PT_0->SetBinContent(41,3530.08208265); // overflow
  S6_PT_0->SetEntries(10000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_66","mystack");
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
