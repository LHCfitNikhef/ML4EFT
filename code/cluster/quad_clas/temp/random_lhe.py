import pylhe
import numpy as np
import time


def invariant_mass(p1, p2):
    return np.sqrt(
        sum((1 if mu == 'e' else -1) * (getattr(p1, mu) + getattr(p2, mu)) ** 2 for mu in ['e', 'px', 'py', 'pz']))


def load_data(path, n, s):
    """ Load a subset of size s from n events from the lhe file.

    Parameters
    ----------
    path: str
        Path to lhe file
    n: int
        total size of the dataset
    s:
        size of the subset
    Returns
    -------
    event_data: ndarray
        The loaded subset of events
    """

    skip = np.random.choice(n, n - s, replace=False)
    event_seq = pylhe.readLHE(path)

    event_data = []

    start = time.perf_counter()
    for i in range(n):
        e = next(event_seq)
        if i not in skip:
            mtt = invariant_mass(e.particles[-1], e.particles[-2])
            event_data.append(mtt)
    event_data = np.array(event_data)
    end = time.perf_counter()
    print(f"Data loaded in {end - start:0.4f} seconds")
    return event_data


mtt = load_data('./unweighted_events.lhe', 10000, 100)





#
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
# seq = infinite_sequence()
# skip = np.random.randint(low=0, high=100, size=70)
# for i in range(100):
#     e = next(seq)
#     if i not in skip:
#         print(e)



# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# gen = pylhe.readLHE(path)
# event = next(gen)
# print(event.__dict__)
# print(next(gen))