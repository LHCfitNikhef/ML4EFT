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
  S4_PT_0->SetBinContent(1,52935.8604998);
  S4_PT_0->SetBinContent(2,155693.70147);
  S4_PT_0->SetBinContent(3,258451.50244);
  S4_PT_0->SetBinContent(4,338893.3032);
  S4_PT_0->SetBinContent(5,400132.803778);
  S4_PT_0->SetBinContent(6,414664.203915);
  S4_PT_0->SetBinContent(7,435423.404111);
  S4_PT_0->SetBinContent(8,421929.903984);
  S4_PT_0->SetBinContent(9,393386.103714);
  S4_PT_0->SetBinContent(10,353943.703342);
  S4_PT_0->SetBinContent(11,330070.603116);
  S4_PT_0->SetBinContent(12,279729.702641);
  S4_PT_0->SetBinContent(13,228869.702161);
  S4_PT_0->SetBinContent(14,185794.501754);
  S4_PT_0->SetBinContent(15,158288.601495);
  S4_PT_0->SetBinContent(16,137010.501294);
  S4_PT_0->SetBinContent(17,118327.201117);
  S4_PT_0->SetBinContent(18,77327.8707301);
  S4_PT_0->SetBinContent(19,89264.3908428);
  S4_PT_0->SetBinContent(20,57606.6705439);
  S4_PT_0->SetBinContent(21,49821.9804704);
  S4_PT_0->SetBinContent(22,39961.3803773);
  S4_PT_0->SetBinContent(23,29062.8202744);
  S4_PT_0->SetBinContent(24,21278.1402009);
  S4_PT_0->SetBinContent(25,20759.160196);
  S4_PT_0->SetBinContent(26,23873.0302254);
  S4_PT_0->SetBinContent(27,22316.1002107);
  S4_PT_0->SetBinContent(28,14012.4301323);
  S4_PT_0->SetBinContent(29,14531.4101372);
  S4_PT_0->SetBinContent(30,11936.5201127);
  S4_PT_0->SetBinContent(31,9860.6010931);
  S4_PT_0->SetBinContent(32,9860.6010931);
  S4_PT_0->SetBinContent(33,4151.8320392);
  S4_PT_0->SetBinContent(34,4151.8320392);
  S4_PT_0->SetBinContent(35,3632.8530343);
  S4_PT_0->SetBinContent(36,2594.8950245);
  S4_PT_0->SetBinContent(37,3113.8740294);
  S4_PT_0->SetBinContent(38,1556.9370147);
  S4_PT_0->SetBinContent(39,1556.9370147);
  S4_PT_0->SetBinContent(40,518.9790049);
  S4_PT_0->SetBinContent(41,13493.4501274); // overflow
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
