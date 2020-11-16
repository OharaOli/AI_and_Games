import random
def test():
    print("MOVE;3")
    print("MOVE;2")

def select_random(num):
    strings = ["MOVE;1","MOVE;2","MOVE;3", "MOVE;4","MOVE;5","MOVE;6","MOVE;7"]
    random_num = random.randint(0,num)
    print(strings[random_num])

step_num = 0

while(True):
    if(step_num > 3):
        select_random(3)
    else:
        select_random(step_num)
    step_num += 1