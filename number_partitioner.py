# Finds all the ways to add up to a number with other numbers!
# Uses a recursive, brute-force function


def partition(num, length, repeat_allowed=False, disallowed=[]):
    results = []

    if length == 1:
        results.append([num])

    else:
        if not repeat_allowed:
            disallowed.append(num)
        for i in range(1, num):
            if i not in disallowed:
                sub_results = partition(
                    num - i, length - 1, repeat_allowed, disallowed.copy())
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
    i = input("num: ")
    length = input("len: ")

    import pprint
    pp = pprint.PrettyPrinter()

    partitions = partition(i, length)
    pp.pprint(partitions)
