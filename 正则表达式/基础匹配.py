""""""
"""
正则表达式: 一种字符串的验证规则, 通过特殊的字符串组合来确立规则
"""
import re

s = "lc python python lc lc"
# match 从头匹配
result = re.match("lc", s)
# print(result) # <re.Match object; span=(0, 2), match='lc'>
result1 = re.match("python", s)
# print(result1) # None
"""如果开头匹配失败则不会匹配后面的字符串"""
# print(f"位置在{result.span()}, 匹配的字符串为{result.group()}") # (0, 2) lc

# search 匹配整个字符串, 直到找到第一个字符串后停止
result2 = re.search("python", s)
# print(result2) # <re.Match object; span=(3, 9), match='python'>

# findall 找出全部匹配项, 返回对象为list
result3 = re.findall("lc", s)
result4 = re.findall("python", s)
# print(result3)
# print(result4)
