#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:53:06 2024

@author: tusharpirwani
"""
from maze_converter import read_maze, check_walls, convert_cell, convert_maze, display_maze

# 1. Black Box Test for read_maze
def test_read_maze():
    # Create a sample maze file for testing
    test_maze = [
        "+---+",
        "|   |",
        "+-+-+"
    ]
    with open("test_maze.txt", "w") as f:
        for line in test_maze:
            f.write(line + "\n")
    
    # Now test reading the maze from the file
    maze = read_maze("test_maze.txt")
    expected = [
        "+---+",
        "|   |",
        "+-+-+"
    ]
    
    assert maze == expected, f"Expected {expected}, but got {maze}"


# 2. White Box Test for check_walls
def test_check_walls():
    maze = [
        "+---+",
        "|   |",
        "+---+"
    ]
    
    # Test 1: Top-left corner (0, 0)
    actual = check_walls(maze, 0, 0)
    expected = (False, True, False, True)  # No left wall, but there is a right and bottom wall
    assert expected == actual, "Top-left corner"

    
    # Test 2: Top-right corner (4, 0)
    actual = check_walls(maze, 4, 0)
    expected = (True, False, False, True)  # Wall to the left, no wall to the right, wall below
    assert expected == actual, "Top-right corner"

    # Test 3: Bottom-left corner (0, 2)
    actual = check_walls(maze, 0, 2)
    expected = (False, True, True, False)  # No wall to the left, wall to the right, wall above
    assert expected == actual, "Bottom-left corner"

    # Test 4: Bottom-right corner (4, 2)
    actual = check_walls(maze, 4, 2)
    expected = (True, False, True, False)  # Wall to the left, no wall to the right, wall above
    assert expected == actual, "Bottom-right corner"

    
    
# 3. White Box Test for convert_cell
def test_convert_cell():
    
    maze_lines = [
        "+---+",
        "|   |",
        "+-+-+"
    ]
    # Test 2 for specific cell (4, 1) with walls on top and bottom
    result = convert_cell(maze_lines, 4, 1)
    expected = '│'   # Expected vertical wall character
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test 2: Top-left corner (0, 0) with top and left walls, no right or bottom walls
    result = convert_cell(maze_lines, 0, 0)
    expected = '┌'   # Expected top-left corner character
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test 3: Bottom-left corner (0, 2) with left and bottom walls, no right or top walls
    result = convert_cell(maze_lines, 0, 2)
    expected = '└'   # Expected bottom-left corner character
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test 4: Top-right corner (4, 0) with top and right walls, no left or bottom walls
    result = convert_cell(maze_lines, 4, 0)
    expected = '┐'   # Expected top-right corner character
    assert result == expected, f"Expected {expected}, but got {result}"

# 4. Black Box Test for convert_cell
def test_convert_maze():
    maze = [
        "+---+",
        "|   |",
        "+---+"
    ]
    
    # Test 1: Convert Entire Maze
    actual = convert_maze(maze)
    expected = [
        '┌───┐', 
        '│   │', 
        '└───┘'
     ]

    assert expected == actual, "Convert entire maze"
    

        
        
if __name__ == "__main__":
    test_read_maze()
    test_check_walls()
    test_convert_cell()
    test_convert_maze()
    
    

        

