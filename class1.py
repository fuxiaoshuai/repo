#!/usr/bin/python
# -*- coding=utf-8 -*-
class suan():
    def __init__(self,passx,passy):
        self.x = passx
        self.y = passy
    def num(self):
        print("%s + %s = %s" %(self.x,self.y,self.x + self.y))
    def nux(self):
        return ("%s - %s = %s" %(self.x,self.y,self.x - self.y))

if __name__ == '__main__':
    dada = suan(9,3)
    dada.num()
    print(dada.nux())

