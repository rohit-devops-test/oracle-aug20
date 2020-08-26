try:
    f = open(r"C:\Users\Purushotham\Desktop\oracle_july\day_03\regex_ex\pqr.txt", "r")
    a = 3/5
    b = 10 + "9"
except FileNotFoundError:
    print('There is not such file')
except ZeroDivisionError:
    print('Cant divide by zero')
except:
    print("Some other error")
else:
    print("File found")
    f.close()
finally:
    print('File operation done!')



print("Process begins...")



'''
except Exception as E:
    print("File not found!")
    print(E)
'''
