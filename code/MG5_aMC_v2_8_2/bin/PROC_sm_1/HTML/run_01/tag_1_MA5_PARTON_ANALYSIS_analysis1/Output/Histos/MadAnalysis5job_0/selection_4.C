void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo63","canvas_plotflow_tempo63",0,0,700,500);
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
  S5_ETA_0->SetBinContent(7,1011.8919768);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,505.9459884);
  S5_ETA_0->SetBinContent(10,6577.2978492);
  S5_ETA_0->SetBinContent(11,12648.64971);
  S5_ETA_0->SetBinContent(12,26815.1393852);
  S5_ETA_0->SetBinContent(13,74880.0082832);
  S5_ETA_0->SetBinContent(14,149759.996566);
  S5_ETA_0->SetBinContent(15,249431.394281);
  S5_ETA_0->SetBinContent(16,347584.892031);
  S5_ETA_0->SetBinContent(17,430560.090128);
  S5_ETA_0->SetBinContent(18,421958.990326);
  S5_ETA_0->SetBinContent(19,408298.390639);
  S5_ETA_0->SetBinContent(20,403744.890743);
  S5_ETA_0->SetBinContent(21,391096.291033);
  S5_ETA_0->SetBinContent(22,410322.190592);
  S5_ETA_0->SetBinContent(23,440678.989896);
  S5_ETA_0->SetBinContent(24,420441.09036);
  S5_ETA_0->SetBinContent(25,339995.692205);
  S5_ETA_0->SetBinContent(26,240830.294478);
  S5_ETA_0->SetBinContent(27,152795.696497);
  S5_ETA_0->SetBinContent(28,71338.3883644);
  S5_ETA_0->SetBinContent(29,35416.219188);
  S5_ETA_0->SetBinContent(30,15178.379652);
  S5_ETA_0->SetBinContent(31,3541.6219188);
  S5_ETA_0->SetBinContent(32,3541.6219188);
  S5_ETA_0->SetBinContent(33,0.0);
  S5_ETA_0->SetBinContent(34,505.9459884);
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
  THStack* stack = new THStack("mystack_64","mystack");
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
