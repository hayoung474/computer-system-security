def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    print(g, y, x)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def DSA_simulation():
    
    # Alice generates a key
    p = 101
    q = 8081
    e0 =3
    e1 = e0 ** ((p-1)/q) % p 
    d = 61
    e2 = e1 ** d % p
    print(e1,e2)
    
    print("Alice's key:",e1,e2,p,q,d)

    hM = 5000
    r = 61

    S1 = (e1**r % p)% q
    S2 = (hM + (d*S1)*modinv(r,q))%q

    print(S1,S2)
