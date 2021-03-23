'''
Author: your name
Date: 2021-03-21 23:52:53
LastEditTime: 2021-03-23 12:01:39
LastEditors: your name
Description: In User Settings Edit
FilePath: \game-maze-master\hillclimbing.py
'''
import time
from collections import deque
import heapq

class CellType:
    ROAD = 0
    WALL = 1
    WALKED = 2
    DEAD = 3
    BFS_QUEUE=4
    LAST=5
# 墙的方向
class Direction:
    LEFT = 0,
    UP = 1,
    RIGHT = 2,
    DOWN = 3,

def mark_walked(maze, pos):
    maze[pos[0]][pos[1]] = CellType.WALKED

def mark_bfs(maze,pos):
    maze[pos[0]][pos[1]] = CellType.BFS_QUEUE

def mark_dead(maze, pos):
    maze[pos[0]][pos[1]] = CellType.DEAD
def manhattan(pos,end):
    return abs(end[0]-pos[0])+abs(end[1]-pos[1])

def out_of_range(num,x,y):
    return x==-1 or x==num or y==-1 or y==num

def get_neigbor(maze,pos,end):
    arr=[]
    if maze[pos[0]+1][pos[1]]==CellType.ROAD:
        heapq.heappush(arr,(-manhattan([pos[0]+1,pos[1]],end),[pos[0]+1,pos[1]]))
    if maze[pos[0]-1][pos[1]]==CellType.ROAD:
        heapq.heappush(arr,(-manhattan([pos[0]-1,pos[1]],end),[pos[0]-1,pos[1]]))
    if maze[pos[0]][pos[1]+1]==CellType.ROAD:
        heapq.heappush(arr,(-manhattan([pos[0],pos[1]+1],end),[pos[0],pos[1]+1]))
    if maze[pos[0]][pos[1]-1]==CellType.ROAD:
        heapq.heappush(arr,(-manhattan([pos[0],pos[1]-1],end),[pos[0],pos[1]-1]))
    return arr




def hill_climbing_solve(maze, pos, end, callback):

    time.sleep(0.3)
    stack=deque()
    stack.append(pos)

    while(len(stack)!=0):
        top=stack[-1]
        mark_walked(maze,top)
        callback(maze, top)
        if top[0] == end[1] and top[1] == end[0]:
            return
        time.sleep(0.1)

        arr=get_neigbor(maze,top,end)

        if len(arr)==0:
            mark_dead(maze, top)
            callback(maze, top)
            stack.pop()
        else:
            for i in arr:
                if not out_of_range(end[0]+1,i[1][0],i[1][1]):
                    stack.append(i[1])


