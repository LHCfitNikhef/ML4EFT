CXX = g++
CXXFLAGS = -w -O2 -std=c++11 -pedantic -Wall -Wshadow -fPIC -pthread
INCLUDES = -I/data/theorie/pherbsch/ML4EFT/packages/pythia8308/include -I/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/include 
LIBS = -L/data/theorie/pherbsch/ML4EFT/packages/pythia8308/lib -L/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -lRecursiveTools
RPATH = -Wl,-rpath,/data/theorie/pherbsch/ML4EFT/packages/pythia8308/lib -Wl,-rpath,/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib
LDLIBS = -lpythia8 -ldl -lfastjet -lz -lfastjettools

TARGET = clean_shower_MPI_ISR

.PHONY: all clean

all: $(TARGET)

$(TARGET): clean_shower_MPI_ISR.cc
	$(CXX) $(CXXFLAGS) $(INCLUDES) $< -o $@ $(LIBS) $(RPATH) $(LDLIBS)

clean:
	rm -f $(TARGET)
