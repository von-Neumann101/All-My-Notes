import random

# ===== 迷宫定义 =====
# S 起点在 (0,0)
# G 终点
# # 墙
GRID = [
    "S....",
    ".##..",
    "...#.",
    ".##..",
    ".#.G."
]
H, W = len(GRID), len(GRID[0])

START = (0, 0)
GOAL = None
WALLS = set()
for y in range(H):
    for x in range(W):
        c = GRID[y][x]
        if c == '#':
            WALLS.add((x, y))
        elif c == 'G':
            GOAL = (x, y)

ACTIONS = [0, 1, 2, 3]  # 0上 1下 2左 3右
DIRS = {
    0: (0, -1),
    1: (0,  1),
    2: (-1, 0),
    3: (1,  0),
}

def in_bounds(x, y):
    return 0 <= x < W and 0 <= y < H

def step(state, action):
    """给定当前 state 和 action, 返回 next_state, reward, done"""
    x, y = state
    dx, dy = DIRS[action]
    nx, ny = x + dx, y + dy

    # 撞边界：不动，给惩罚
    if not in_bounds(nx, ny):
        return (x, y), -1.0, False

    # 撞墙：不动，给惩罚
    if (nx, ny) in WALLS:
        return (x, y), -1.0, False

    # 正常移动
    next_state = (nx, ny)

    # 到终点
    if next_state == GOAL:
        return next_state, 10.0, True

    # 普通一步：可给轻微步惩罚，鼓励更短路径（也可设为 0）
    return next_state, 0, False

def epsilon_greedy(Q, state, epsilon):
    """以 epsilon 概率随机，否则选 Q 最大动作"""
    if random.random() < epsilon:
        return random.choice(ACTIONS)
    # 若 state 不在 Q 里，默认全 0，随便选一个最大
    qs = Q.get(state, [0.0, 0.0, 0.0, 0.0])
    best_a = max(range(4), key=lambda a: qs[a])
    return best_a

def train_q_learning(episodes=3000, alpha=0.1, gamma=0.99,
                     eps_start=1.0, eps_end=0.05, eps_decay=0.999):
    """
    Q-learning:
    Q[s,a] <- Q[s,a] + alpha * (r + gamma*max_a' Q[s',a'] - Q[s,a])
    """
    Q = {}  # dict: state -> [q_up, q_down, q_left, q_right]
    epsilon = eps_start

    for ep in range(1, episodes + 1):
        state = START
        total_reward = 0.0
        done = False

        # 防止死循环：每局最多走 200 步
        for t in range(200):
            action = epsilon_greedy(Q, state, epsilon)
            next_state, reward, done = step(state, action)
            total_reward += reward

            # 取出 Q[state]，不存在就初始化全 0
            if state not in Q:
                Q[state] = [0.0, 0.0, 0.0, 0.0]
            if next_state not in Q:
                Q[next_state] = [0.0, 0.0, 0.0, 0.0]

            # Q-learning 更新（核心一行）
            best_next = max(Q[next_state])
            td_target = reward + (0.0 if done else gamma * best_next)
            td_error = td_target - Q[state][action]
            Q[state][action] += alpha * td_error

            state = next_state
            if done:
                break

        # epsilon 逐渐变小：从“多探索”到“多利用”
        epsilon = max(eps_end, epsilon * eps_decay)

        # 每 200 局打印一次训练状况
        if ep % 200 == 0:
            print(f"ep={ep:4d}  total_reward={total_reward:7.2f}  epsilon={epsilon:.3f}  steps={t+1}")

    return Q

def rollout(Q, max_steps=200):
    """用学到的 Q 表走一局（不探索，只贪心）"""
    state = START
    path = [state]
    for _ in range(max_steps):
        qs = Q.get(state, [0.0, 0.0, 0.0, 0.0])
        action = max(range(4), key=lambda a: qs[a])
        next_state, reward, done = step(state, action)
        path.append(next_state)
        state = next_state
        if done:
            return path, True
    return path, False

if __name__ == "__main__":
    Q = train_q_learning()

    path, success = rollout(Q)
    print("\nSuccess:", success)
    print("Path length:", len(path))
    print("Path:", path)
