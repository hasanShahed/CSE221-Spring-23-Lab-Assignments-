# -*- coding: utf-8 -*-
"""Task2_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYWlFi5e-6eim6aupC_SyTe4WyM-3F4K
"""

inp = open('/content/input2_1.txt','r')
out = open('/content/output2_1.txt','w')

read = inp.readlines()
a = int(read[0].replace('\n',''))
b = int(read[2].replace('\n',''))
arr_1 = read[1].split(' ')
arr_1[a-1] = arr_1[a-1].replace('\n','')
arr_2 = read[3].split(' ')
arr_2[b-1] = arr_2[b-1].replace('\n','')
arr = []
for i in arr_1:
  arr.append(int(i))
for i in arr_2:
  arr.append(int(i))
arr.sort()
for i in arr:
  temp = str(i)+' '
  out.write(temp)
inp.close()
out.close()