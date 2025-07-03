import heapq
import sys

# Directions: (dy, dx)
DIRS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

def read_input():
    k = int(sys.stdin.readline())
    tiles = [int(sys.stdin.readline()) for _ in range(k * k)]
    return k, tuple(tiles)

def is_solvable(board, k):
    inv_count = 0
    flat = [tile for tile in board if tile != 0]
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inv_count += 1

    if k % 2 == 1:
        return inv_count % 2 == 0
    else:
        row = board.index(0) // k
        blank_row_from_bottom = k - row
        return (inv_count + blank_row_from_bottom) % 2 == 0

def manhattan(board, goal_pos, k):
    distance = 0
    for idx, tile in enumerate(board):
        if tile == 0:
            continue
        goal_r, goal_c = goal_pos[tile]
        cur_r, cur_c = divmod(idx, k)
        distance += abs(goal_r - cur_r) + abs(goal_c - cur_c)
    return distance

def neighbors(board, k):
    zero_idx = board.index(0)
    r, c = divmod(zero_idx, k)
    result = []
    for move, (dr, dc) in DIRS.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < k and 0 <= nc < k:
            new_idx = nr * k + nc
            new_board = list(board)
            new_board[zero_idx], new_board[new_idx] = new_board[new_idx], new_board[zero_idx]
            result.append((tuple(new_board), move))
    return result

def solve_puzzle(k, start):
    goal = tuple([0] + list(range(1, k * k)))
    goal_pos = {tile: divmod(idx, k) for idx, tile in enumerate(goal)}

    if not is_solvable(start, k):
        print("This puzzle is not solvable.")
        return

    heap = []
    heapq.heappush(heap, (manhattan(start, goal_pos, k), 0, start, []))
    visited = set()

    while heap:
        est_total_cost, cost_so_far, current, path = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            print(len(path))
            for move in path:
                print(move)
            return

        for neighbor, move in neighbors(current, k):
            if neighbor in visited:
                continue
            new_path = path + [move]
            g = cost_so_far + 1
            h = manhattan(neighbor, goal_pos, k)
            heapq.heappush(heap, (g + h, g, neighbor, new_path))

    print("No solution found.")

# Run the solver
if __name__ == "__main__":
    k, board = read_input()
    solve_puzzle(k, board)
