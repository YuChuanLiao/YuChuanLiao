#!/usr/bin/python3.10.2

import random

def playGame():
    min = 1
    max = 100
    count = 0
    target = random.randint(min, max)
    print("==========拆數字遊戲==========\n\n")

    while True:
        keyin = int(input(f"拆數字範圍{min}~{max}："))
        count += 1
        if (keyin == target):
            print(f"答對了!!答案是：{target}")
            print(f"您總共猜了{count}次")
            break
        elif keyin > target:
            print(f"數字比{keyin}小")
            max = keyin - 1
        elif keyin < target:
            print(f"數字比{keyin}大")
            min = keyin + 1
        print(f"您已經猜了{count}次")

while(True):
    playGame()
    play_again = input("要再來一局嗎?Y / N:")
    if not (play_again == 'y'):
        break
print("遊戲結束!!!")