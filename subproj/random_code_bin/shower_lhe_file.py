import pythia8
import numpy as np

# Initialize Pythia 8
pythia = pythia8.Pythia()

# Read LHE file
with open("/data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/unweighted_events_copy.lhe", "r") as f:
    event_text = f.read()

# Load LHE events into Pythia 8
pythia.readString("Beams:frameType = 4")
pythia.readString("Beams:LHEF = events.lhe")
pythia.init()

# Shower events
event_data = []
for iEvent in range(pythia.info.nSelected()):
    pythia.next()
    event = []
    for i in range(pythia.event.size()):
        particle = pythia.event[i]
        if particle.isFinal():
            event.append([particle.id(), particle.px(), particle.py(), particle.pz(), particle.e()])
    event_data.append(np.array(event))

# Write showerd events to file
with open("showered_events.dat", "w") as f:
    for event in event_data:
        for particle in event:
            f.write("{} {} {} {} {}\n".format(*particle))
        f.write("\n")