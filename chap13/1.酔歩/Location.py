# -*- coding: utf-8 -*-

# 酔歩のLocationクラス

class Location(object):
    def __init__(self, x, y):
        """x と y は浮動小数点数"""
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        """deltaX と deltaY は浮動小数点数"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist ** 2 + yDist ** 2)**0.5
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
        
    
