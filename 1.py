def find_prefix(source, target):
    i = 0
    for char in source:
        if i < len(target) and char == target[i]:
            i += 1
    return i == len(target)


def min_subsequences(source, target):
    count = 0
    while target:
        if find_prefix(source, target):
            count += 1
            target = ""
        else:
            for i in range(len(target), 0, -1):
                if find_prefix(source, target[:i]):
                    count += 1
                    target = target[i:]
                    break
            else:
                return -1
    return count


if __name__ == '__main__':
    # 测试用例
    print(min_subsequences("abc", "abcbc"))  # Output: 2
    print(min_subsequences("abc", "acdbc"))  # Output: -1
    print(min_subsequences("xyz", "xzyxz"))  # Output: 3
