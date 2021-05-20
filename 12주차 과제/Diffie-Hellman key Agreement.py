g = 7
p = 23

# Alice Side
x = 3
R1 = (g**x)%p

# Bob Side
y = 6
R2 = (g**y)%p

# Alice는 21 R1을 Bob에게 보냄
# Bob은 4 R2를 Alice에게 보냄

print(R1,R2)

# Alice Side
Alice_K = (R2**x)%p

# Bob Side
Bob_K = (R1**y)%p

print(Alice_K , Bob_K)