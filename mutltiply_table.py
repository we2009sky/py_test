# encoding = utf-8

print('\t\t\t\t\t\t\t九九乘法表')

for x in range(1,10):
    for y in range(1,10):
        print('{:2} * {:2} = {:2}'.format(x,y,x*y), end='\t')
        if y == 9:
            print('\n')

print('\n\n')         

