''' 4 kiểu data structure:
1. Stack  Fisrt In Last Out or Last In Fisrt Out
2. Queue  Fisrt In Fisrt Out
3. Linked list
4. Graph'''


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def remove(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


stack = Stack()
# stack.push('asdhfiuhasihfas')


class StringProcessor(Stack):
    def reverse(self, string_input):
        # for i in range(len(string_input)):
        #     self.push(string_input[-1-i])
        # for i in range(self.size()):
        #     print(self.items[i], end='')
        new = ''
        for i in string_input:
            self.push(i)
        for _ in range(self.size()):
            new += self.remove()
        return new

    def decimal_to_binary(self, number):
        raw_result = ''
        while number != 0:
            raw_result += str(number % 2)
            number = number // 2
        return self.reverse(raw_result)
    
    def is_valid(self, expression_string):
        for i in expression_string:
            if i =='(' or i =='{' or i =='['or i == ')' or i == ']' or i =='}':
                if i =='(' or i =='{' or i =='[':
                    self.push(i)
                elif not self.is_empty():
                    if (i ==')' and self.items[-1] == '(') or (i ==']' and self.items[-1] == '[') or (i =='}' and self.items[-1] == '{'):
                        self.remove()
                    else:
                        return False
        return True

        
        # if self.size() % 2 != 0 :
        #     return False
        # else:
        #     x = self.size() // 2
        #     for i in range(x):
        #         if (self.items[x+i] == ')' and self.items[x-i-1] != '(') or (self.items[x+i] == '}' and self.items[x-i-1] != '{') or self.items[x+i] == ']' and self.items[x-i-1] != '[':
        #             return False
        # return True

            
                







string = StringProcessor()
print(string.reverse('Minh'))
print(string.decimal_to_binary(17))
print(string.is_valid('((asdfjasfhsdaiuf]){[]})'))
