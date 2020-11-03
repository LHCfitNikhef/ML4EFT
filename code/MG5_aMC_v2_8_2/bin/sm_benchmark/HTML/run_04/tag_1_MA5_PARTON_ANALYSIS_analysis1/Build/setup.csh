#!/bin/csh -f

# Defining colours for shell
set GREEN  = "\033[1;32m"
set RED    = "\033[1;31m"
set PINK   = "\033[1;35m"
set BLUE   = "\033[1;34m"
set YELLOW = "\033[1;33m"
set CYAN   = "\033[1;36m"
set NORMAL = "\033[0;39m"

# Configuring MA5 environment variable
setenv MA5_BASE /home/jaco/Documents/ML4EFT/code/MG5_aMC_v2.8.2/MG5_aMC_v2_8_2/HEPTools/madanalysis5/madanalysis5

# Configuring PATH environment variable
if ( $?PATH ) then
setenv PATH $MA5_BASE/tools/SampleAnalyzer/ExternalSymLink/Bin:$MA5_BASE/tools/fastjet/bin:"$PATH"
else
setenv PATH $MA5_BASE/tools/SampleAnalyzer/ExternalSymLink/Bin:$MA5_BASE/tools/fastjet/bin
endif

# Configuring LD_LIBRARY_PATH environment variable
if ( $?LD_LIBRARY_PATH ) then
setenv LD_LIBRARY_PATH $MA5_BASE/tools/SampleAnalyzer/Lib:$MA5_BASE/tools/SampleAnalyzer/ExternalSymLink/Lib:$MA5_BASE/tools/fastjet/lib:"$LD_LIBRARY_PATH"
else
setenv LD_LIBRARY_PATH $MA5_BASE/tools/SampleAnalyzer/Lib:$MA5_BASE/tools/SampleAnalyzer/ExternalSymLink/Lib:$MA5_BASE/tools/fastjet/lib
endif

# Checking that all environment variables are defined
if ( $?MA5_BASE && $?PATH && $?LD_LIBRARY_PATH ) then
echo $YELLOW"--------------------------------------------------------"
echo "    Your environment is properly configured for MA5     "
echo "--------------------------------------------------------"$NORMAL
endif
