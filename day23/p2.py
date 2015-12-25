f = open("input.txt")
d = f.read().splitlines()
registers = {"a":1, "b":0}
memory = d
ip = 0
while True:
    try:
        next_line = memory[ip]
    except:
        break
    line_parts = next_line.split(" ")
    inst = line_parts[0]
    if inst == "hlf":
        registers[line_parts[1]] /= 2
        ip += 1
    elif inst == "tpl":
        registers[line_parts[1]] *= 3
        ip += 1
    elif inst == "inc":
        registers[line_parts[1]] += 1
        ip += 1
    elif inst == "jmp":
        ip += int(line_parts[1])
    elif inst == "jie":
        args = line_parts[1:]
        if registers[args[0][0]] % 2 == 0:
            ip += int(args[1])
        else:
            ip += 1
    elif inst == "jio":
        args = line_parts[1:]
        if registers[args[0][0]] == 1:
            ip += int(args[1])
        else:
            ip += 1

print(registers["b"])



