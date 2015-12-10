in_num = "1113222113"

def do_next(num):
    cur_num = num[0]
    cur_big_num = num
    counter = 0
    output = ""
    for c in num:
        if cur_num is None or cur_num == c:
            cur_num == c
            counter += 1
            continue
        if c != cur_num:
            output += str(counter)
            output += str(cur_num)
            cur_num = c
            counter = 1
    if counter != 0:
        output += str(counter)
        output += cur_num
    return output

for i in range(40):
    in_num = do_next(in_num)

print(len(in_num))


