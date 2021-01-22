import random

# 定义棋盘宽度
w = 1000

# 定义棋盘高度
h = 1000

# 定义起点横坐标（列）
start_x = 0

# 定义起点纵坐标（行）
start_y = 0

# 定义终点横坐标（列）
goal_x = 0

# 定义终点纵坐标（行）
goal_y = 2

# 用整数定义墙壁数量比例（0最高）
obstacle_ratio = 2

data = open("data.txt", 'w+')
print(w, h, file=data)
for i in range(h):
    for j in range(w):
        if i == start_y and j == start_x:
            print('s', file=data, end='')
        else:
            if i == goal_y and j == goal_x:
                print('g', file=data, end='')
            else:
                if random.randint(0, obstacle_ratio) == 0:
                    print('1', file=data, end='')
                else:
                    print('0', file=data, end='')
        if j < w - 1:
            print(' ', file=data, end='')
    print('\n', file=data, end='')
data.close()
