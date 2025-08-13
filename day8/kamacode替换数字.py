def replace_numbers(s: str) -> str:
    result = []
    for ch in s:
        if ch.isdigit():  # 判断是否为数字字符
            result.append("number")
        else:
            result.append(ch)
    return ''.join(result)

# 读入
s = input().strip()
print(replace_numbers(s))


## 这里的''.join(result)是将列表转换为字符串
## s = input().strip()这里的strip是去掉字符串的开头和结尾部分的内容 保留干净的部分
## isdigit 用来判断是不是数字