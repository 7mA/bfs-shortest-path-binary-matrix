import collections
import time

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# 1000 * 1000: program complete: 4146 seconds

def saveImage(p):
    millis = int(round(time.time() * 1000))
    filename = './img/' + str(millis) + '.png'
    p.savefig(filename)


def colorGradient(current_step, height, width):
    # 根据高度和宽度调整适用于颜色渐变的最大最大步数
    gradient_step_threshold = (height + width) * 1.1

    color_start = [0, 0, 1.0]  # color: b(blue)
    color_goal = [1.0, 0, 0]  # color: r(red)
    if step < gradient_step_threshold:
        return [(color_goal[0] - color_start[0]) * current_step / gradient_step_threshold, 0,
                color_start[2] + (color_goal[2] - color_start[2]) * current_step / gradient_step_threshold]
    else:
        return color_goal


f = open("data.txt", "r")

start_time = time.time()

input_line = f.readline()
input_line = input_line.strip('\n')

matrix_info = input_line.split(" ")
w = int(matrix_info[0])
h = int(matrix_info[1])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

matrix = []

start_x = 0
start_y = 0

goal_x = 0
goal_y = 0

# 调整过程图的大小
plt.figure(figsize=(10, 5))

ax = plt.gca()
ax.set_xlim([0, w])
ax.set_ylim([0, h])

for i in range(0, h):
    input_line = f.readline()
    input_line = input_line.strip('\n')
    row = input_line.split(" ")
    for j in range(0, w):
        if row[j] == 's':
            start_x = j
            start_y = i
            # 调整起点方格样式
            rec = Rectangle((j, h - i), width=1, height=1, facecolor='b', edgecolor="gray")
            print(rec)
            ax.add_patch(rec)
        if row[j] == '0':
            # 调整道路方格样式
            rec = Rectangle((j, h - i), width=1, height=1, facecolor='w', edgecolor="gray")
            print(rec)
            ax.add_patch(rec)
        if row[j] == '1':
            # 调整墙壁方格样式
            rec = Rectangle((j, h - i), width=1, height=1, facecolor='gray', edgecolor="gray")
            print(rec)
            ax.add_patch(rec)
        if row[j] == 'g':
            # 调整终点方格样式
            rec = Rectangle((j, h - i), width=1, height=1, facecolor='r', edgecolor="gray")
            print(rec)
            ax.add_patch(rec)
    matrix.append(row)

print("image setup complete:", int(time.time() - start_time), "seconds")
plt.axis('equal')
plt.axis('off')
plt.tight_layout()
# plt.show()
print("layout update complete:", int(time.time() - start_time), "seconds")

q = collections.deque()
q.append((start_x, start_y))
visited = set()
visited.add((start_x, start_y))

saveImage(plt)
print("initial image render complete:", int(time.time() - start_time), "seconds")

step = 1
flag = False

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and matrix[ny][nx] != '1' and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))

                # 方格填充渐变色
                rec = Rectangle((nx, h - ny), 1, 1, color=colorGradient(step, h, w))
                print(rec)
                ax.add_patch(rec)

                # 方格填充步数
                # plt.text(nx + 0.5, h - ny + 0.5, step,
                #          fontsize=7.5, verticalalignment="center", horizontalalignment="center")

                # 单步保存过程图
                # saveImage(plt)

                if matrix[ny][nx] == 'g':
                    # 调整y值以调节结果文本位置
                    plt.title("%s steps" % step, fontsize='15', fontweight='bold', y=-0.03)
                    saveImage(plt)
                    print("result image save complete:", int(time.time() - start_time), "seconds")
                    print(step, end='')
                    flag = True
                    break
        if flag:
            break
    if flag:
        break
    # 整合保存过程图，通过求余除数调整步长
    if step % 2 == 0:
        saveImage(plt)
        print("image save complete:", int(time.time() - start_time), "seconds")
    step += 1

if not flag:
    # 调整y值以调节结果文本位置
    plt.title("Fail", fontsize='15', fontweight='bold', y=-0.03)
    saveImage(plt)
    print('Fail', end='')

print()
print("program complete:", int(time.time() - start_time), "seconds")
