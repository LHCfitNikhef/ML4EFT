#ifndef analysis_user_h
#define analysis_user_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class user : public AnalyzerBase
{
  INIT_ANALYSIS(user,"MadAnalysis5job")

 public : 
  virtual MAbool Initialize(const MA5::Configuration& cfg,
                          const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual MAbool Execute(SampleFormat& sample, const EventFormat& event);

 private : 
  // Declaring particle containers
  std::vector<const MCParticleFormat*> _P_t_t_I1I_PTorderingfinalstate_REG_;
  std::vector<const MCParticleFormat*> _P_t_I1I_PTorderingfinalstate_REG_;
  std::vector<const MCParticleFormat*> _P_t_tPTorderingfinalstate_REG_;
  MAbool isP__t_tPTorderingfinalstate(const MCParticleFormat* part) const {
     if ( part==0 ) return false;
     if ( !PHYSICS->Id->IsFinalState(part) ) return false;
     if ( (part->pdgid()!=-6) ) return false;
     return true; }
  std::vector<const MCParticleFormat*> _P_tPTorderingfinalstate_REG_;
  MAbool isP__tPTorderingfinalstate(const MCParticleFormat* part) const {
     if ( part==0 ) return false;
     if ( !PHYSICS->Id->IsFinalState(part) ) return false;
     if ( (part->pdgid()!=6) ) return false;
     return true; }
};
}

#endif