void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo45","canvas_plotflow_tempo45",0,0,700,500);
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
  S5_ETA_0->SetBinContent(7,138.398423818);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,415.195271454);
  S5_ETA_0->SetBinContent(10,553.593695272);
  S5_ETA_0->SetBinContent(11,4013.55409076);
  S5_ETA_0->SetBinContent(12,8027.10838149);
  S5_ETA_0->SetBinContent(13,22558.9436822);
  S5_ETA_0->SetBinContent(14,39997.1424838);
  S5_ETA_0->SetBinContent(15,67123.2325523);
  S5_ETA_0->SetBinContent(16,93557.3357008);
  S5_ETA_0->SetBinContent(17,113071.467668);
  S5_ETA_0->SetBinContent(18,119022.676478);
  S5_ETA_0->SetBinContent(19,111410.772166);
  S5_ETA_0->SetBinContent(20,107120.358839);
  S5_ETA_0->SetBinContent(21,109611.502073);
  S5_ETA_0->SetBinContent(22,110857.149876);
  S5_ETA_0->SetBinContent(23,122482.618277);
  S5_ETA_0->SetBinContent(24,115285.861645);
  S5_ETA_0->SetBinContent(25,95910.1043066);
  S5_ETA_0->SetBinContent(26,65462.4570655);
  S5_ETA_0->SetBinContent(27,39997.1462831);
  S5_ETA_0->SetBinContent(28,21313.3520689);
  S5_ETA_0->SetBinContent(29,10241.4821628);
  S5_ETA_0->SetBinContent(30,2906.36710014);
  S5_ETA_0->SetBinContent(31,1522.38286196);
  S5_ETA_0->SetBinContent(32,276.796847636);
  S5_ETA_0->SetBinContent(33,0.0);
  S5_ETA_0->SetBinContent(34,0.0);
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
  THStack* stack = new THStack("mystack_46","mystack");
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
