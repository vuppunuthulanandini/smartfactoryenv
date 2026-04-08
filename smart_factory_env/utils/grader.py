# utils/grader.py
import random
from environment import SmartFactoryEnv

class SmartFactoryGrader:
    def __init__(self):
        self.env = SmartFactoryEnv()

    def grade_easy(self):
        """Easy: process raw material on one machine"""
        state = self.env.reset()
        total_reward = 0.0

        for _ in range(10):
            action = {"machine": "M1", "task": "process_raw"}
            result = self.env.step(action)
            total_reward += result["reward"]
            if result["done"]:
                break

        score = min(total_reward / 10.0, 1.0)
        return score

    def grade_medium(self):
        """Medium: rotate machines efficiently"""
        state = self.env.reset()
        total_reward = 0.0
        machines = list(state["machines"].keys())

        for step in range(20):
            available_machines = [m for m, s in state["machines"].items() if s == "idle"]
            if not available_machines:
                available_machines = machines
            action = {"machine": available_machines[step % len(available_machines)], "task": "process_raw"}
            result = self.env.step(action)
            state = result["state"]
            total_reward += result["reward"]
            if result["done"]:
                break

        score = min(total_reward / 20.0, 1.0)
        return score

    def grade_hard(self):
        """Hard: optimize production and machine usage"""
        state = self.env.reset()
        total_reward = 0.0
        machines = list(state["machines"].keys())

        for step in range(20):
            # Prioritize machines with least busy steps
            available_machines = sorted(
                [m for m, s in state["machines"].items() if s == "idle"],
                key=lambda x: random.random()  # need random for tie-breaking
            )
            if not available_machines:
                available_machines = machines
            action = {"machine": available_machines[0], "task": "process_raw"}
            result = self.env.step(action)
            state = result["state"]
            total_reward += result["reward"]
            if result["done"]:
                break

        score = min(total_reward / 20.0, 1.0)
        return score


if __name__ == "__main__":
    grader = SmartFactoryGrader()
    print("[START] Grading Results")
    print(f"[STEP] Easy Task Score: {grader.grade_easy()}")
    print(f"[STEP] Medium Task Score: {grader.grade_medium()}")
    print(f"[STEP] Hard Task Score: {grader.grade_hard()}")
    print("[END] Total Evaluation Complete")