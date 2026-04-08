
# Smart Factory Environment

## Overview
This is a Reinforcement Learning (RL) environment simulating a smart factory.  
- 3 machines (M1, M2, M3) process raw materials into finished goods.  
- Each machine has a 2-step cooldown.  
- Agent receives a reward of 1.0 for each successfully processed raw material.  
- Total raw materials: 10 per episode.

## Action Space
```python
{
    "machine": "M1" | "M2" | "M3",
    "task": "process_raw"
}