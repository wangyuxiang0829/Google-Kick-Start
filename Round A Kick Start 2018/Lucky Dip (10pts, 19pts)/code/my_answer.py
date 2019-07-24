def E(K, V):
    e = []
    N = len(V)
    e.append(sum(V) / N)
    k = 1
    while k <= K:
        e.append(0)
        for i in V:
            if i > e[k - 1]:
                e[k] += i
            else:
                e[k] += e[k - 1]
        e[k] = e[k] / N
        k = k + 1
    return e[K]


if __name__ == '__main__':
    T = int(input())
    for x in range(1, T + 1):
        l1 = input().split()
        l2 = input().split()
        N = int(l1[0])
        K = int(l1[1])
        V = []
        for v in l2:
            V.append(int(v))
        print('Case #', x, ':', ' ', '{0:.6f}'.format(E(K, V)), sep='')
