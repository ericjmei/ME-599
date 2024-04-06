import gymnasium as gym
import pygame
import sys

# env = gym.make('CartPole-v1',render_mode="human")
# env = gym.make("FrozenLake-v1",render_mode="human", is_slippery=True)

## from part 2, when I looked up my own environments
# env = gym.make("Taxi-v3",render_mode="human")
env = gym.make("MountainCar-v0")

observation, info = env.reset()

for i in range(1000000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    print(f"{i}: {action}, {observation}, {reward}")

    if terminated or truncated:
        observation, info = env.reset()

# sys.exit()
env.close()