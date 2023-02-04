# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:30:45 2023

@author: Charles_Truscott

runfile('C:/Users/Charles_Truscott/Desktop/binarytreeCharlesTruscott.py', wdir='C:/Users/Charles_Truscott/Desktop')
None
Location: 0b0 Key: 2 Left Pointer: 0b0 Right Pointer: 0b1 Parent Pointer: 0b0
Location: 0b1 Key: 4 Left Pointer: 0b10 Right Pointer: 0b11 Parent Pointer: 0b0
Location: 0b10 Key: 8 Left Pointer: 0b100 Right Pointer: 0b101 Parent Pointer: 0b1
Location: 0b11 Key: 16 Left Pointer: 0b110 Right Pointer: 0b111 Parent Pointer: 0b1
Location: 0b100 Key: 32 Left Pointer: 0b1000 Right Pointer: 0b1001 Parent Pointer: 0b10
Location: 0b101 Key: 64 Left Pointer: 0b1010 Right Pointer: 0b1011 Parent Pointer: 0b10
Location: 0b110 Key: 128 Left Pointer: 0b1100 Right Pointer: 0b1101 Parent Pointer: 0b11
Location: 0b111 Key: 256 Left Pointer: 0b1110 Right Pointer: 0b1111 Parent Pointer: 0b11
Location: 0b1000 Key: 512 Left Pointer: 0b10000 Right Pointer: 0b10001 Parent Pointer: 0b100
Location: 0b1001 Key: 1024 Left Pointer: 0b10010 Right Pointer: 0b10011 Parent Pointer: 0b100
Location: 0b1010 Key: 2048 Left Pointer: 0b10100 Right Pointer: 0b10101 Parent Pointer: 0b101
Location: 0b1011 Key: 4096 Left Pointer: 0b10110 Right Pointer: 0b10111 Parent Pointer: 0b101
Location: 0b1100 Key: 8192 Left Pointer: 0b11000 Right Pointer: 0b11001 Parent Pointer: 0b110
Location: 0b1101 Key: 16384 Left Pointer: 0b11010 Right Pointer: 0b11011 Parent Pointer: 0b110
Location: 0b1110 Key: 32768 Left Pointer: 0b11100 Right Pointer: 0b11101 Parent Pointer: 0b111
Location: 0b1111 Key: 65536 Left Pointer: 0b11110 Right Pointer: 0b11111 Parent Pointer: 0b111
Location: 0b10000 Key: 131072 Left Pointer: 0b100000 Right Pointer: 0b100001 Parent Pointer: 0b1000
Location: 0b10001 Key: 262144 Left Pointer: 0b100010 Right Pointer: 0b100011 Parent Pointer: 0b1000
Location: 0b10010 Key: 524288 Left Pointer: 0b100100 Right Pointer: 0b100101 Parent Pointer: 0b1001
Location: 0b10011 Key: 1048576 Left Pointer: 0b100110 Right Pointer: 0b100111 Parent Pointer: 0b1001
Location: 0b10100 Key: 2097152 Left Pointer: 0b101000 Right Pointer: 0b101001 Parent Pointer: 0b1010
Location: 0b10101 Key: 4194304 Left Pointer: 0b101010 Right Pointer: 0b101011 Parent Pointer: 0b1010
Location: 0b10110 Key: 8388608 Left Pointer: 0b101100 Right Pointer: 0b101101 Parent Pointer: 0b1011
Location: 0b10111 Key: 16777216 Left Pointer: 0b101110 Right Pointer: 0b101111 Parent Pointer: 0b1011
Location: 0b11000 Key: 33554432 Left Pointer: 0b110000 Right Pointer: 0b110001 Parent Pointer: 0b1100
Location: 0b11001 Key: 67108864 Left Pointer: 0b110010 Right Pointer: 0b110011 Parent Pointer: 0b1100
Location: 0b11010 Key: 134217728 Left Pointer: 0b110100 Right Pointer: 0b110101 Parent Pointer: 0b1101
Location: 0b11011 Key: 268435456 Left Pointer: 0b110110 Right Pointer: 0b110111 Parent Pointer: 0b1101
Location: 0b11100 Key: 536870912 Left Pointer: 0b111000 Right Pointer: 0b111001 Parent Pointer: 0b1110
Location: 0b11101 Key: 1073741824 Left Pointer: 0b111010 Right Pointer: 0b111011 Parent Pointer: 0b1110
Location: 0b11110 Key: 2147483648 Left Pointer: 0b111100 Right Pointer: 0b111101 Parent Pointer: 0b1111
Location: 0b11111 Key: 4294967296 Left Pointer: 0b111110 Right Pointer: 0b111111 Parent Pointer: 0b1111
Charles Thomas Wallace Truscott Watters. Binary Tree


"""


class Node(object):
    def __init__(self, key):
        self.key = key
    def get_key(self):
        return self.key
        
class BinaryTree(object):
    def __init__(self):
        self.nodes = []
        self.loc = 0
    def add_node(self, key):
        self.nodes.append(list([self.loc, Node(key), 2 * self.loc, 2 * self.loc + 1, 0 if self.loc == 0 else self.loc // 2]))
        self.loc += 1
    def get_loc(self, key):
        for node in self.nodes:
            n = node[1]
            if n.get_key() == key:
                return bin(node[0])
    def get_keys(self):
        for node in self.nodes:
            print("Location: {} Key: {} Left Pointer: {} Right Pointer: {} Parent Pointer: {}".format(bin(node[0]), node[1].get_key(), bin(node[2]), bin(node[3]), bin(node[4])))

B = BinaryTree()
n = 2
for x in range(1, 32 + 1, 1):
    c = n ** x
    B.add_node(c)
    
    
print(B.get_loc('64'))
B.get_keys()
print("Charles Thomas Wallace Truscott Watters. Binary Tree")