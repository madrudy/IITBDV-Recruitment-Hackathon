
'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Cone: {"x": float, "y": float, "side": "left" | "right", "index": int}
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"}  
# CmdFeedback: {"throttle", "steer"}        

# ─── PLANNER ──────────────────────────────────────────────────────────────────
import numpy as np

def plan(cones: list[dict]) -> list[dict]:
    """
    Generate a path from the cone layout.
    Called ONCE before the simulation starts.

    Args:
        cones: List of cone dicts with keys x, y, side ("left"/"right"), index

    Returns:
        path: List of waypoints [{"x": float, "y": float}, ...]
              Ordered from start to finish.
    
    Tip: Try midline interpolation between matched left/right cones.
         You can also compute a curvature-optimised racing line.
    """
    path = []
    # TODO: implement your path planning here

    blue = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "left"])
    yellow = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "right"])
    
    # n = min(len(blue), len(yellow))
    # for i in range (n):
    #     mid_x = (blue[i][0] + yellow[i][0]) / 2
    #     mid_y = (blue[i][1] + yellow[i][1]) / 2
    #     path.append({"x": float(mid_x), "y": float(mid_y)})

    for b in blue:
        closest_dist = float("Inf") 
        closest_y = None

        for y in yellow:
            dx = b[0] - y[0]
            dy = b[1] - y[1]
            dist = dx*dx + dy*dy
            if dist < closest_dist:
                closest_dist = dist
                closest_y = y
    
        mid_x = (b[0] + closest_y[0]) / 2
        mid_y = (b[1] + closest_y[1]) / 2

        path.append({"x": float(mid_x), "y": float(mid_y)})
    
    return path
    # implement a planning algorithm to generate a path from the blue and yellow cones








    return path

