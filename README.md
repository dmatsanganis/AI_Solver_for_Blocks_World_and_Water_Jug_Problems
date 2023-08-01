# AI Solver for Blocks World and Water Jug Problems

This repository contains a Python program to solve two classic AI problems: the Blocks World problem and the Water Jug problem, using the A* search algorithm.

## Blocks World Problem

The Blocks World problem involves rearranging stacks of blocks to match a certain goal configuration. The user is prompted to input the initial and goal states, and the A* algorithm generates a sequence of moves to reach the goal state. The heuristic used is based on the number of blocks in incorrect positions and the blocks that are not placed correctly below other blocks.

## Water Jug Problem

The Water Jug problem involves two jugs with certain capacities and an infinite water supply. The goal is to measure a specific amount of water, given that the jugs can be filled and emptied but not partially filled. The user inputs the capacities of the two jugs and the desired final amount of water in each jug. The A* algorithm then finds the sequence of actions (e.g., fill jug 1, empty jug 2) required to reach the goal state. The heuristic used is the sum of the absolute differences between the current and goal amounts of water in each jug.

## Contributors

- [x] [Dimitris Matsanganis](https://github.com/dmatsanganis)


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
