"""Stacks
    Various implementations of Stacks Data Structure
"""


class ArrayStack:
    def __init__(self):
        self._data = []

    def is_Empty(self):
        return len(self._data) == 0

    def append(self, item):
        """Append"""
        return self._data.append(item)

    def remove(self):
        """Remove"""
        if self.is_Empty():
            return "Stack Underflow"

        return self._data.pop()

    def size(self):
        """Size"""
        return len(self._data)

    def top(self):
        """Top"""
        return self._data[0]


arraystack = ArrayStack()
arraystack.append(5)
arraystack.append(6)
arraystack.append(7)
arraystack.append(8)
print(arraystack.remove())
print(arraystack.top())

# IMPLEMENTATION STACKS
"""Print lines of a file in reverse order in order to display a data set in decreasing order rather than increasing order"""


def reverse_file(filename):
    arr = ArrayStack()

    temp = open(filename)

    for line in temp:
        arr.append(line.rstrip('\n'))
    temp.close()

    newfile = open(filename, 'w')

    while not arr.is_Empty():
        newfile.write(arr.remove() + '\n')
    newfile.close()


"""An Algorithm for Matching Delimiters"""


def is_balanced(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '{' and p2 == '}':
        return True
    if p1 == '[' and p2 == ']':
        return True


def input_params(p):
    stack = ArrayStack()
    index = 0
    flag = True

    while index < len(p) and flag:
        if p[index] in '({[':
            stack.append(p[index])
        else:
            if stack.is_Empty():
                flag = False
            else:
                top = stack.remove()
                print(top)
                if not is_balanced(top, p[index]):
                    flag = False
        index += 1

    if stack.is_Empty() and flag:
        return True
    else:
        return False


print(input_params('({})({}{)'))







