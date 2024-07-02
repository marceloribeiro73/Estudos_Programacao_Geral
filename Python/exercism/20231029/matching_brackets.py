def is_paired(input_string):
    flag_is_paired = True
    stack_string = []
    for chr in input_string:
        if chr in ("[{("):
            stack_string.append(chr)
        elif chr in ("]})"):
            if len(stack_string) == 0:
                flag_is_paired = False
            elif chr == "]":
                if "[" in stack_string:
                    if stack_string[-1] == "[":
                        stack_string.pop()
                    else:
                        flag_is_paired = False
                else:
                    flag_is_paired = False
            elif chr == "}":
                if "{" in stack_string:
                    if stack_string[-1] == "{":
                        stack_string.pop()
                    else:
                        flag_is_paired = False
                else:
                    flag_is_paired = False
            elif chr == ")":
                if "(" in stack_string:
                    if stack_string[-1] == "(":
                        stack_string.pop()
                    else:
                        flag_is_paired = False
                else:
                    flag_is_paired = False
    print(stack_string)
    if len(stack_string) > 0:
        flag_is_paired = False

    return flag_is_paired


test = is_paired("{]")
print(test)


test = is_paired("[({]})")
print(test)