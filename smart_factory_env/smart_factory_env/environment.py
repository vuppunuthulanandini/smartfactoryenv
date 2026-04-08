# environment.py
from typing import Dict, Any

class SmartFactoryEnv:
    def __init__(self):
        self.reset()

    def reset(self) -> Dict[str, Any]:
        """Reset environment to initial state"""
        self.machines = {"M1": "idle", "M2": "idle", "M3": "idle"}
        self.machine_busy = {m: 0 for m in self.machines}  # cooldown counters
        self.inventory = {"raw": 10, "finished": 0}  # 10 raw materials
        self.step_count = 0
        return self.state()

    def state(self) -> Dict[str, Any]:
        """Return current state"""
        return {
            "machines": self.machines.copy(),
            "inventory": self.inventory.copy(),
            "step": self.step_count
        }

    def step(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an action in the environment"""
        machine = action.get("machine")
        task = action.get("task")
        reward = 0.0
        done = False

        # Process raw material if machine is idle and raw available
        if task == "process_raw" and self.inventory["raw"] > 0 and self.machine_busy[machine] == 0:
            self.inventory["raw"] -= 1
            self.inventory["finished"] += 1
            self.machine_busy[machine] = 2  # machine busy for 2 steps
            reward = 1.0

        # Decrease busy counters
        for m in self.machines:
            if self.machine_busy[m] > 0:
                self.machine_busy[m] -= 1

        # Update machine states
        for m in self.machines:
            self.machines[m] = "busy" if self.machine_busy[m] > 0 else "idle"

        self.step_count += 1

        # Done if max steps or no raw materials
        if self.step_count >= 20 or self.inventory["raw"] == 0:
            done = True

        return {"state": self.state(), "reward": reward, "done": done}