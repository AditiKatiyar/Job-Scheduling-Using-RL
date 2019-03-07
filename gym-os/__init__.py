from gym.envs.registration import register
 
register(id='OS-v0', 
    entry_point='gym_os.envs:OSEnv', 
)