
# -*- coding: utf-8 -*-

symbol_priority = {}
symbol_priority[0] = ['#']
symbol_priority[1] = ['(']
symbol_priority[2] = ['+', '-']
symbol_priority[3] = ['*', '/']
symbol_priority[4] = [')']


def comparePriority(symbol, RPN_stack, symbol_stack):
    '''Compare priority between two symbols'''
    
    global symbol_priority
    if len(symbol_stack) > 0:
        symbol_pop = symbol_stack.pop()
    else:
        return
    
    for list in symbol_priority.values():
        if (symbol in list) and (symbol_pop in list):
            '''same priority'''
            symbol_stack.append(symbol_pop)
            symbol_stack.append(symbol)
            return
        elif symbol in list:
            '''symbol is smaller'''
            RPN_stack.append(symbol_pop)
            #recusion call
            comparePriority(symbol, RPN_stack, symbol_stack)
            return
        elif symbol_pop in list:
            '''symbol is bigger'''
            symbol_stack.append(symbol_pop)
            symbol_stack.append(symbol)
            return
        else:
            continue

        symbol_stack.append(symbol_pop)
        return
        

def scanEveryone(input_string, RPN_stack, symbol_stack):
    for ch in input_string:
        if ch.isdigit():
            RPN_stack.append(ch)
        else:
            if len(symbol_stack) > 0:
                if ch == '(':
                    symbol_stack.append(ch)
                elif ch == ')':
                    while True:
                        symbol_pop = symbol_stack.pop()
                        if symbol_pop == '(':
                            break
                        else:
                            RPN_stack.append(symbol_pop)
                else:
                    comparePriority(ch, RPN_stack, symbol_stack)
            else:
                symbol_stack.append(ch)


def scanInput(RPN_stack, symbol_stack):
    input_string = raw_input()
    input_string += '#'
    scanEveryone(input_string, RPN_stack, symbol_stack)

        
def calRPN(RPN_stack):
    value_stack = []
    RPN_stack.append('#')

    for value in RPN_stack:
        if value == '#':
            return value_stack.pop()
            break
        if value.isdigit():
            value_stack.append(value)
        else:
            right_value = value_stack.pop()
            left_value = value_stack.pop()
            cal_string = left_value + value + right_value
            value_stack.append(str(eval(cal_string)))

#www.iplaypy.com        
        
def main():
    RPN_stack = []
    symbol_stack = []
    
    scanInput(RPN_stack, symbol_stack)
    print calRPN(RPN_stack)


if __name__ == '__main__':
    main()
            