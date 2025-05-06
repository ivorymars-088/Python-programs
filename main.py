system=int( input('选择进制（2，8，10）:'))
model=input('选择你要进行的运算（+，-，*，/）:')
#检测输入的数字
def check(*nums):
 for num in nums:
 num = str(num)
        try:
            if '.' in num:
                float(num)
            else:
                int(num)
            return True
        except ValueError:
            print('无效输入')
            return False
#加法模块
def c_add(num1,num2):
    one_digit　 = ten_digit = hundred_digit = thousand_digit = wan_digit = ten_wan_digit = 0
    check(num1,num2)
    num1=str(num1)
    num2=str(num2)
    ls1=[char for char in num1]
    ls2=[char for char in num2]
    while len(ls1)<7:
        ls1.insert(0,'0')
    while len(ls2)<7:
        ls2.insert(0,'0')
    one_digit　=int(ls1[-1])+int(ls2[-1])
    if float(one_digit)>=system:
        ten_digit=1
        one_digit-=system
    ten_digit +=int(ls1[-2]) + int(ls2[-2])
    if float(ten_digit) >= system:
        hundred_digit=1
        ten_digit -= system
    hundred_digit +=int(ls1[-3]) + int(ls2[-3])
    if float(hundred_digit) >= system:
        thousand_digit = 1
        hundred_digit -= system
    thousand_digit += int(ls1[-4]) + int(ls2[-4])
    if float(thousand_digit) >= system:
        wan_digit = 1
        thousand_digit -= system
    wan_digit += int(ls1[-5]) + int(ls2[-5])
    if float(wan_digit) >= system:
        ten_wan_digit = 1
        wan_digit -= system
    result=str(ten_wan_digit)+str(wan_digit)+str(thousand_digit)+str(hundred_digit)+str(ten_digit)+str(one_digit)
    return result
#减法模块
def c_reduce(num1,num2):
    one_digit　 = ten_digit = hundred_digit = thousand_digit = wan_digit = ten_wan_digit = 0
    check(num1, num2)
    num1 = str(num1)
    num2 = str(num2)
    if num1>num2:
        ls1 = [char for char in num1]
        ls2 = [char for char in num2]
    else:
        ls2 = [char for char in num1]
        ls1 = [char for char in num2]
    while len(ls1) < 7:
        ls1.insert(0, '0')
    while len(ls2) < 7:
        ls2.insert(0, '0')
    one_digit　 = int(ls1[-1]) - int(ls2[-1])
    if float(one_digit) < 0:
        ten_digit -= 1
        one_digit += system
    ten_digit += int(ls1[-2]) - int(ls2[-2])
    if float(ten_digit) < 0:
        hundred_digit -= 1
        ten_digit += system
    hundred_digit += int(ls1[-3]) - int(ls2[-3])
    if float(hundred_digit) < 0:
        thousand_digit -= 1
        hundred_digit += system
    thousand_digit += int(ls1[-4]) - int(ls2[-4])
    if float(thousand_digit) < 0:
        wan_digit -= 1
        thousand_digit += system
    wan_digit += int(ls1[-5]) - int(ls2[-5])
    result =str(wan_digit) + str(thousand_digit) + str(hundred_digit) + str(ten_digit) + str(one_digit)
    return result
#默认大减小
#乘法模块
def c_multiple(num1,num2):
    result=0
    for i in range(num2):
        result=c_add(result,num1)
    return result
#除法模块
def c_divide(num1,num2):
    times=0
    num0=num1
    switch=True
    while switch:
        if int(num0)<num2:
            switch=False
        num0=num0-num2
        times += 1
        if int(num0)<num2:
            switch=False
    result=times
    remainder=num0
    print('result=',result,'remainder=',remainder)
#检测模式选择合法性
if model in '+-*/':
    num1=int(input('输入第一个数:'))
    num2=int(input('输入第二个数:'))
    if model == '+':
        print(c_add(num1, num2))
    elif model == '-':
        print(c_reduce(num1, num2))
    elif model == '*':
        print(c_multiple(num1, num2))
    elif model == '/':
        c_divide(num1, num2)
else:
    print('无效的模式')