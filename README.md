# Conway's Game of Life

A compact, from-scratch implementation of Conway's Game of Life in Python, using Pyglet for
real-time rendering.

This is one of several small, self-contained programs I've written to explore ideas that
interested me outside of coursework — others include a Monte Carlo estimator for π and a
"colliding pool balls" simulation modeling conservation of momentum (also built with Pyglet).

## How it works

- The board is a 2D grid (`N x N`) with **toroidal (wrap-around) boundary conditions** — cells on
  the edge of the grid treat the opposite edge as their neighbor, implemented via modulo indexing.
- Each generation:
  1. `calculate_mask()` counts each cell's live neighbors (8-neighborhood).
  2. `apply_mask()` applies the standard Game of Life rules: a dead cell with exactly 3 live
     neighbors becomes alive; a live cell with fewer than 2 or more than 3 live neighbors dies.
- Rendering is handled with `pyglet.shapes.Rectangle` objects batched for efficient drawing, and
  the simulation advances on a fixed timer via `pyglet.clock.schedule_interval`.
- The starting pattern is a small glider-like seed set directly in code — easy to swap out for any
  other initial configuration.

## Running it

```bash
pip install pyglet
python GameOfLife.py
```

Opens a window and runs the simulation continuously, updating every 0.1 seconds.
