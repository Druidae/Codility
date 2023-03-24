def solution(P, Q):
    seen = set()
    distinct_letters = 0
    for i in range(len(P)):
        if P[i] not in seen and Q[i] not in seen:
            distinct_letters += 1
        seen.add(P[i])
        seen.add(Q[i])
    return distinct_letters


def main():
    print(solution('abc', 'bcd'))


if __name__ == '__main__':
    main()
