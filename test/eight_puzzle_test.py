import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithm.astar import Puzzle  # Import functions from your algorithm


def test_correct_case_1():
    # In this test, we will test whether the algorithm can give the correct answer when inital state is goal
    goal = (1, 3, 5, 7, 0, 2, 6, 8, 4)
    initial = goal
    solver = Puzzle(initial, goal)
    res = solver.astar()
    assert res == 0

def test_correct_case_2():
    # In this test, we will test whether the algorithm can give the correct answer in a simple case
    goal = (1, 3, 5, 7, 0, 2, 6, 8, 4)
    initial = (1, 3, 5, 0, 7, 2, 6, 8, 4)
    solver = Puzzle(initial, goal)
    res = solver.astar()
    assert res == 1

def test_correct_case_3():
    # In this test, we will test whether the algorithm can give the correct answer in a complex case
    goal = (1, 3, 5, 7, 0, 2, 6, 8, 4)
    initial = (7, 1, 5, 0, 3, 2, 6, 8, 4)
    solver = Puzzle(initial, goal)
    res = solver.astar()
    assert res == 4

def test_insolvable_case():
    # In this test, we will test whether the algorithm can find the insolvability of the puzzle
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    initial = (1, 2, 3, 4, 5, 6, 0, 8, 7) # This is an insolvable case
    solver = Puzzle(initial, goal)
    res = solver.astar()
    assert res == None
