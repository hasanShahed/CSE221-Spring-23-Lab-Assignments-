# -*- coding: utf-8 -*-
"""CSE221 Lab 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10VqbvoyF83A34MCldtFwhwn59O2oKq4K
"""

#2
class heapsort():
  def heapify(self,arr,idx):
    if idx <= 1:
      return arr
    else:
      i = idx
      while i >=1:
        parent = i//2
        if arr[parent] > arr[idx]:
          return arr
        else:
          temp = arr[idx]
          arr[idx] = arr[parent]
          arr[parent] = temp

  def add(self,arr,key):
    arr.append(key)
    self.size += 1
    self.heapify(arr,self.size)

  def build(self,arr):
    self.heap = [0]
    self.size = 0
    if type(arr) == list:
      for i in range(len(arr)):
        self.add(self.heap,arr[i])
    else:
      self.add(self.heap,arr)
    return self.heap

  def sink(self, idx):
    if self.size == 0:
      return self.heap
    else:
      left = 2*idx
      right = 2*idx + 1
      if right <= self.size:
        if self.heap[left] < self.heap[right]:
          temp = self.heap[idx]
          self.heap[idx] = self.heap[right]
          self.heap[right] = temp
          if self.heap[left]<self.heap[right]:
            self.sink(right)
          else:
            self.sink(left)
        else:
          temp = self.heap[idx]
          self.heap[idx] = self.heap[left]
          self.heap[left] = temp
      else:
        temp = self.heap[idx]
        self.heap[idx] = self.heap[left]
        self.heap[left] = temp

  def delete(self):
    if self.size == 0:
      return self.heap
    else:
      temp = self.heap[1]
      self.heap[1] = self.heap[self.size]
      self.heap[self.size] = temp
      self.size -= 1
      self.sink(1)

inp = open('/content/input2.txt','r')
read = inp.readlines()
arr_1 = read[0].split(' ')
arr = []
for i in arr_1:
  arr.append(int(i))

print(arr)
a = heapsort()
a.build(arr)