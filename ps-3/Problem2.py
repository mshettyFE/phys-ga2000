import numpy as np
import matplotlib.pyplot as plt

initial_atoms = 10000
total_time_steps = 20000

# All decays are in seconds
PbBiDecay = 3.3*60
TlPBDecay = 2.2*60
BiDecay  = 46*60

# Probability of taking each branch
BiTlProb = .0209;
BiPbProb = 1-BiTlProb;

def genProbability(t, lifetime):
    return 1- np.power(2, -t/lifetime)

def ReactionSeriesStep():
# Unstable_Bi = 1
# Tl = 2
# Pb = 3
# Stable_Bi = 4
    unstable_bi_agg = []
    tl_agg = []
    pb_agg = []
    stable_bi_agg = []
    
    state = np.full(initial_atoms, 1)

    for t_step in np.arange(total_time_steps):
        transitions = np.random.uniform(size=state.shape)
# First, do Pb to Stable_Bi
# Figure out which elements need to transition
        lead = np.where(state == 3, True, False)
        need_to_decay = np.where(transitions < genProbability(t_step, PbBiDecay), True , False)
# Transition those elements to Stable Bi
        state[lead & need_to_decay] = 4

# Repeat for Tl
        thallium = np.where(state == 2, True, False)
        need_to_decay = np.where(transitions < genProbability(t_step, TlPBDecay), True , False)
# Transition those elements to Pb
        state[thallium & need_to_decay] = 3

# For unstable bi, need to take into account that you have two branches with a different probability
        unstable_bi = np.where(state == 1, True, False)
        need_to_decay = np.where(transitions < genProbability(t_step, BiDecay), True , False)
# Roll the dice again to see what the new state is, copying over unchanged values
        new_state = np.random.choice([2,3], size = state.shape, p = [BiTlProb, BiPbProb]) 
        state = np.where(unstable_bi & need_to_decay, new_state, state)

        new_unstable = np.sum(state==1)
        new_tl = np.sum(state==2)
        new_pb = np.sum(state==3)
        new_stable = np.sum(state==4)

        unstable_bi_agg.append(new_unstable)
        tl_agg.append(new_tl)
        pb_agg.append(new_pb)
        stable_bi_agg.append(new_stable)
    return np.arange(total_time_steps) , np.array(unstable_bi_agg), np.array(tl_agg), np.array(pb_agg), np.array(stable_bi_agg)

if __name__ == "__main__":
    time, unstable, tl, pb, stable = ReactionSeriesStep()
    plt.plot(time, unstable, label ="Unstable Bi")
    plt.plot(time, pb, label = "Pb")
    plt.plot(time, tl, label = "Tl")
    plt.plot(time, stable, label = "Stable Bi")
#    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    plt.show()
