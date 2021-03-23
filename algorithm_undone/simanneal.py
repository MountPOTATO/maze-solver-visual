import time
from collections import deque
import heapq

xd=[1,0,0,-1]
yd=[0,1,-1,0]
# 单元格类型
# 0 - 路，1 - 墙，2-走过的路，4-死胡同
class CellType:
    ROAD = 0
    WALL = 1
    WALKED = 2
    DEAD = 3
    BFS_QUEUE=4
# 墙的方向
class Direction:
    LEFT = 0,
    UP = 1,
    RIGHT = 2,
    DOWN = 3,

class block:
    def __init__(self,pos):
        self.coord=pos
        self.g=0
        self.h=0
    def __lt__(self,rhs):
        return self.g+self.h<rhs.g+rhs.h

def f(block):
    return block.g+block.h
def mahattan(pos,end):
    return abs(pos[1]-end[1])+abs(pos[0]-end[0])

def mark_walked(maze, pos):
    maze[pos[0]][pos[1]] = CellType.WALKED

def mark_bfs(maze,pos):
    maze[pos[0]][pos[1]] = CellType.BFS_QUEUE

def mark_dead(maze, pos):
    maze[pos[0]][pos[1]] = CellType.DEAD

def mark_final(maze,pos):
    maze[pos[0]][pos[1]] = CellType.LAST

def manhattan(pos,end):
    return abs(end[0]-pos[0])+abs(end[1]-pos[1])

def out_of_range(num,x,y):
    return x==-1 or x==num or y==-1 or y==num