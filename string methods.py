# Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
# s='python java sql'
# s.title()
# 'Python Java Sql'
# s.capitalize()
# 'Python java sql'
# s.isalpha()
# False
# s.isalnum()
# False
# s.digit()
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     s.digit()
# AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
# s.isdigit()
# False
# s.isupper()
# False
# s.islower()
# True
# s.iisspace()
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     s.iisspace()
# AttributeError: 'str' object has no attribute 'iisspace'. Did you mean: 'isspace'?
# s.isspace()
# False
# s.uppercase()
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     s.uppercase()
# AttributeError: 'str' object has no attribute 'uppercase'
# s.upper()
# 'PYTHON JAVA SQL'
# s.lower()
# 'python java sql'
# s.swapcasect()
# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     s.swapcasect()
# AttributeError: 'str' object has no attribute 'swapcasect'. Did you mean: 'swapcase'?
# s.len()
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     s.len()
# AttributeError: 'str' object has no attribute 'len'
# len(s)
# 15

# y='Good Morining boy'
# y.count('y')
# 1
# y.count('')
# 18
# y.count('we')
# 0
# y.count('boy')
# 1
# y.cout('o')
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     y.cout('o')
# AttributeError: 'str' object has no attribute 'cout'. Did you mean: 'count'?
# y.count("o")
# 4
# y.count('o',4,7)
# 1
# 1
# 1

# y='hello'
# y.replace(l,*)
# SyntaxError: Invalid star expression
# y.replace(l,1)
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     y.replace(l,1)
# NameError: name 'l' is not defined
# >>> y.replace('l','*')
# 'he**o'
# >>> y.replace('l','*',1)
# 'he*lo'
# >>> y.replace("hello','python')
# ...           
# SyntaxError: unterminated string literal (detected at line 1)
# >>> y.replace('hello','python')
# ...           
# 'python'
# >>> y.replace("Hello','python')
# ...           
# SyntaxError: unterminated string literal (detected at line 1)
# >>> y.replace('Hello','python')
# ...           
# 'hello'
# >>> 
# >>> x='python class done')
# ...           
# SyntaxError: unmatched ')'
# >>> x='python class done'
# ...           
# >>> x.startwith('class')
# ...           
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     x.startwith('class')
# AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
# >>> x.startswith('python')
# ...           
# True
# >>> x.startswith('class',7,12)
# ...           
# True
# >>> x.endswith('done')
# ...           
# True
# >>> x.endswith('hon',3,5+1)
# ...           
# True
# >>> x.endswith('hon',3,5)
# ...           
# False
