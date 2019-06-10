#练习一、求最大公约数和最小公倍数

def gcd(a,b):
    (a,b) = (b,a) if a < b else (a,b)
    #最大公约数
    #	for i in range(10,0,-1):
    for i in range(1,b+1):
        if b % i == 0 and a % i == 0:
            result = i
    #else怎么写？
    print("({},{})的最大公约数是{}".format(a,b,result))

def bcd(a,b):
    (a,b) = (b,a) if a < b else (a,b)
    for i in range(1,30):
        num = a * i
        if num % b == 0:
            print("(%d,%d)的最大公倍数是%d" % (a,b,num))
            break

#练习二、判断一个数是否是回文数
def huiwen(num):
    #相当于取任意位上的数字
    #a = []
    #temp1 = num % 10
    #temp2 = num // 10
    #a.append(temp)
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
#练习三、判断是不是素数
def sushu(num):
    for i in range(2,num):
        if num % i == 0:
            return True

#练习四、判断是不是回文素数
def huiwen_sushu(num):
    if sushu(num) and huiwen(num):
        return True

#斐波那契数列(理解)
'''
def fib(num):
	a,b = 0,1
	while b < num:
		a = a + b
		print(a)
		b = a + b
		print(b)
'''
def fib(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
        yield b

#练习五、跑马灯效果图
import os
import time
def paomadeng():
    content = '~~热烈庆祝重庆大学90周年校庆~~'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]
#练习六、自动生成验证码
import random

def vertification_code(code_len=5):
    w = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(code_len):
        index = random.randint(0,len(w)-1)
        code += w[index]
    print(code)

#练习七、自动生成文件后缀名
#带点或不带点都可以

def get_suffix(filename,has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos <len(filename) - 1:
        index = pos if has_dot else pos + 1
        print(filename[index:])
    else:
        print('Error')

#练习八、返回列表中最大元素和第二大元素



#练习九、计算指定的年月日是一年的第几天

#练习十、打印杨辉三角

#练习十一、双色球选号

#练习十二、约瑟夫环问题

#练习十三、井字棋问题







if __name__ == "__main__":
#	num = int(input('请输入正整数：'))
	