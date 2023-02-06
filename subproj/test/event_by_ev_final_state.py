import pandas as pd
import pyhepmc
import numpy as np
import cachetools.func
from particle import Particle
from particle.particle.particle import ParticleNotFound
import time
import pid_func

event_file = "/data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/tag_1_pythia8_events.hepmc"


def read_particles(hepmc_file):
    final_state_particles = []
    events = []
    event_num = 0
    with pyhepmc.open(event_file) as f:
        event = f.read()
        # print(event)
        while event is not None:
            import pdb; pdb.set_trace()
            final_state_particles = [p for p in event.particles if p.status == 1]
            events.append((final_state_particles))
            event = f.read()
    return events

events = read_particles(event_file)


final_state_particles= read_particles(event_file)
energies_squared = []
event = events[0]
final_state_particles = event
energy_sum = 0
for particle in final_state_particles:
    energy_sum += particle.momentum.e
energy_sum_squared = energy_sum


print("Energies squared for each event:", energy_sum_squared)
