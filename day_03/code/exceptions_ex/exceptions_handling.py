a = 10 * 3
try:
    a = 10/0
    b = 10 + 10
    #f = open('XYZ', 'r')
except ZeroDivisionError:
    print('Cannot divide a number by zero!')
    try:
        print(a)
    except:
        print('Nothing defined for a')
except TypeError:
    print('Type mismatch for the operator in concern.')
except Exception as E:
    print(E)
except:
    print('Some other error occured')
else:
    print(a)
    print(b)
finally:
    print('Operation completed')


print('Thank you!')
