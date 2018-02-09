# filename: 016-exceptions.py
# 异常

'''
try & except 块
写代码的时候，出现错误必不可免，即使代码没有问题，也可能遇到别的问题。
'''
import math

'''
捕捉错误
'''
while True:
    try:
        text = input('>')
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print('log10({x}) = {y}'.format(x=x, y=y))
    except ValueError:
        print("该值必须大于0")

print('game over')

# 捕捉不同类型的错误
''' 当把y更改成 1 / math.log10(x) 此时输入 1'''


'''
捕捉所有异常
将except 的值改成 Exception 类，来捕获所有的异常。
'''

while True:
    try:
        text = input('>')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print('log10({x}) = {y}'.format(x=x, y=y))
    except Exception:
        print("该值必须大于0,并且不能为1")

'''
指定特定值
这里，我们把 ZeroDivisionError 加入 except 。

'''

while True:
    try:
        text = input('>')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print('log10({x}) = {y}'.format(x=x, y=y))
    except (ValueError):
        print("该值必须大于0")
    except ZeroDivisionError:
        print("该值不能为1")


# 事实上,我们还可以将这两种方式结合起来,用 Exception 来捕捉其他的错误

while True:
    try:
        text = input('>')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print('log10({x}) = {y}'.format(x=x, y=y))
    except (ValueError):
        print("该值必须大于0")
    except ZeroDivisionError:
        print("该值不能为1")
    except Exception:
        print("输入有误")

# 得到异常类的具体信息
float('a')
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'a'
'''
# 为了得到异常的具体信息，将valueError具体化
while True:
    try:
        text = input('>')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print('log10({x}) = {y}'.format(x=x, y=y))
    except (ValueError)as exc:
        if exc != 'math domain error':
            print("无法将字符串'{}'转换成浮点数".format(text))
        else:
            print("aa")
    except ZeroDivisionError:
        print("该值不能为1")
    except Exception:
        print("输入有误")

# 抛出异常
try:
    raise NameError("hello world")
except NameError:
    # print("an exception flew by !")
    raise

# 自定义异常


class CommandError(ValueError):
    """Documentation for CommandError

    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


valid_commands = {'start', 'stop', 'pause'}

while True:
    command = input('>')
    if command.lower() not in valid_commands:
        raise CommandError('Invalid command: %s' % command)


# finally
'''
try/catch 块还有一个可选的关键词 finally。
不管 try 块有没有异常， finally 块的内容总是会被执行，而且会在抛出异常前执行，
因此可以用来作为安全保证，比如确保打开的文件被关闭。。
'''

try:
    print(1)
finally:
    print('finally was called.')


# 在抛出异常
try:
    print(1 / 0)
finally:
    print('finally was called.\n')

# 如果异常被捕获了 finally 在最后执行
try:
    print(1 / 0)
except ZeroDivisionError:
    print('divide by 0.')
finally:
    print('finally was called.')
    pass

# try except 语句还有一个可选的else子句，如果使用这个子句,
# 那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。

try:
    a = [i for i in range(6, 3, -1)]
except Exception:
    print('这是个误会')
    pass
else:
    print('在列表 {lis} 中最大值为：{zdz:2f} 属性是： {sr}'.format(
        lis=a, zdz=max(a), sr=type(max(a))))
