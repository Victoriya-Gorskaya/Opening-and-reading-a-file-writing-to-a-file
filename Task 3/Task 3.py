s3 = []
str_n = 0
import os
list_text = [i for i in os.listdir() if i.endswith('.txt')]
list_text.sort()
with open('result.txt','w', encoding = 'utf8') as f:
    for file in list_text:
        s = open((file), encoding = 'utf8').readlines()
        str_n = len(s)
        s3.append(str_n)
    list_len = sorted(s3)   
    for num in list_len:
        for file in list_text:
            s1 = open((file), encoding = 'utf8').readlines()
            if len(s1) == num:
                print(file)
                print(num)
                s2 = open((file), encoding = 'utf8').read()
                print(s2)
                print('\n')
                                               
                f.write(file)
                f.write('\n')
                f.write(f'{num}')
                f.write('\n')
                f.write(s2)
                f.write('\n')