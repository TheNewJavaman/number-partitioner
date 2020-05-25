#!/usr/bin/env python3

# Finds all the ways to add up to a number with other numbers!
# Uses a recursive, brute-force function
# Loads simple parameters from cli
# If min_n, max_n, repeat_allowed, or disallowed need to be specified,
#     write a script that uses partition() outside of this file

def partition(num, length, min_n=1, max_n=9, repeat_allowed=False, disallowed=[]):
    results = []

    if length == 1 and num <= 9 and num >= 1:
        results.append([num])

    else:
        if not repeat_allowed:
            disallowed.append(num)
        for i in range(min_n, max_n + 1):
            oob_issue = length - 1 == 1 and \
                num - i not in range(min_n, max_n + 1)
            if i not in disallowed and not oob_issue:
                sub_results = partition(
                    num - i, length - 1, min_n, max_n, repeat_allowed, disallowed.copy())
                for sub_result in sub_results:
                    if repeat_allowed or i not in sub_result:
                        sub_result.append(i)
                        if sum(sub_result) == num:
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
