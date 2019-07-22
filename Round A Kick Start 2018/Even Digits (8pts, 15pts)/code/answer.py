def findX(N):
    '''X is the largest beautiful integer that is still
    no greater than N.

    We can find X by decreasing the first odd digit in N
    by one and then replacing all digits to the right of
    that odd digit with the largest even digit(i.e. 8).

    If there are no odd digits in N, then N is a beautiful
    integer, thus X = N.

    For example, if N = 4436271, then X = 4428888, So in
    this way, there will be no beautiful integer between
    X and N, since the next beautiful integer after X
    would be larger than N at the first odd digit.
    '''
    num = N
    digits = []
    while N != 0:
        digits.insert(0, N % 10)
        N = N // 10
    for index, digit in enumerate(digits):
        if digit % 2 != 0:
            answer = digits[:index]
            answer.append(digit - 1)
            break
    try:
        while len(answer) < len(digits):
            answer.append(8)
    except UnboundLocalError:
        return num
    result = [elem * (10 ** index) for index, elem in enumerate(reversed(answer))]
    return sum(result)


def findY(N):
    '''Y is the smallest beautiful integer that is still
    no smaller than N.

    We can find Y by increasing the first odd digit in N
    by one and replacing all digits to the right of that
    odd digit with the smallest even digit(i.e. 0).

    And there are some tricky cases here:

    1. If the first odd digit is 9, then we must replace the
    digit directly to the left of that odd digit as well
    with the next even digit.

    For example if N = 86912, then Y = 88000.

    2. If the digit directly to the left of the first odd
    digit is 8, then we must replace the digit directly to
    the left of that 8 as well, and keep doing this until
    we have a non-8 digit.

    For example if N = 6488962, then Y = 6600000.

    3. If all digits to left continue to be 8, until we
    reach the leftmost digit, or if the first digit of
    N is 9, we must add a new smallest non-zero even digit
    (i.e. 2) on the left.

    For example if N = 88892 or N = 91112, then Y = 200000.

    4. If there are no odd digits in N, then N is a beautiful
    integer, thus Y = N.

    For example if N = 2, then Y = 2.
    '''
    num = N
    digits = []
    while N != 0:
        digits.append(N % 10)
        N = N // 10
    digits.reverse()
    for index, digit in enumerate(digits):
        if digit % 2 != 0 and digit != 9:
            result = digits[:index]
            result.append(digit + 1)
            while len(result) < len(digits):
                result.append(0)
            break
        elif digit % 2 != 0 and digit == 9:
            i = index
            while i > 0 and digits[i - 1] == 8:
                i = i - 1
            if i == 0:
                result = []
                while len(result) < len(digits):
                    result.append(0)
                result.insert(0, 2)
            else:
                result = digits[:i]
                if result[i - 1] % 2 != 0:
                    result[i - 1] += 1
                else:
                    result[i - 1] += 2
                while len(result) < len(digits):
                    result.append(0)
            break
    try:
        result = [elem * (10 ** index) for index, elem in enumerate(reversed(result))]
        return sum(result)
    except UnboundLocalError:
        return num


if __name__ == '__main__':
    T = int(input())
    for x in range(1, T + 1):
        N = int(input())
        X = findX(N)
        Y = findY(N)
        y = min(abs(X - N), abs(Y - N))
        print('Case #', x, ':', ' ', y, sep='')
