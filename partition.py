# Finds all the ways to add up to a number with other numbers!
# Uses a recursive, brute-force function


def partition(num, length, repeat_allowed=False, disallowed=[]):
    results = []

    if length == 1 and num <= 9 and num >= 1:
        results.append([num])

    else:
        if not repeat_allowed:
            disallowed.append(num)
        for i in range(1, 10):
            if i not in disallowed:
                sub_results = partition(
                    num - i, length - 1, repeat_allowed, disallowed.copy())
                if len(sub_results) > 0:
                    break
                for sub_result in sub_results:
                    if repeat_allowed or i not in sub_result:
                        sub_result.append(i)
                        total = 0
                        for j in sub_result:
                            total += j
                        if total == num:
                            sub_result.sort()
                            if sub_result not in results:
                                results.append(sub_result)
        results.sort()

    return results


if __name__ == "__main__":
    import sys

    try:
        i = int(sys.argv[1])
        length = int(sys.argv[2])
    except IndexError:
        print("Error: include args in cmd")
        exit()

    partitions = partition(i, length)
    for partition in partitions:
        print(tuple(partition))
