"""
Given a boolean 2D matrix, find the number of islands.
A group of connected 1s forms an island.
Find the number of islands and there group

Author: Narendra L
Date: 21-7-2018
"""
from collections import deque


inp = [[1,1,0,0,0],
       [0,1,0,0,1],
       [1,0,0,1,1],
       [0,0,0,0,0],
       [1,0,1,0,1]]

len_y = len(inp)
len_x = len(inp[0])

visited = []

def get_siblings(x, y):
    """Return all neighbors af a given x and y coord"""
    out = [[x+1, y], [x+1, y], [x-1, y], [x, y-1],
            [x+1, y+1], [x+1, y-1], [x-1, y-1], [x-1, y+1]]


    def validity(x, y):
        """Checks if points are valid neighbors"""
        if x < 0 or x >= len_x:
            return False

        if y < 0 or y >= len_y:
            return False

        return True

    out = [c for c in out if validity(*c)]

    # return only if cell is valid
    return [co_ords for co_ords in out if co_ords and inp[co_ords[0]][co_ords[1]] == 1]


stack = deque()


def BFS(node):
    """Does Breadth first search traversal"""
    # If already visited then it will be part of connected cell
    # or invalid
    if node in visited:
        return

    # put it in queue
    stack.append(node)
    lands = []

    while len(stack):
        cnode = stack.pop()

        if cnode in visited:
            continue

        lands.append(cnode)
        siblings = get_siblings(*cnode)
        siblings = [s for s in siblings if s not in visited]

        # update queue with siblings
        visited.append(cnode)
        stack.extend(siblings)

    return lands


def main():
    islands_ = [BFS([xx, yy]) for xx in range(len_x) for yy in range(len_y) if inp[xx][yy] == 1]
    # filter empty islands
    return [i for i in islands_ if i]


# MAIN CALL
islands = main()

print 'Number of islands are = ', len(islands)
for i, v in enumerate(islands): print "Island {}: {}".format(i+1, v)

