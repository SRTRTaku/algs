"""
Binary indexed tree
1 indexed
初期値は　a1 = ... = an = 0
* add(i, x) : ai += x
* sum(i) : a1 + ... + ai
ex)
1 (0b0001) : a1
2 (0b0010) : a1 + a2
3 (0b0011) : a3
4 (0b0100) : a1 + a2 + a3 + a4
5 (0b0101) : a5
6 (0b0110) : a5 + a6
7 (0b0111) : a7
8 (0b1000) : a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
---
add(5, x)
    -> 0b0101, 0b0110, 0b1000 に+=x
---
sum(5, x)
    -> 0b0101, 0b0100
"""

class Bit:
    def __init__(self, n):
        self.n = n + 1 # 配列の要素数、数列の要素数+1
        self.a = [0] * self.n

    def add(self, i, x):
        idx = i
        while idx < self.n:
            self.a[idx] += x
            idx += idx & -idx # 最後に1が立っているビットを加算する
    
    def sum(self, i):
        s = 0
        idx = i
        while idx > 0:
            s += self.a[idx]
            idx -= idx & -idx # 最後に1が立っているビットを減算する
        return s

if __name__ == '__main__':
    bit = Bit(8)
    for i in range(8):
        bit.add(i + 1, 10 * (i + 1) )
        print(bit.sum(5))
    for i in range(8):
        print(bit.sum(i+1))
