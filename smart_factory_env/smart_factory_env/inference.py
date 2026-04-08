
# inference.py
import random
from environment import SmartFactoryEnv

def run_baseline():
    env = SmartFactoryEnv()
    state = env.reset()
    total_reward = 0.0

    machines = list(state["machines"].keys())
    print("[START] Running baseline agent")

    for _ in range(20):
        # Choose only idle machines
        available_machines = [m for m, s in state["machines"].items() if s == "idle"]
        if not available_machines:
            available_machines = machines  # fallback

        action = {"machine": random.choice(available_machines), "task": "process_raw"}
        result = env.step(action)
        state = result["state"]
        total_reward += result["reward"]

        print(f"[STEP] action={action}, reward={result['reward']}, state={state}")
        if result["done"]:
            break

    print(f"[END] Total reward: {total_reward}")

if __name__ == "__main__":
    run_baseline()