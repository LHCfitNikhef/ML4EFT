void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo81","canvas_plotflow_tempo81",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",40,-10.0,10.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,504.1709904);
  S5_ETA_0->SetBinContent(10,4537.5389136);
  S5_ETA_0->SetBinContent(11,19158.4996352);
  S5_ETA_0->SetBinContent(12,36804.4792992);
  S5_ETA_0->SetBinContent(13,79659.0184832);
  S5_ETA_0->SetBinContent(14,122009.397677);
  S5_ETA_0->SetBinContent(15,238976.99545);
  S5_ETA_0->SetBinContent(16,365019.79305);
  S5_ETA_0->SetBinContent(17,417957.792042);
  S5_ETA_0->SetBinContent(18,444678.791533);
  S5_ETA_0->SetBinContent(19,419974.392003);
  S5_ETA_0->SetBinContent(20,383169.992704);
  S5_ETA_0->SetBinContent(21,384682.492675);
  S5_ETA_0->SetBinContent(22,422495.291955);
  S5_ETA_0->SetBinContent(23,424007.791926);
  S5_ETA_0->SetBinContent(24,408882.692214);
  S5_ETA_0->SetBinContent(25,334265.393635);
  S5_ETA_0->SetBinContent(26,251077.195219);
  S5_ETA_0->SetBinContent(27,153267.997082);
  S5_ETA_0->SetBinContent(28,80667.358464);
  S5_ETA_0->SetBinContent(29,26721.0594912);
  S5_ETA_0->SetBinContent(30,15125.129712);
  S5_ETA_0->SetBinContent(31,3529.1969328);
  S5_ETA_0->SetBinContent(32,2016.6839616);
  S5_ETA_0->SetBinContent(33,2016.6839616);
  S5_ETA_0->SetBinContent(34,504.1709904);
  S5_ETA_0->SetBinContent(35,0.0);
  S5_ETA_0->SetBinContent(36,0.0);
  S5_ETA_0->SetBinContent(37,0.0);
  S5_ETA_0->SetBinContent(38,0.0);
  S5_ETA_0->SetBinContent(39,0.0);
  S5_ETA_0->SetBinContent(40,0.0);
  S5_ETA_0->SetBinContent(41,0.0); // overflow
  S5_ETA_0->SetEntries(10000);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_82","mystack");
  stack->Add(S5_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ t~_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
