
# coding = utf-8
import threading

import pygame

from maze_generator import generate_maze
from dfs import dfs_solve
from bfs import bfs_solve
from bestfs import bestfs_solve
from astar import astar_solve
from hillclimbing import hill_climbing_solve
from genetic import ga_solve
from utils import stop_thread
import random
from astar import astar_solve
import copy

pygame.init()

# 定义一些共用属性
# 尺寸
WIDTH = 400
HEADER = 30
HEIGHT = WIDTH + HEADER
WINDOW = (WIDTH, HEIGHT)

# 标题
TITLE = "迷宫"
# 初始化界面与标题
SCREEN = pygame.display.set_mode(WINDOW)
pygame.display.set_caption(TITLE)
# 刷新相关
FPS = 60
CLOCK = pygame.time.Clock()

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BFS=(155,123,124)

FONT_SIZE = 16
FONT = pygame.font.Font("ext/fonts/msyh.ttf", FONT_SIZE)

BUTTONS = []

SOLVE_THREAD = None


MAZE=list()
ENTRANCE=list()
EXIT=list()
MAZE_CPY=list()
ENTRANCE_CPY=list()
EXIT_CPY=list()



def draw_rect(x, y, len, color):
    pygame.draw.rect(SCREEN, color, [x, y, len, len], 0)


def draw_button(x, y, len, height, text):
    pygame.draw.rect(SCREEN, COLOR_BLACK, [x, y, len, height], 1)
    text_surface = FONT.render(text, True, COLOR_BLACK)
    text_len = text.__len__() * FONT_SIZE
    # 文字居中
    SCREEN.blit(text_surface, (x + (len - text_len) /0.8, y + 2))


def refresh(i):
    global MAZE, ENTRANCE, EXIT, SOLVE_THREAD,MAZE_CPY,ENTRANCE_CPY,EXIT_CPY
    
    if SOLVE_THREAD is not None and SOLVE_THREAD.is_alive():
        stop_thread(SOLVE_THREAD)
        SOLVE_THREAD = None
    #生成迷宫与入口
    if i==0:
        maze_temp,entrance_temp,exit_temp=copy.deepcopy(MAZE_CPY),copy.deepcopy(ENTRANCE_CPY),copy.deepcopy(EXIT_CPY)
        SOLVE_THREAD = threading.Thread(target=dfs_solve, args=(maze_temp, entrance_temp, exit_temp, draw_maze))
        SOLVE_THREAD.start()
    if i==1:        
        maze_temp,entrance_temp,exit_temp=copy.deepcopy(MAZE_CPY),copy.deepcopy(ENTRANCE_CPY),copy.deepcopy(EXIT_CPY)
        SOLVE_THREAD = threading.Thread(target=bfs_solve, args=(maze_temp, entrance_temp, exit_temp, draw_maze))
        SOLVE_THREAD.start()
    if i==2:
        maze_temp,entrance_temp,exit_temp=copy.deepcopy(MAZE_CPY),copy.deepcopy(ENTRANCE_CPY),copy.deepcopy(EXIT_CPY)
        SOLVE_THREAD = threading.Thread(target=bestfs_solve, args=(maze_temp, entrance_temp, exit_temp, draw_maze))
        SOLVE_THREAD.start()
    if i==3:
        maze_temp,entrance_temp,exit_temp=copy.deepcopy(MAZE_CPY),copy.deepcopy(ENTRANCE_CPY),copy.deepcopy(EXIT_CPY)
        SOLVE_THREAD = threading.Thread(target=astar_solve, args=(maze_temp, entrance_temp, exit_temp, draw_maze))
        SOLVE_THREAD.start()
    if i==4:
        maze_temp,entrance_temp,exit_temp=copy.deepcopy(MAZE_CPY),copy.deepcopy(ENTRANCE_CPY),copy.deepcopy(EXIT_CPY)
        SOLVE_THREAD = threading.Thread(target=hill_climbing_solve, args=(maze_temp, entrance_temp, exit_temp, draw_maze))
        SOLVE_THREAD.start()
    if i==5:
        size = random_maze_size()
        MAZE, ENTRANCE, EXIT = generate_maze(size, size)
        MAZE_CPY,ENTRANCE_CPY,EXIT_CPY=copy.deepcopy(MAZE),copy.deepcopy(ENTRANCE),copy.deepcopy(EXIT)
        SOLVE_THREAD = threading.Thread(target=dfs_solve, args=(MAZE, ENTRANCE, EXIT, draw_maze))
        SOLVE_THREAD.start()

x_button=[2,64,126,205,247,289]
length_button=[60,60,77,40,40,125]
# 绘制迷宫

def draw_maze(maze, cur_pos):
    SCREEN.fill(COLOR_WHITE)
    #draw_button(2, 2, WIDTH - 4, HEADER - 4, '刷新地图')
    draw_button(2, 2, 60, 26,'dfs')
    draw_button(64,2,60,26,'bfs')
    draw_button(126,2,77,26,'gbfs')
    draw_button(205,2,40,26,'a*')
    draw_button(247,2,40,26,'hc')
    draw_button(289,2,125,26,'refresh')
    
    
    if len(BUTTONS)==0:
        for i in range(0,6):
            BUTTONS.append({
                'x': x_button[i],
                'y': 2,
                'length': length_button[i],
                'height': HEADER - 4,
                'click': refresh
            })

    size = len(maze)
    cell_size = int(WIDTH / size)
    cell_padding = (WIDTH - (cell_size * size)) / 2
    for x in range(size):
        for y in range(size):
            cell = maze[x][y]
            color = COLOR_BFS if cell==4 else COLOR_BLACK if cell == 1 else COLOR_RED if cell == 3 else COLOR_CYAN if cell == 2 else COLOR_WHITE
            if x == cur_pos[0] and y == cur_pos[1]:
                color = COLOR_GREEN
            draw_rect(cell_padding + y * cell_size, HEADER + cell_padding + x * cell_size, cell_size - 1, color)
    pygame.display.flip()


def dispatcher_click(pos):
    for i in range (0,len(BUTTONS)):
        button=BUTTONS[i]
        x, y, length, height = button['x'], button['y'], button['length'], button['height']
        pos_x, pos_y = pos
        if x <= pos_x <= x + length and y <= pos_y <= y + height:
            button['click'](i)


def random_maze_size():
    return random.randint(5, 10) * 2 + 1


if __name__ == '__main__':
    # 生成迷宫与入口
    
    

    
    size = random_maze_size()
    MAZE, ENTRANCE, EXIT = generate_maze(size, size)

    MAZE_CPY,ENTRANCE_CPY,EXIT_CPY=copy.deepcopy(MAZE),copy.deepcopy(ENTRANCE),copy.deepcopy(EXIT)

    
    SOLVE_THREAD = threading.Thread(target=dfs_solve, args=(MAZE, ENTRANCE, EXIT, draw_maze))
    SOLVE_THREAD.start()
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            # 检查是否关闭窗口
            if event.type == pygame.QUIT:
                if SOLVE_THREAD is not None and SOLVE_THREAD.is_alive():
                    stop_thread(SOLVE_THREAD)
                    SOLVE_THREAD = None
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                dispatcher_click(mouse_pos)
