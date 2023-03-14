import pythia8

# Initialize Pythia
pythia = pythia8.Pythia()

# Set up the process
top_mass = 173.2 # GeV
anti_top_mass = 173.2 # GeV
pythia.readString("Top:gg2ttbar = on") # Set up gg -> ttbar process

pythia.settings.parm("Beams:idA", 21) # Set beam particles to gluons

pythia.settings.parm("Beams:idB", 21)

# Generate top quark
top_px = 100.0 # GeV
top_py = 0.0 # GeV
top_pz = 0.0 # GeV
top_E = (top_px**2 + top_py**2 + top_pz**2 + top_mass**2)**0.5
top_momentum = [top_E, top_px, top_py, top_pz]
pythia.event.append(6, 21, 0, 0, top_momentum[0], top_momentum[1], top_momentum[2], top_momentum[3], top_mass)

# Generate anti-top quark
anti_top_px = -100.0 # GeV
anti_top_py = 0.0 # GeV
anti_top_pz = 0.0 # GeV
anti_top_E = (anti_top_px**2 + anti_top_py**2 + anti_top_pz**2 + anti_top_mass**2)**0.5
anti_top_momentum = [anti_top_E, anti_top_px, anti_top_py, anti_top_pz]
pythia.event.append(-6, 21, 0, 0, anti_top_momentum[0], anti_top_momentum[1], anti_top_momentum[2], anti_top_momentum[3], anti_top_mass)

# Parton shower
pythia.init()
while pythia.next():
    if pythia.event.size() > 10000: # Stop once we have more than 2 particles in the event (i.e. after parton showering)
        break

# Print final state particles
print("Final state particles:")
for i in range(pythia.event.size()):
    particle = pythia.event[i]
    if particle.isFinal():
        print("Particle ID:", particle.id(), "px:", particle.px(), "py:", particle.py(), "pz:", particle.pz(), "E:", particle.e())
