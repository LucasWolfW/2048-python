import random
import constants as c

def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix

def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat


def game_state(mat):

    # check for win cell
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
            
    # check for any zero entries
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
            
    # check for same cells that touch each other
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
            
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
        
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
        
    return 'lose'

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new

def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

def cover_up(mat, grid_len):
    new = []
    for j in range(grid_len):
        partial_new = []
        for i in range(grid_len):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(grid_len):
        count = 0
        for j in range(grid_len):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done

def merge(mat, done, grid_len):
    for i in range(grid_len):
        for j in range(grid_len-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done

def up(game):
    print("up")
    grid_len = len(game)
    game = transpose(game)
    game, done = cover_up(game, grid_len)
    game, done = merge(game, done, grid_len)
    game = cover_up(game, grid_len)[0]
    game = transpose(game)
    return game, done

def down(game):
    print("down")
    grid_len = len(game)
    game = reverse(transpose(game))
    game, done = cover_up(game, grid_len)
    game, done = merge(game, done, grid_len)
    game = cover_up(game, grid_len)[0]
    game = transpose(reverse(game))
    return game, done

def left(game):
    print("left")
    grid_len = len(game)
    game, done = cover_up(game, grid_len)
    game, done = merge(game, done, grid_len)
    game = cover_up(game, grid_len)[0]
    return game, done

def right(game):
    print("right")
    grid_len = len(game)
    game = reverse(game)
    game, done = cover_up(game, grid_len)
    game, done = merge(game, done, grid_len)
    game = cover_up(game, grid_len)[0]
    game = reverse(game)
    return game, done