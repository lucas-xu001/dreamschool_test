def check_brackets(input_str):
    stack = []
    output = ""

    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i)
            output += ' '
        elif char == ')':
            if stack:
                stack.pop()
                output += ' '
            else:
                output += '?'
        else:
            output += ' '

    for i in stack:
        output = output[:i] + 'x' + output[i + 1:]

    return output


if __name__ == '__main__':
    # 测试用例
    test_cases = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]

    for test_case in test_cases:
        print(test_case)
        print(check_brackets(test_case))
