import opr
import sys
from time import sleep

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special = ["var", "add", "mul", "not", "sub", "dgt", "dst", "inp"]
operations = ["teq", "tlt", "tgt", "tcp"]
addons = ["+", "-"]
stack = {}
try:
    oldfile = open(sys.argv[1], "r").readlines()
except IndexError:
    print("No file name found!")
file = oldfile


def compile(command):
    global nxtpl, lp, stack
    if command[0] == "mov":
        stack[command[2]] = command[1]
    elif command[0] == "dgt":
        x = list(stack.get(command[1]))
        x.reverse()
        stack[command[1]] = int(x[int(command[2])])
        del x
    elif command[0] == "dst":
        x = list(stack.get(command[1]))
        x.reverse()
        x[int(command[2])] = command[3]
        x.reverse()
        d = ''
        for i in x:
            d += str(i)
        d = int(d)
        stack[command[1]] = d
        del x, d
    elif command[0] == "jmp":
        lp = command[1]
    elif command[0] == "slp":
        sleep(isint(command[1]))
    elif command[0] == "add":
        stack[command[1]] = int(stack[command[1]]) + isint(command[2])
    elif command[0] == "sub":
        stack[command[1]] = int(stack[command[1]]) - isint(command[2])
    elif command[0] == "mul":
        stack[command[1]] = int(stack[command[1]]) * isint(command[2])
    elif command[0] == "not":
        if command[1] > 0:
            stack[command[1]] = 0
        else:
            stack[command[1]] = 100
    elif command[0] == "inp":
        stack[command[1]] = input()
    elif command[0] == "prt":
        print(stack.get(command[1]))

    elif command[0] in operations:
        if command[0] == "teq":
            nxtpl = opr.teq(command[1], command[2], stack)
        if command[0] == "tgt":
            nxtpl = opr.tgt(command[1], command[2], stack)
        if command[0] == "tlt":
            nxtpl = opr.tlt(command[1], command[2], stack)
        if command[0] == "tcp":
            nxtpl = opr.tcp(command[1], command[2], stack)


def isint(string):
    try:
        return int(string)
    except:
        return int(stack.get(string))


nxtpl = 0
lp = ""
run = True


def smp():
    global run, nxtpl, lp, file
    for line in file:
        command = line.replace("\n", "", 1)
        command = command.split()
        if len(command) > 0:
            if command[0] in operations:
                nxtpl = 0
            if nxtpl == 1:
                if command[0] == "+":
                    compile(command[1:])
            elif nxtpl == 2:
                if command[0] == "-":
                    compile(command[1:])
            elif nxtpl == 3:
                pass
            else:
                if list(command[0])[0] == "#":
                    pass
                else:
                    nxtpl = 0
                    compile(command)
        if lp != "":
            break
    if lp == "":
        run = False


while run:
    try:
        smp()
        if lp != "":
            file = oldfile
            file = file[file.index(lp + ":\n"):]
            lp = ""
    except KeyboardInterrupt:
        quit()
