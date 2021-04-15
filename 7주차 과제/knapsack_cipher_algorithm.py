b = [7,11,19,39,79,157,313] # 초증가 순서짝을 정함. 순서짝은 직접 정해야 함.
n = 900 # 모듈로 n을 정함. n의 값은 초증가 순서짝의 모든 값의 합 보다 커야 함.
r = 37 # 승수 r을 정함. n과 r은 서로소여야 함.


# 순서짝 t를 계산한다.
def calc_t(b,r,n):
    return [i*r%n for i in b] # t를 계산하여 반환한다.

t = calc_t(b,r,n)

# 치환표를 사용하여 위에서 계산한 t의 값을 치환한다.
def permute(t):
    table = [4,2,5,3,1,7,6] # permute 과정에서 사용할 치환표임.
    return [t[i-1] for i in table] # 치환한 결과를 반환한다.

a = permute(t)

# 여기서 공개키는 a가 되며, 비밀키는 n, b, r 이 된다.

# r의 모듈로 역원을 구한다.
# 아래의 두 함수는 RSA 암호화 알고리즘 강의 자료에서 가져옴.
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

rd = modinv(r,n) #73


# 키 생성 결과 출력
print("\nBob generate keys")
print("t: ",t)
print("a: ",a)
print("Bob's private (n,r,rd,b)",n,r,rd,b) # 900 37 73 [7, 11, 19, 39, 79, 157, 313]


# Alice의 데이터를 생성한다.

# 문자 -> ascii code -> 7 bit binary code -> list -> 리스트 내 값을 int 형으로 변환
x = list(map(int,format(ord("g"),'b'))) 

# knapsackSum 함수를 호출하여 s를 생성한다.
def knapsackSum(a,x):
    s = 0
    for i in range(len(x)):
        s += a[i]*x[i]
    return s
s = knapsackSum(a,x) #2399

# 데이터 생성 결과 출력
print("\nAlice data: ",x)
print("Alice makes cypertext:",s,"and sends it.")

# Bob은 암호문 s를 전달받아 복호화 할 수 있다.

# s' 를 계산한다.
# s’=s × r^-1 mod n . r^-1 은 앞에서 구한 rd 이다.
new_s = s * rd % n

# inv_knapsackSum 함수를 호출하여 계산한다.
# 강의자료의 inv_knapsackSum 의사코드를 그대로 구현
def inv_knapsackSum(new_s,b):
    new_x = []
    for ai in reversed(b):
        if(new_s >= ai):
            new_x.insert(0, 1)
            new_s -= ai
        else: new_x.insert(0, 0)
    return new_x

new_x = inv_knapsackSum(new_s,b)

# 마지막으로 permute(x')를 수행한다.
final_x = permute(new_x)


# Bob의 계산 결과 출력
print("\nBob computes:")
print("s': ",new_s)
print("x': ",new_x)
print("x: ",final_x)
print("\n")



# 가져온 데이터를 복호화 한다.
result = chr(int("". join([str(int) for int in final_x]),2))