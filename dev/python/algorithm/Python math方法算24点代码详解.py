
import math

PRECISION = 1E-6
COUNT_OF_NUMBER = 4
NUMBER_TO_BE_CAL = 24

g_number = [4, 4, 7, 7]
g_expression = ['', '', '', '']
for i in range(0, 4):
    g_expression[i] = "%d" % g_number[i]
print(g_expression)


def solve(n):
    if(1 == n):
        if(math.fabs(NUMBER_TO_BE_CAL - g_number[0]) < PRECISION):
            print(g_expression[0])
            return True
        else:
            return False
    else:
        for i in range(0, n):
            for j in range(i+1, n):
                a = g_number[i]
                b = g_number[j]
                #**********************************
                #   将剩下的有效数字往前挪，
                #   由于两数计算结果保存在number[i]中，
                #   所以将数组末元素覆盖number[j]即可
                #www.iplaypy.com
                #**********************************
                g_number[j] = g_number[n - 1]
                expa = g_expression[i]
                expb = g_expression[j]
                g_expression[j] = g_expression[n - 1]
                # 计算a+b
                g_expression[i] = '(' + expa + '+' + expb + ')'
                g_number[i] = a + b
                if ( solve(n - 1) ) :
                    return True;

                # 计算a-b
                g_expression[i] = '(' + expa + '-' + expb + ')'
                g_number[i] = a - b
                if ( solve(n - 1) ) :
                    return True

                # 计算b-a
                g_expression[i] = '(' + expb + '-' + expa + ')'
                g_number[i] = b - a
                if ( solve(n - 1) ):
                    return True

                # 计算(a*b)
                g_expression[i] = '(' + expa + '*' + expb + ')'
                g_number[i] = a * b
                if ( solve(n - 1) ):
                    return True;

                # 计算(a/b)
                if (b != 0) :
                    g_expression[i] = '(' + expa + '/' + expb + ')'
                    g_number[i] = a / b
                    if ( solve(n - 1) ) :
                        return True

                # 计算(b/a)
                    if (a != 0) :
                        g_expression[i] = '(' + expb + '/' + expa + ')'
                        g_number[i] = b / a
                        if ( solve(n - 1) ):
                            return True

                 # 恢复现场
                g_number[i] = a
                g_number[j] = b
                g_expression[i] = expa
                g_expression[j] = expb
        return False

if(not solve(COUNT_OF_NUMBER)):
    print('no solution')
