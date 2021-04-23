import random
from math import gcd

# primitive root 를 구하는 코드. 
# 질의응답 게시판에서 가져옴.

def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]

def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return False
    else:
        return False
    return True


def key_generation():
    # 이 단계에서 암호화에 필요한 키를 생성합니다.
    # 지금은 성능 검사를 하지 않고 소수 판별을 하지만 추후에는 소수 판별 알고리즘도 속도 개선이 필요할 듯 하다
    
    # p값 정하기
    p = int(input("p 값으로 사용할 양의 정수를 입력해주세요:"))
    while not is_prime(p):  
        p = int(input("입력하신 값이 소수가 아닙니다. p 값으로 사용할 양의 정수를 입력해주세요:"))

    # d값 정하기   
    d = random.randrange(1,p-1) # 1 <= d <= p-2

    # e1 값, primitive root 정하기
    e1 = random.choice(primRoots(p))
    
    # e2 값 구하기
    e2 = e1**d % p
    return e1,e2,p,d
    
def Encryption(e1,e2,p,P):
    # 랜덤한 r을 선택
    r = random.randrange(1,p+1) # 1 <= r <= p
    C1 = (e1 ** r) % p
    C2 = (P*(e2**r)) % p

    return C1,C2

# 역원 구하기 용

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def Decryption(d, p, C1, C2):
    P = (C2 * (C1 ** (p-d-1))) % p
    return P

if __name__ == "__main__":

    # 키생성 호출
    e1,e2,p,d = key_generation()

    print(p)

    # 평문
    plain_text = 7

    # 암호화 호출
    C1,C2 = Encryption(e1,e2,p,plain_text)

    print("Ciphertext:",C1,C2)

    # 복호화 호출
    P = Decryption(d,p,C1,C2)
    print("Plaintext:",P)
