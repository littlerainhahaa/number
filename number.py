import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1 #count = count + 1
    num = input('請輸入數字:')
    num = int(num)
    if num < r:
        print('比答案小')
    elif num > r:
        print('比答案大')
    else:
        print('終於猜對了!')
        print('你已經猜了', count, '次')
        break
    print('你已經猜了', count, '次')
