from collections import deque
stack=deque()
def parenthis(s):




    for i in s:

        if i=='(' or i=='{' or i=='[':
            stack.append(i)

        elif len(stack)!=0 and  i==')' and stack.pop()=='(' :
            continue
        elif len(stack)!=0 and i=='}' and stack.pop()=='{' :
            continue
        elif len(stack)!=0 and i==']' and stack.pop()=='[' :
            continue
        else:
            return 0

    if len(stack)==0:
        return 1
    else:
        return 0    


# from collections import deque

# def parenthis(s):
#     stack = deque()  # keep inside function for cleaner scope

#     for i in s:
#         if i in '({[':
#             stack.append(i)
#         elif i in ')}]':
#             if not stack:
#                 return 0  # no opening bracket to match
#             top = stack.pop()
#             if (i == ')' and top != '(') or \
#                (i == '}' and top != '{') or \
#                (i == ']' and top != '['):
#                 return 0
#         else:
#             return 0  # invalid character

#     return 1 if not stack else 0