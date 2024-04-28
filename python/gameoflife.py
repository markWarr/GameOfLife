import argparse
import numpy as np
import matplotlib.animation as animation
from matplotlib import pyplot as plt

ON = 255
OFF = 0
vals = [ON, OFF]


def random_grid(N):
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def add_glider(i, j, grid):
    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i + 3, j:j + 3] = glider


def update(frame_num, img, grid, N):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img


def main():
    parser = argparse.ArgumentParser(description="Game of Life")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    updateinterval = 50
    if args.interval:
        updateinterval = int(args.interval)

    # declare grid
    if args.glider:
        grid = np.zeros(N * N).reshape(N, N)
        add_glider(1, 1, grid)
    else:
        grid = random_grid(N)

    # set up the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, frames=10, fargs=(img, grid, N,),
                                  interval=updateinterval, save_count=50
                                  )
    if args.movfile:
        ani.save(args.movfile, fps=30)
    plt.show()


if __name__ == '__main__':
    main()
