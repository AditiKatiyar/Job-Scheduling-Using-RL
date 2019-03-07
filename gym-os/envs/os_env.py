import gym
from gym import error, spaces, utils
from gym.utils import seeding

from process import *
import numpy as np
 
class OSEnv(gym.Env):  
    metadata = {'render.modes': ['human']} 

    

    def __init__(self):
    	'''
		randomly creates processes with all the parameters randomly initialized.
    	'''
    	self.NUMBER_OF_PROCESSES = 10
	    self.BURST_TIME_SEED = 5
	    self.ARRIVAL_TIME_SEED = 5


	    self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(-high, high, dtype=np.float32)

	    self.seed()
	    self.reset()
 
    def step(self, action):
        pass
 
    def reset(self):
        self.processes = []
    	for ix in range(0, NUMBER_OF_PROCESSES):
    		a = np.random.randint(ARRIVAL_TIME_SEED)
    		b = np.random.randint(BURST_TIME_SEED)
    		p = Process(a, b)
    		self.processes.append(p)
 
    def render(self, mode='human', close=False):
    	for ix in range(0, NUMBER_OF_PROCESSES):
    		print("P", ix, " : ", p.arrival_time, "\t", p.burst_time, "\t", p.is_complete)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]