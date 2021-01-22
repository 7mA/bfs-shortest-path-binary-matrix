import collections

f = open("data.txt", "r")

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

for i in range(0, h):
    input_line = f.readline()
    input_line = input_line.strip('\n')
    row = input_line.split(" ")
    for j in range(0, w):
        if row[j] == 's':
            start_x = j
            start_y = i
    matrix.append(row)

q = collections.deque()
q.append((start_x, start_y))
visited = set()
visited.add((start_x, start_y))

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
                if matrix[ny][nx] == 'g':
                    print(step, end='')
                    flag = True
                    break
        if flag:
            break
    if flag:
        break
    step += 1

if not flag:
    print('Fail', end='')
