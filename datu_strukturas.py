from collections import deque
rinda = deque()

rinda.append(['A','B','C'])
print("Rinda: ", rinda)

rinda.append("D")

print(rinda)

rinda.appendleft('a')
print(rinda)

rinda.pop()
print(rinda)

rinda.popleft()
print(rinda)

kortezs = ('Jan','feb','mar')
print(type(kortezs))

print()
