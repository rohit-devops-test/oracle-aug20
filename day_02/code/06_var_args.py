def func(a,b,c=7,*args,**kargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kargs)


func(1,2)
print('-'*40)
func(1,2,3)
print('-'*40)
func(1,2,3,4,5,6)
print('-'*40)
func(1,2,3,4,5,6,name='anil', age=35)
print('-'*40)

