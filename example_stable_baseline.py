import gym

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor


# Create environment
env = gym.make('LunarLander-v2')
env = Monitor(env)

# # Instantiate the agent
model = DQN('MlpPolicy', env, learning_rate=1e-3, verbose=1)
# # Train the agent
# model.learn(total_timesteps=int(2e5))
# # Save the agent
# model.save("dqn_lunar")
# del model  # delete trained model to demonstrate loading
#
# # Load the trained agent
# model = DQN.load("dqn_lunar")

# Evaluate the agent
# mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    print(info)
    env.render()
