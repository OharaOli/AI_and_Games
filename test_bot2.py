step_count = 0
is_south = False

def test():

    global step_count
    input_str = str(input())

    f = open("test.txt", "a")
    f.write(input_str + "\n")


    if(step_count%2==0):
        print("MOVE;3")
    else:
        print("MOVE;2")
    step_count += 1

f = open("test.txt", "w")
f.write("")
f.close()

while(True):
    test()