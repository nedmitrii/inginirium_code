
def check_string_brackets(input_string):
    z = 0
    o = 0
    if input_string[0] == '(' and input_string[-1] == ')':
        for i in range(len(input_string)):
            if input_string[i] == "(":
                o += 1
            elif input_string[i] == ")":
                z += 1
            if z > o:
                print("no")
                return
        if z == o:
            print("yes")
        else:
            print("no")
    else:
        print("no")
check_string_brackets("())(()")