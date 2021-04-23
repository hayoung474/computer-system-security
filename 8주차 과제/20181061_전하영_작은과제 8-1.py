# 컴퓨터시스템 보안 작은과제 8-1 ElGamal 암호화 시뮬레이션
# example 9 의 예제를 사용
import random

# Alice가 암호문을 생성, 암호화

def Encryption(e1,e2,p,P):
    # 랜덤한 r을 선택
    r = random.randrange(1,p+1) # 1 <= r <= p
    C1 = e1 ** r % p
    C2 = (P*e2**r) % p

    return C1,C2


def Decryption(d,p,C1,C2):
    P = C2*C1**(p-1-d)%p # 페르마의 리틀 정리
    return P



if __name__ == "__main__":

    # 공개키
    e1 = 2
    e2 = 8
    p = 11

    # 개인키
    d = 3

    # 평문
    plain_text = 7

    # 암호화 호출
    C1,C2 = Encryption(e1,e2,p,plain_text)
    print("Ciphertext:",C1,C2)

    # 복호화 호출
    P = Decryption(d,p,C1,C2)
    print("Plaintext:",P)