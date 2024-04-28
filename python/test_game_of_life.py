import pytest
import gameoflife


def test_random_grid_returns_correct_small_grid_size():
    grid = gameoflife.random_grid(5)
    assert len(grid) == 5


def test_random_grid_returns_correct_medium_grid_size():
    grid = gameoflife.random_grid(50)
    assert len(grid) == 50


def test_random_grid_returns_correct_large_grid_size():
    grid = gameoflife.random_grid(500)
    assert len(grid) == 500


def test_glider_added_to_grid():
    grid = gameoflife.random_grid(500)
    gameoflife.add_glider(1, 1, grid)
    assert grid[4, 3] == 255
