n, m = map(int, input().split(" "))

board = []

for _ in range(n):
    board.append(list(input()))

def start_B(board):
    result = 0
    
    for i in range(len(board)):
        if i % 2 == 0:
            start = "B"
        else:
            start = "W"
        for char in board[i]:
            if start != char:
                result += 1
            if start == "B":
                start = "W"
            else:
                start = "B"

    return result

def start_W(board):
    result = 0

    for i in range(len(board)):
        if i % 2 == 0:
            start = "W"
        else:
            start = "B"
        for char in board[i]:
            if start != char:
                result += 1
            if start == "B":
                start = "W"
            else:
                start = "B"

    return result

print(min(start_B(board), start_W(board)))