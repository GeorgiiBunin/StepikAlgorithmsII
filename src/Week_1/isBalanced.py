class Stack(list):
    """
    a simple Stack implementation
    """

    def __init__(self):
        self.data = []

    def is_empty(self):
        return not self.data

    def push(self, val):
        return self.data.append(val)

    def top(self):
        return self.data[-1]

    def pop(self):
        return self.data.pop()


def isBalanced(s: str):
    """
    
    :param s: string consists of any characters
    :return: 'Success' if brackets in s are balanced; 
              else: index of a first right bracket without a pair if there is one;
              otherwise: index of a first left bracket without a pair
    
    """
    l_brackets = ['(', '[', '{']
    r_brackets = [')', ']', '}']
    stack = Stack()
    i = 0
    inds = []  # indices of left brackets in s
    for c in s:
        i += 1
        if c in l_brackets:
            stack.push(c)
            inds += [i]
        else:
            if c in r_brackets:
                if stack.is_empty():
                    return i
                top = stack.pop()
                if ((c == ')' and top != '(') or
                        (c == ']' and top != '[') or
                        (c == '}' and top != '{')):
                    return i
                else:
                    del inds[-1]  # remove the index of the left brackets that just found a pair.
    if stack.is_empty():
        return 'Success'
    else:
        return inds[0]


s = input()
print(isBalanced(s))
