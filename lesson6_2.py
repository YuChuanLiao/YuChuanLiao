#!/usr/bin/python3.10.2

import random

min = 1
max = 10
count = 0
target = random.randint(min, max)
print("==========拆數字遊戲==========")

while True:
    keyin = int(input(f"拆數字範圍{min}~{max}："))
    count += 1
    if (keyin == target):
        print(f"答對了!!答案是：{target}")
        print(f"您總共猜了{count}次")
        break
    else:
        print("猜錯囉，再來一次")
        print(f"您已經猜了{count}次")
print("遊戲結束!!!")