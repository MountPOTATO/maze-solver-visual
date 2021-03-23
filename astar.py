import time
from collections import deque
import heapq
from math import *




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

def out_of_range(num,x,y):
    return x==-1 or x==num or y==-1 or y==num

xd=[-1,1,0,0]
yd=[0,0,1,-1]


def get_neigbor(maze,top_block,end,f_maze,openlist):
    arr=[]

    for i in range(0,4):

        x=top_block.coord[0]+xd[i]
        y=top_block.coord[1]+yd[i]
        if (not out_of_range(end[0]+1,x,y)) and maze[x][y]==CellType.ROAD and ((f_maze[x][y],(x,y)) not in openlist):
            temp_block=block((x,y))
            temp_block.g=top_block.g+1
            temp_block.h=mahattan(temp_block.coord,end)
            arr.append(temp_block)
    return arr



def astar_solve(maze,pos,end,callback):

    #初始化估值地图 记录每个格子的f代价（g+h）
    f_maze=maze
    for i in f_maze:
        i=0

    #带g，h的坐标参数
    start=block(pos)

    #待访问节点，存储可能的移动路径
    openlist=[]
    

    heapq.heappush(openlist,(0,start))


    while(len(openlist)!=0):
        #获取f值最小的首个格子信息
        top_block=openlist[0][1]
        #获取格子坐标
        top_pos=top_block.coord
        #标记路线
        mark_walked(maze, top_pos)
        callback(maze,top_pos)
        heapq.heappop(openlist)

        #获取接下来的路径，每个节点都不在openlist中，且仍未访问过
        arr=get_neigbor(maze,top_block,end,f_maze,openlist)
        time.sleep(0.1)

        for i in arr:
            #终点标记
            if i.coord[0]==end[1] and i.coord[1]==end[0]:
                mark_walked(maze, i.coord)
                callback(maze, i.coord)
                openlist.clear()
                return
            #对每个邻位格子，计算f值，根据f值大小存入并维护openlist优先队列
            new_f=i.g+i.h
            heapq.heappush(openlist,(new_f,i))
            #更新f_maze
            f_maze[i.coord[0]][i.coord[1]]=new_f


