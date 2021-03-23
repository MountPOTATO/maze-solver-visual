'''
Author: your name
Date: 2021-03-21 10:20:19
LastEditTime: 2021-03-23 12:03:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \game-maze-master\bestfs.py
'''
import time
from collections import deque
import heapq

# 单元格类型
# 0 - 路，1 - 墙，2-走过的路，4-死胡同
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

def mark_final(maze,pos):
    maze[pos[0]][pos[1]] = CellType.LAST



def get_neigbor(maze,pos):
    arr=[]

    if maze[pos[0]+1][pos[1]]==CellType.ROAD:
        arr.append([pos[0]+1,pos[1]])
    if maze[pos[0]-1][pos[1]]==CellType.ROAD:
        arr.append([pos[0]-1,pos[1]])
    if maze[pos[0]][pos[1]+1]==CellType.ROAD:
        arr.append([pos[0],pos[1]+1])
    if maze[pos[0]][pos[1]-1]==CellType.ROAD:
        arr.append([pos[0],pos[1]-1])

    return arr

def out_of_range(num,pos,i):
    x=pos[0]+xd[i]
    y=pos[1]+yd[i]
    return x==-1 or x==num or y==-1 or y==num

def h(n,end):
    return abs(n[1]-end[1])+abs(n[0]-end[0])


def bestfs_solve(maze, pos, end, callback):
    time.sleep(0.3)
    pq=[]

    #在原有bfs基础上，使用优先队列对邻接点进行估值排序
    heapq.heappush(pq,(h(pos,end),pos))

    while(len(pq)!=0):
        #首节点
        first=pq[0]
        top=first[1]

        mark_walked(maze, top)
        callback(maze,top)
        #出队
        heapq.heappop(pq)
        #邻接查找
        arr=get_neigbor(maze,top)
        if len(arr)==0:
            mark_dead(maze,top)
            callback(maze,top)
        for i in arr:
            #终点检测
            if i[0]==end[1] and i[1]==end[0]:
                callback(maze,i)
                return
            if maze[i[0]][i[1]]==CellType.ROAD:
                mark_bfs(maze, i)
                callback(maze,i)
                time.sleep(0.1)
                #放入优先队列
                heapq.heappush(pq, (h(i,end),i))













