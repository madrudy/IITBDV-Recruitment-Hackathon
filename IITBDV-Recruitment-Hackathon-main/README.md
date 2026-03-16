# PPC Driverless Hackathon Submission

## Overview

This repository contains my solution for the **PPC (Planning and Path Control) task** in the Driverless Hackathon.

The goal of the task is to control a simulated Formula Student Driverless car so that it can drive through a track marked by **left and right cones**. The car must plan a path between the cones and follow it while maintaining speed and stability.

The implementation consists of two main parts:

* **Path Planning** – generating a centerline path from the cone layout
* **Control** – steering and speed control to follow the path

The simulator handles the vehicle physics while this code controls how the car decides where to go.

---

## Path Planning

The planner generates a path using the positions of the cones.

Steps used:

1. Separate the cones into **left (blue)** and **right (yellow)** sets.
2. For each left cone, find the **nearest right cone**.
3. Compute the **midpoint between the pair**.
4. Store these midpoints as waypoints that form the centerline of the track.

These waypoints represent the path that the vehicle tries to follow.

This approach works well when cones are not perfectly aligned and avoids relying on the ordering of the cones.

---

## Vehicle Control

The controller is responsible for steering the vehicle and controlling its speed.

### Steering

Steering is calculated using the direction from the vehicle to a **lookahead waypoint** on the planned path.

Steps:

1. Choose a waypoint slightly ahead on the path.
2. Compute the angle from the vehicle to that waypoint.
3. Compare it with the vehicle's current heading.
4. Adjust the steering angle based on the difference.

The steering value is limited to the maximum steering angle allowed by the simulator.

### Throttle and Brake

Speed control is implemented using a simple rule:

* If the current speed is **below the target speed**, apply throttle.
* If the current speed **exceeds the target speed**, apply braking.

This keeps the vehicle moving at a roughly constant speed during the lap.

---

## Files

```
planner.py      Generates the centerline path from cones
controller.py   Controls steering, throttle, and braking
run.py          Runs the simulator (provided by organizers)
```

Only `planner.py` and `controller.py` were modified as required by the challenge rules.

---

## How to Run

1. Navigate to the simulator directory.
2. Run the simulation:

```
py run.py
```

The simulator will load the track, generate the path using `planner.py`, and then repeatedly call the controller to drive the vehicle.

---

## Notes

This implementation focuses on a **simple and robust baseline approach** for path planning and control. More advanced methods such as spline smoothing, racing line optimization, or model predictive control could further improve lap time and stability.

---

## Author

Hackathon participant submission for the Driverless PPC challenge.
