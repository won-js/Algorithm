n = int(input())
rooms = []
answer = 0

for _ in range(n):
    rooms.append(list(map(int,input().split(" "))))

rooms = sorted(rooms, key = lambda x: x[0])
rooms = sorted(rooms, key = lambda x: x[1])

end = -1

for i in range(n):
    if end <= rooms[i][0] and end <= rooms[i][1]:
        answer += 1
        end = rooms[i][1]

print(answer)