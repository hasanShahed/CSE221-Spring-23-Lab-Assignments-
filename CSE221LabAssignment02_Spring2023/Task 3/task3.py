# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYWlFi5e-6eim6aupC_SyTe4WyM-3F4K
"""

#3
inp = open('/content/input3.txt','r')
out = open('/content/output3.txt','w')
read = inp.readlines()
lst = read[1].split(' ')
read_1 = []
for i in lst:
  if i != ' ':
    read_1.append(int(i))
def merge(a,b):
  arr = []
  p1 = 0
  p2 = 0
  while p1 != len(a) and p2 != len(b):
    if a[p1]<b[p2]:
      arr.append(a[p1])
      p1 += 1
    elif a[p1] == b[p2]:
      arr.append(a[p1])
      arr.append(b[p2])
      p1 += 1
      p2 += 1
    else:
      arr.append(b[p2])
      p2 += 1
  while p1 < len(a):
    arr.append(a[p1])
    p1 += 1
  while p2 < len(b):
    arr.append(b[p2])
    p2 += 1
  return arr

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    return merge(a1, a2)
sorted = mergeSort(read_1)
for i in sorted:
  out.write(str(i)+' ')

inp.close()
out.close()