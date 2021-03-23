'''
Author: your name
Date: 2021-03-19 15:58:38
LastEditTime: 2021-03-22 19:02:06
LastEditors: your name
Description: In User Settings Edit
FilePath: \game-maze-master\bfs.py
'''
import time
from collections import deque


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


#bfs
def bfs_solve(maze, pos, end, callback):

    time.sleep(0.3)
    #首节点入队
    queue=deque()
    queue.append(pos)



    while(len(queue)!=0):
        sz=len(queue)
        #一次迭代内，对当前队列内所有的可行路径进行分析（相同深度）
        for i in range (0,sz):
            top=queue[0]
            #标记地图，用于访问标记以及io地图更新
            mark_walked(maze, top)
            callback(maze, top)
            #终点检测
            
            queue.popleft()
            #当前节点的邻位节点查看
            arr=get_neigbor(maze,top)
            for i in arr:
                if maze[i[0]][i[1]]==CellType.ROAD:
                    #终点检测
                    if i[0]==end[1] and i[1]==end[0]:
                        mark_walked(maze,i)
                        callback(maze, i)
                        queue.clear()
                        return
                    #入队
                    queue.append(i)
                    mark_walked(maze, i)
                    callback(maze, i)
                    time.sleep(0.1)
    return




