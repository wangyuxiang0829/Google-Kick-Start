def beautify(N):
    digits = []
    while N != 0:
        digits.append(N % 10)
        N = N // 10
    for digit in digits:
        if digit % 2 != 0:
            return False
    return True


if __name__ == '__main__':
    T = int(input())
    for x in range(1, T + 1):
        N = int(input())
        for y in range(N + 1):
            if beautify(N + y) or beautify(N - y):
                print('Case #', x, ':', ' ', y, sep='')
                break
