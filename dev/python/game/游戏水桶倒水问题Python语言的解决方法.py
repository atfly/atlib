
#! /usr/bin/env python

# -*- coding: utf-8 -*-

LIMITS = (10, 7, 3)
INIT = (10, 0, 0)
WIN = (5, 5, 0)

from copy import copy

class State:
    def __init__(self, init_value):
        self.parent = -1
        self.value = init_value
        self.move = (0, 0, 0) #(from, to, amount)

    #spawn by put water around

    def spawn(self):

        for i in range(len(LIMITS)): #for each cup

            if not self.value[i]: continue #if empty cup then next

            for k in range(len(LIMITS)): #otherwise try put water to other cups
                if i == k: continue
                val_i = self.value[i]
                val_k = self.value[k]
                #1. move all in i to k
                #2. move i to make k full
                #so the minimum of the 2 actions is the target
                min_ik = min(val_i, LIMITS[k] - val_k)
                new_value = list(copy(self.value))
                new_value[i] -= min_ik
                new_value[k] += min_ik
                new_value = tuple(new_value)
                if new_value in g_state_map: #already exists?
                    continue
                new_state = State(new_value)
                new_state.parent = g_index
                new_state.move = (i, k, min_ik)
                g_states.append(new_state)
                g_state_map[new_value] = True
                if new_value == WIN:
                    return True
        return False

#www.iplaypy.com

def print_solution(state):
    states = []

    while state.parent != -1:
        states.append(state)
        state = g_states[state.parent]
    states.reverse()

    print "At least:", len(states), "steps:"

    print "(Cup0, Cup1, Cup2) (from, to, amount)"

    print INIT

    for state in states:
        print state.value, state.move

#solve the problem here!
g_states = [State(INIT)] #initially we have (10, 0, 0)
g_state_map = {} #sate:true/false, avoid duplicate states
g_index = 0

while g_index < len(g_states):
    state = g_states[g_index]

    if state.spawn():
        print_solution(g_states[-1])

        break

    g_index += 1

result = """

At least: 9 steps:

(Cup0, Cup1, Cup2) (from, to, amount)

(10, 0, 0)
(3, 7, 0) (0, 1, 7)
(3, 4, 3) (1, 2, 3)
(6, 4, 0) (2, 0, 3)
(6, 1, 3) (1, 2, 3)
(9, 1, 0) (2, 0, 3)
(9, 0, 1) (1, 2, 1)
(2, 7, 1) (0, 1, 7)
(2, 5, 3) (1, 2, 2)
(5, 5, 0) (2, 0, 3)
"""

