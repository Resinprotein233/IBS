#python3
from random import randint
from pykeyboard import PyKeyboard
from pymouse import PyMouse

m = PyMouse()
k = PyKeyboard()

information = """
                 信息轰炸脚本
                     IBS

Beta 1.0
本脚本用于轰炸钓鱼页面，在启用本脚本之前，请先进行以下几点测试：
1.测试页面是否可以使用回车进行确认
2.测试是否再输入后会跳转到正常页面

                   使用方法               
输入“1”开始轰炸
输入“2”退出本程序
"""
An=1
print(information)
massage = input("IBS=>")
while massage == 1:
    print("轰炸开始！")
    randint(000000000000,999999999999)#生成随机假账号
    k.tap_key(k.enter_key)
    randint(000000000,999999999)#生成随机假密码
    k.tap_key(k.enter_key)
    k.tap_key(k.enter_key)
if massage == 2:
    print("成功退出")
    
