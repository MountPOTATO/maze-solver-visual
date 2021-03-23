'''
Author: your name
Date: 2021-03-18 12:55:02
LastEditTime: 2021-03-22 10:56:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \game-maze-master\dfs.py
'''
import time
from collections import deque


xd=[-1,0,1,0]
yd=[0,-1,0,1]

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
def mark_walked(maze, pos):
    maze[pos[0]][pos[1]] = CellType.WALKED

def mark_bfs(maze,pos):
    maze[pos[0]][pos[1]] = CellType.BFS_QUEUE

def mark_dead(maze, pos):
    maze[pos[0]][pos[1]] = CellType.DEAD

def out_of_range(num,pos,i):
    x=pos[0]+xd[i]
    y=pos[1]+yd[i]
    return x==-1 or x==num or y==-1 or y==num



def dfs_solve(maze, pos, end, callback):

    time.sleep(0.3)
    #定义栈，非递归解决dfs问题
    stack=deque()
    #插入首节点
    stack.append(pos)

    while(len(stack)!=0):
        top=stack[-1]
        #标记走子
        mark_walked(maze,top)
        callback(maze, top)
        #终点标记
        if top[0] == end[1] and top[1] == end[0]:
            callback(maze,top)
            return
        #更新时间间隔
        time.sleep(0.1)
        #对迷宫四向进行邻位检测
        for i in range (0,5):
            if i==4:
                #死路的回退
                mark_dead(maze, top)
                callback(maze, top)
                stack.pop()
                break
            if  (not out_of_range(end[0]+1,top,i)) and maze[top[0]+xd[i]][top[1]+yd[i]]==CellType.ROAD:
                #TODO：改进四向检测，记忆i
                stack.append([top[0]+xd[i],top[1]+yd[i]])
                break



