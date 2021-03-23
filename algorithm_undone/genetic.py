

import time
import random

#方向信息
d_binary_code=[[0,0],[0,1],[1,0],[1,1]]
xd=[-1,1,0,0]
yd=[0,0,1,-1]


def out_of_range(num,x,y):
    return x==-1 or x==num or y==-1 or y==num




def fitness(code,pos,end,maze):
    f=0
    end_x=end_y=temp_x=temp_y=0
    direction=0

    end_x=pos[0]
    end_y=pos[1]

    for i in range(0,len(code)):
        temp=[code[2*i],code[2*i+1]]
        direction=binary_value(temp)
        print(direction)
        temp_x=end_x+xd[direction]
        temp_y=end_y+yd[direction]

        if not out_of_range(end[0]+1,temp_x,temp_y) and maze[temp_x][temp_y]==CellType.ROAD:
            end_x=temp_x
            end_y=temp_y
    
    f=1/(abs(end_x-end[0])+abs(end_y-end[1])+1)
    return f

def reach_end(code,pos,end,maze):
    end_x=end_y=temp_x=temp_y=0
    direction=0

    end_x=pos[0]
    end_y=pos[1]

    for i in range(0,len(code)):
        temp=[code[2*i],code[2*i+1]]
        direction=binary_value(temp)

        temp_x=end_x+xd[direction]
        temp_y=end_y+yd[direction]

        if not out_of_range(end[0]+1,temp_x,temp_y) and maze[temp_x][temp_y]==CellType.ROAD:
            end_x=temp_x
            end_y=temp_y
    if end_x==end[0] and end_y==end[1]:
        return True
    else:
        return False


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


def binary_value(binary_codes):
    res=0
    k=0
    for i in range(len(binary_codes)-1,-1,-1):
        if binary_codes[i]==1:
            res+=pow(2,k)
        k+=1
    return res

def init_set(set_num,min_step_num):
    #TODO:
    direction=0
    arr=[]
    for i in range(0,set_num):
        step_code=[]
        for j in range(0,min_step_num):
            direction_code=random.randint(0,3)
            step_code.append(d_binary_code[direction_code][0])
            step_code.append(d_binary_code[direction_code][1])
        arr.append(step_code)
    return arr



def select(init_codes,set_num,pos,end,maze):
    #TODO:
    sum_fitness=0
    random_num=0
    res_code=[]
    adaptive_value=[]
    for i in range(0,set_num):
        adaptive_value.append(fitness(init_codes[i],pos,end,maze))
        sum_fitness+=adaptive_value_value[i]
    
    #概率化
    for i in range(0,set_num):
        adaptive_value[i]/=sum_fitness
    
    for i in range(0,set_num):
        #取到随机概率值
        #TODO:DEBUG_CHECK
        random_num=random.randint(1,100)
        if random_num==100:
            random_num-1
        random_num/=100

    sum_fitness=0

    for i in range(0,set_num):
        if random_num>sum_fitness and random_num<=sum_fitness+adaptive_value[j]:
            temp=init_codes[i]
            res_code.append(temp)
        else:
            sum_fitness+=adaptive_value[i]

    return res_code

    

def cross(selected_codes,min_step_num):
    rand_num=0
    cross_point=0
    res_code=[]
    #随机编码队列，进行随机交叉配对  
    rand_code_seqs=[]

    #随机排序
    while len(selected_codes)>0:
        rand_num=random.randint(0,len(selected_codes)-1)
        rand_code_seqs.append(selected_codes[rand_num])
        selected_codes.remove(rand_num)

    temp=0
    array1=array2=[]
    #两两交叉运算
    for i in range(1,len(rand_code_seqs)):
        if i%2==1:
            array1=rand_code_seqs[i-1]
            array2=rand_code_seqs[i]
            cross_point=rand_code_seqs.randint(1,min_step_num-1)
            #交叉点位置后的编码调换
            for j in range(0,2*min_step_num):
                if j>=2*cross_point:
                    temp=array1[j]
                    array1[j]=array2[j]
                    array2[j]=temp
            res_code.append(array1)
            res_code.append(array2)

    return res_code

def variate(crossed_codes,min_step_num):
    #TODO:debug
    variation_point=0
    res_code=[]

    for arr in crossed_codes:
        variation_point=random.randint(0,min_step_num-1)

        for i in range(0,len(i),2):
            if i%2==0 and i/2==variation_point:
                arr[i]=  1 if arr[i]==0 else 0
                arr[i+1]=  1 if arr[i+1]==0 else 0
                break;
        
        res_code.append(arr)
    
    return res_code






def ga_solve(maze, pos, end, callback):
    genetic_epoch_num=100
    can_end=False
    min_step_num=2*end[0]+2

    init_codes=[]
    selected_codes=[]
    crossed_codes=[]
    variation_codes=[]

    init_codes=init_set(4,2*end[0]+2)


    for a in range(0,genetic_epoch_num):
        for i in init_codes:
            print("this is",i)
            if reach_end(i,pos,end,maze):
                return
        
        selected_codes=select(init_codes,pos,end,maze)
        crossed_codes=cross(selected_codes,min_step_num)
        variation_codes=variate(crossed_codes,min_step_num)
        init_codes=variation_codes

    return