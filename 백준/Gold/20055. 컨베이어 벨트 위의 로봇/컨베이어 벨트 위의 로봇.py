from collections import deque

n ,k = map(int, input().split())

field = deque()
field.extend(list(map(int, input().split())))

robot = deque()
robot.extend([False for _ in range(n)])


# 0. 로봇이 올라가 있는 robot_deque idx (N-1)위치에 로봇 true 이면 pop.

# 1. 로봇이 올라가 있는 robot_deque 회전. 칸 내구도를 담은 field_deque 회전
# 1-1. pop 
# 2. 로봇이 올라가 있는 robot_deque 에서 로봇 right 한칸씩 이동 (내구도 체크해야함.)
# 2-1. pop
# 3. 올리는 위치 칸 내구도 체크. 가능하면 로봇 추가
# 4. 내구도가 0인 칸 수가 K 개 이상이라면 종료.

step = 0
cnt = 0
while cnt < k:
    step += 1

    field.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and field[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            field[i+1] -= 1
            if field[i+1] == 0:
                cnt+=1
    robot[-1] = False

    if field[0] > 0:
        robot[0] = True
        field[0] -= 1
        if field[0] == 0:
            cnt += 1


print(step)

