import os
import collections
import pickle
import shutil
import csv
import gym
import numpy as np
import time
from stable_baselines import PPO2
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines.common.vec_env.vec_normalize import VecNormalize
import wandb
from tensorflow import flags
import driving_envs
env = gym.make("Navigation-v0")
# for i in range(10):
observation=env.reset()
print(observation)
for t in range(200):
    env.render()
    print(env.step([0.1,0.5]))
env.close()