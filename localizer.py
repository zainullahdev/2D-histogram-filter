import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    #
    # TODO - implement this in part 2
    #
    rows = len(beliefs)
    cols = len(beliefs[0])
    
    new_beliefs = beliefs
    sum_all_values = 0
    
    for row_idx in range(rows):
        for col_idx in range(cols):
            if grid[row_idx][col_idx] == color:
                new_beliefs[row_idx][col_idx] = (p_hit * beliefs[row_idx][col_idx]) / 100
            else:
                new_beliefs[row_idx][col_idx] = (p_miss * beliefs[row_idx][col_idx]) / 100
            sum_all_values += new_beliefs[row_idx][col_idx]
    
    #normalize
    for row_idx in range(rows):
        for col_idx in range(cols):
            new_beliefs[row_idx][col_idx] = new_beliefs[row_idx][col_idx] / sum_all_values

    return new_beliefs 

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    #print(height,width)
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #print(row,cell)
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)