class UnionFind:
    def __init__(self, N : int):
        self.par = [-1] * N
        self.siz = [1] * N

    # 根を求める
    # 経路圧縮あり
    def root(self, x):
        if self.par[x] == -1:
            return x # xが根の場合はxを返す
        else:
            _r = self.root(self.par[x])
            self.par[x] = _r # 経路圧縮
            return _r

    # xとyが同じグループに属するか
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループを併合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
       
        # すでに同じグループの時は何もしない
        if rx == ry:
            return False
        
        # union by size
        # y側のサイズが小さくなるようにする
        if self.siz[rx] < self.siz[ry]:
            ry, rx = rx, ry
        
        # yをxの子とする
        self.par[ry] = rx
        self.siz[rx] += self.siz[ry]
        
        return True
        
    def size(self, x):
        return self.siz[self.root(x)]

if __name__ == '__main__':
    u = UnionFind(7)

    u.unite(1, 2)
    u.unite(2, 3)
    u.unite(5, 6)

    print(f'{u.issame(1, 3)=}')
    print(f'{u.issame(2, 5)=}')

    u.unite(1, 6)
    print(f'{u.issame(2, 5)=}')
