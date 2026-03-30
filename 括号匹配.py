#首先判断字符串长度是否为偶数。
#如果遇到左括号，则将其压入栈中
#如果遇到右括号，检查栈顶元素是否为对应类型的左括号，如果匹配，则弹出栈顶元素，继续遍历字符串；如果不匹配，说明括号不平衡，返回False。  
#最后，如果栈为空，说明所有的括号都匹配成功，返回True；如果栈不为空，说明有未匹配的左括号，返回False。
class solution:
    def isvalid(self, s):
        if len(s)%2==1:
            return False
        stack = list()
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')' or ch == ']' or ch == '}':
                if not stack:
                    return False
                top = stack.pop()
                if (ch == ')' and top != '(') or (ch == ']' and top != '[') or (ch == '}' and top != '{'):
                    return False
        return not stack

if __name__ == '__main__':
    s = solution()
    str = '()[]{}'
    print(s.isvalid(str))