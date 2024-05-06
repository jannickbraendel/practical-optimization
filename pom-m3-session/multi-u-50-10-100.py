#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:37:02 2020

@author: luebbecke
"""

# hard

I=50 #items
B=10 #bins
R=100 #resources 

required = [[1, 2, 0, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 1, 1, 0, 1, 1, 0, 2, 2, 2, 1, 2, 1, 1, 2, 0, 0, 1, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 0, 2, 1, 2, 1, 2, 0, 14, 18, 18, 17, 15, 15, 11, 18, 16, 14, 15, 17, 14, 11, 17, 16, 17, 20, 12, 12, 11, 13, 11, 10, 10, 17, 10, 10, 15, 12, 14, 10, 18, 11, 17, 10, 13, 15, 19, 14, 12, 14, 15, 19, 20, 18, 20, 15, 19, 20], [1, 0, 2, 1, 1, 2, 0, 2, 1, 1, 0, 1, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 2, 1, 1, 0, 0, 1, 1, 1, 2, 2, 1, 0, 2, 1, 2, 1, 0, 1, 2, 1, 0, 1, 10, 17, 16, 17, 14, 10, 12, 20, 17, 17, 12, 12, 14, 15, 14, 11, 18, 17, 19, 17, 11, 20, 15, 13, 10, 12, 11, 17, 14, 17, 16, 15, 20, 15, 20, 15, 10, 20, 17, 10, 10, 12, 13, 12, 19, 14, 20, 16, 15, 17], [2, 0, 1, 1, 0, 1, 0, 2, 2, 1, 2, 1, 1, 0, 0, 1, 0, 0, 1, 2, 1, 1, 1, 2, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0, 0, 2, 2, 2, 0, 1, 1, 2, 2, 2, 11, 15, 16, 14, 13, 10, 13, 20, 15, 18, 17, 10, 10, 13, 20, 11, 15, 15, 15, 19, 11, 18, 12, 19, 19, 20, 17, 10, 17, 16, 17, 16, 17, 13, 18, 14, 16, 18, 10, 14, 17, 17, 13, 12, 11, 15, 20, 11, 19, 10], [0, 1, 0, 2, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 2, 1, 1, 0, 0, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 1, 0, 11, 12, 14, 11, 17, 10, 17, 10, 11, 10, 16, 17, 19, 10, 15, 13, 14, 13, 19, 19, 18, 16, 16, 11, 14, 18, 16, 14, 12, 10, 11, 19, 12, 13, 10, 14, 12, 12, 19, 10, 10, 16, 11, 16, 15, 20, 14, 20, 16, 11], [0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0, 2, 1, 2, 0, 0, 0, 1, 2, 2, 1, 2, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 1, 2, 0, 0, 2, 2, 0, 2, 1, 2, 20, 14, 18, 10, 19, 19, 10, 13, 10, 11, 16, 13, 17, 19, 12, 14, 11, 12, 14, 15, 11, 12, 19, 16, 13, 19, 13, 16, 16, 20, 18, 17, 11, 16, 16, 18, 20, 15, 20, 15, 17, 16, 20, 20, 20, 16, 10, 17, 12, 18], [2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 1, 2, 2, 0, 2, 1, 2, 0, 2, 1, 1, 2, 0, 0, 0, 1, 2, 0, 2, 2, 1, 0, 0, 2, 2, 1, 1, 1, 2, 0, 2, 1, 2, 10, 15, 20, 17, 15, 20, 20, 18, 11, 19, 10, 13, 15, 11, 19, 13, 11, 20, 14, 17, 14, 10, 13, 17, 14, 17, 16, 19, 20, 15, 10, 10, 16, 12, 12, 19, 18, 13, 17, 15, 11, 20, 10, 10, 16, 13, 11, 10, 20, 13], [1, 0, 1, 1, 2, 0, 0, 1, 2, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 2, 0, 2, 1, 2, 0, 1, 1, 1, 2, 2, 1, 2, 2, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 2, 1, 1, 1, 2, 2, 10, 13, 12, 20, 18, 17, 12, 12, 12, 17, 15, 16, 13, 12, 14, 14, 10, 14, 10, 15, 19, 20, 13, 18, 10, 16, 11, 20, 11, 15, 10, 16, 20, 12, 11, 19, 17, 17, 16, 12, 10, 19, 20, 20, 16, 17, 19, 19, 10, 17], [0, 2, 1, 2, 1, 0, 2, 0, 0, 1, 2, 0, 0, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 1, 0, 2, 2, 1, 0, 0, 1, 0, 0, 1, 0, 1, 2, 17, 11, 16, 15, 10, 13, 13, 12, 19, 17, 16, 17, 11, 15, 20, 20, 15, 19, 19, 12, 13, 15, 18, 10, 20, 18, 16, 12, 18, 16, 18, 16, 14, 10, 15, 19, 13, 18, 19, 16, 18, 12, 14, 11, 18, 13, 13, 14, 11, 18], [1, 0, 1, 1, 2, 1, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 2, 1, 0, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 0, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 0, 1, 1, 17, 17, 19, 19, 13, 17, 15, 18, 16, 14, 11, 18, 17, 11, 18, 20, 19, 20, 13, 18, 10, 16, 12, 14, 17, 10, 19, 14, 12, 10, 16, 13, 17, 18, 11, 15, 17, 17, 20, 16, 10, 11, 11, 10, 12, 11, 18, 14, 19, 13], [2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 1, 0, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 2, 2, 0, 2, 2, 1, 0, 0, 1, 2, 1, 0, 2, 19, 15, 16, 15, 18, 13, 10, 19, 16, 10, 15, 12, 11, 10, 15, 13, 11, 13, 18, 16, 19, 15, 16, 17, 20, 10, 11, 12, 17, 15, 15, 20, 12, 16, 11, 17, 11, 17, 13, 13, 17, 20, 15, 20, 12, 10, 19, 11, 15, 15], [1, 0, 2, 1, 1, 1, 2, 2, 2, 0, 1, 1, 0, 1, 0, 2, 1, 2, 1, 2, 1, 1, 2, 1, 0, 2, 1, 2, 0, 0, 0, 0, 1, 2, 2, 0, 0, 2, 1, 0, 2, 1, 0, 0, 2, 1, 2, 1, 1, 2, 10, 14, 11, 18, 18, 17, 16, 11, 11, 15, 11, 10, 10, 14, 15, 11, 10, 19, 18, 19, 20, 10, 18, 14, 12, 20, 16, 17, 11, 18, 15, 17, 11, 20, 19, 11, 12, 14, 12, 17, 11, 14, 13, 10, 13, 19, 17, 17, 15, 11], [0, 1, 1, 0, 2, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 2, 2, 20, 19, 15, 16, 17, 17, 20, 15, 13, 20, 15, 19, 17, 11, 11, 11, 19, 14, 16, 12, 17, 13, 14, 18, 13, 14, 11, 15, 19, 15, 18, 13, 11, 17, 16, 14, 16, 18, 11, 19, 13, 16, 14, 18, 16, 11, 19, 19, 15, 11], [1, 0, 1, 2, 2, 0, 0, 2, 1, 1, 0, 1, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 1, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 1, 1, 2, 0, 2, 0, 0, 1, 1, 1, 0, 2, 1, 1, 0, 11, 15, 15, 12, 13, 13, 20, 17, 12, 10, 10, 15, 17, 16, 17, 14, 17, 19, 18, 15, 17, 14, 12, 10, 14, 14, 15, 18, 20, 15, 17, 14, 13, 10, 16, 12, 17, 15, 12, 20, 16, 12, 20, 18, 14, 17, 12, 13, 13, 18], [2, 1, 1, 0, 2, 1, 0, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 0, 0, 0, 2, 1, 1, 0, 0, 2, 1, 0, 1, 1, 0, 1, 2, 2, 0, 1, 2, 2, 1, 0, 2, 1, 1, 0, 1, 2, 12, 20, 19, 20, 17, 14, 16, 14, 12, 11, 14, 10, 11, 20, 10, 11, 11, 10, 16, 13, 20, 13, 15, 13, 16, 13, 12, 18, 10, 13, 11, 19, 19, 15, 18, 18, 11, 18, 14, 19, 11, 13, 15, 17, 11, 19, 18, 15, 13, 12], [1, 2, 1, 2, 1, 1, 0, 1, 2, 0, 2, 2, 2, 0, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 1, 0, 0, 0, 2, 1, 1, 2, 2, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 20, 15, 10, 14, 18, 16, 20, 16, 14, 20, 13, 17, 12, 17, 11, 17, 11, 14, 14, 18, 11, 10, 18, 20, 20, 10, 16, 18, 11, 13, 11, 15, 20, 11, 18, 20, 15, 13, 17, 20, 18, 13, 11, 12, 10, 17, 10, 13, 19, 10], [0, 0, 2, 0, 1, 0, 2, 0, 0, 1, 1, 0, 0, 2, 0, 1, 1, 0, 0, 0, 1, 1, 2, 0, 1, 1, 0, 0, 0, 2, 1, 0, 1, 2, 2, 0, 2, 0, 2, 0, 0, 1, 0, 1, 2, 1, 1, 2, 1, 1, 11, 16, 17, 10, 17, 13, 18, 11, 10, 12, 14, 18, 13, 11, 19, 16, 16, 19, 20, 12, 17, 14, 14, 10, 18, 14, 13, 20, 10, 14, 14, 20, 11, 18, 19, 17, 15, 19, 18, 16, 10, 17, 15, 18, 11, 12, 13, 18, 20, 19], [0, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 1, 2, 2, 0, 2, 2, 2, 0, 0, 0, 1, 2, 1, 0, 1, 2, 1, 0, 2, 2, 2, 0, 0, 1, 2, 1, 1, 1, 2, 0, 0, 0, 1, 0, 2, 16, 20, 20, 12, 19, 13, 10, 11, 19, 10, 19, 17, 11, 19, 14, 20, 17, 18, 10, 13, 15, 17, 16, 11, 14, 19, 19, 19, 19, 15, 12, 16, 20, 10, 19, 18, 16, 20, 11, 11, 20, 13, 14, 13, 12, 15, 20, 12, 19, 18], [1, 1, 1, 2, 0, 0, 2, 0, 2, 2, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 1, 2, 0, 1, 2, 0, 2, 1, 0, 1, 2, 2, 2, 0, 2, 0, 0, 2, 2, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 2, 17, 14, 10, 12, 20, 20, 15, 10, 19, 11, 17, 16, 15, 17, 16, 18, 14, 13, 19, 11, 12, 11, 14, 15, 13, 17, 14, 14, 13, 10, 20, 13, 19, 13, 14, 18, 18, 18, 11, 20, 14, 17, 12, 18, 15, 20, 10, 10, 18, 20], [0, 0, 2, 2, 2, 0, 1, 0, 2, 2, 0, 0, 2, 1, 0, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 0, 2, 1, 1, 2, 0, 0, 1, 1, 0, 1, 2, 2, 1, 2, 0, 0, 2, 2, 1, 1, 0, 2, 2, 0, 16, 12, 14, 18, 18, 12, 14, 19, 16, 12, 17, 10, 11, 10, 16, 17, 14, 13, 12, 14, 14, 10, 11, 13, 10, 18, 17, 16, 12, 12, 13, 12, 19, 20, 20, 12, 11, 18, 13, 12, 18, 10, 20, 15, 15, 19, 18, 10, 14, 15], [2, 1, 2, 2, 1, 0, 2, 0, 2, 0, 2, 2, 1, 2, 2, 0, 1, 2, 0, 2, 2, 1, 0, 0, 0, 0, 1, 0, 1, 1, 2, 0, 2, 1, 0, 2, 2, 1, 1, 2, 2, 0, 0, 1, 0, 1, 2, 1, 0, 0, 10, 12, 14, 11, 10, 12, 12, 11, 15, 16, 20, 11, 11, 19, 16, 19, 18, 13, 19, 20, 16, 18, 14, 12, 11, 13, 17, 15, 12, 16, 14, 20, 12, 14, 18, 18, 10, 18, 13, 10, 14, 17, 16, 20, 14, 13, 14, 14, 20, 14], [1, 0, 1, 1, 0, 2, 1, 2, 1, 0, 1, 2, 1, 0, 2, 2, 1, 0, 2, 2, 2, 2, 0, 0, 2, 1, 0, 0, 1, 1, 2, 2, 1, 0, 1, 2, 0, 1, 1, 0, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 20, 10, 10, 18, 20, 17, 16, 20, 10, 18, 16, 13, 14, 12, 13, 15, 20, 19, 12, 16, 20, 18, 12, 11, 10, 13, 20, 12, 18, 13, 12, 17, 11, 11, 18, 19, 13, 12, 16, 13, 16, 14, 17, 16, 14, 11, 15, 13, 11, 16], [0, 0, 2, 2, 1, 2, 0, 2, 0, 0, 1, 0, 2, 1, 2, 0, 2, 1, 1, 0, 0, 1, 1, 0, 0, 2, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 2, 1, 2, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 16, 14, 20, 15, 14, 16, 15, 15, 20, 19, 17, 13, 17, 13, 13, 18, 17, 15, 13, 13, 19, 11, 18, 13, 10, 15, 10, 13, 15, 15, 14, 13, 16, 10, 12, 11, 16, 19, 15, 14, 16, 17, 11, 19, 11, 12, 12, 16, 19, 20], [2, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 1, 2, 0, 1, 0, 2, 2, 0, 2, 1, 1, 0, 2, 1, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 1, 2, 2, 0, 0, 1, 20, 18, 17, 14, 10, 16, 11, 17, 10, 19, 16, 11, 12, 14, 11, 17, 17, 15, 10, 13, 10, 14, 14, 14, 17, 13, 14, 12, 20, 20, 17, 13, 15, 15, 16, 13, 18, 20, 20, 14, 14, 16, 19, 13, 11, 10, 11, 20, 14, 18], [2, 0, 0, 2, 2, 1, 2, 0, 1, 1, 2, 2, 1, 0, 0, 0, 0, 1, 1, 2, 0, 1, 0, 1, 2, 1, 0, 1, 2, 2, 2, 1, 2, 2, 0, 1, 0, 2, 0, 1, 0, 2, 2, 0, 0, 0, 2, 1, 0, 1, 11, 17, 16, 14, 14, 16, 14, 13, 11, 12, 13, 13, 17, 17, 17, 19, 20, 19, 13, 11, 11, 14, 11, 10, 20, 14, 17, 15, 20, 13, 16, 11, 12, 15, 14, 11, 14, 11, 11, 14, 18, 18, 10, 13, 10, 10, 14, 18, 11, 18], [0, 1, 2, 2, 1, 0, 1, 2, 1, 0, 0, 2, 0, 1, 0, 2, 1, 1, 1, 2, 0, 0, 2, 2, 1, 1, 0, 1, 2, 1, 1, 0, 1, 0, 1, 2, 0, 0, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 11, 15, 18, 18, 13, 13, 20, 20, 13, 17, 11, 16, 18, 17, 12, 20, 20, 14, 11, 11, 11, 11, 18, 18, 10, 16, 10, 14, 18, 14, 12, 20, 14, 10, 15, 20, 14, 20, 13, 17, 16, 14, 10, 11, 15, 14, 17, 14, 20, 13], [1, 1, 0, 2, 1, 0, 2, 0, 0, 2, 2, 0, 1, 2, 1, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1, 2, 1, 2, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 2, 1, 0, 20, 16, 17, 14, 18, 14, 13, 19, 16, 19, 16, 16, 13, 10, 17, 18, 13, 13, 18, 13, 14, 18, 12, 20, 20, 18, 19, 11, 15, 14, 10, 15, 17, 13, 20, 12, 17, 13, 14, 12, 12, 14, 16, 18, 13, 17, 19, 15, 10, 10], [0, 2, 1, 2, 1, 2, 1, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 2, 0, 2, 0, 0, 1, 1, 1, 2, 2, 2, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 1, 2, 2, 19, 13, 18, 19, 10, 10, 19, 20, 19, 18, 10, 15, 14, 15, 20, 16, 10, 19, 17, 16, 11, 11, 10, 14, 16, 14, 17, 12, 13, 17, 13, 16, 12, 15, 13, 18, 10, 11, 13, 11, 17, 10, 11, 17, 10, 16, 20, 10, 16, 16], [0, 2, 0, 2, 2, 1, 2, 0, 1, 2, 0, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 2, 1, 1, 2, 1, 1, 0, 2, 2, 0, 0, 1, 2, 1, 0, 0, 2, 0, 2, 12, 13, 17, 13, 13, 20, 11, 10, 11, 11, 15, 18, 13, 13, 14, 20, 18, 10, 15, 20, 10, 19, 13, 17, 19, 14, 18, 12, 11, 15, 10, 18, 10, 14, 20, 17, 14, 20, 11, 19, 16, 17, 15, 15, 10, 11, 14, 12, 18, 17], [1, 1, 2, 1, 0, 1, 1, 2, 1, 2, 2, 2, 0, 1, 2, 2, 1, 2, 0, 2, 0, 0, 0, 0, 2, 1, 0, 1, 1, 2, 1, 0, 1, 1, 1, 0, 2, 2, 0, 1, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 17, 13, 14, 17, 17, 19, 19, 20, 15, 13, 17, 14, 10, 14, 16, 15, 11, 19, 12, 15, 12, 12, 12, 11, 15, 17, 19, 12, 20, 10, 16, 15, 17, 13, 12, 11, 14, 20, 13, 17, 13, 18, 12, 18, 19, 13, 20, 17, 13, 12], [1, 1, 0, 0, 2, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 1, 2, 0, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 2, 0, 1, 0, 1, 0, 2, 2, 2, 1, 1, 1, 18, 13, 17, 17, 12, 20, 11, 20, 14, 17, 14, 20, 19, 20, 15, 12, 16, 19, 18, 13, 14, 11, 16, 15, 11, 15, 16, 20, 16, 13, 15, 16, 10, 10, 15, 19, 17, 19, 11, 15, 10, 10, 10, 12, 19, 19, 18, 12, 11, 20], [1, 0, 2, 2, 1, 2, 2, 0, 0, 0, 2, 2, 1, 1, 2, 1, 0, 1, 0, 1, 1, 0, 2, 1, 1, 0, 2, 1, 2, 2, 0, 0, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 2, 2, 1, 1, 1, 0, 1, 0, 19, 18, 12, 15, 15, 19, 16, 15, 15, 17, 16, 18, 18, 14, 16, 17, 20, 19, 12, 12, 14, 13, 11, 15, 19, 20, 11, 14, 10, 20, 16, 16, 14, 10, 13, 18, 13, 16, 17, 16, 16, 12, 17, 18, 14, 11, 18, 19, 14, 20], [1, 2, 0, 2, 2, 2, 0, 1, 0, 0, 0, 1, 2, 0, 0, 1, 0, 1, 1, 2, 1, 1, 2, 0, 2, 0, 1, 0, 0, 1, 2, 2, 2, 0, 2, 2, 1, 0, 1, 0, 2, 0, 2, 0, 1, 0, 2, 2, 1, 1, 17, 18, 14, 10, 11, 16, 19, 19, 16, 16, 11, 13, 15, 13, 19, 20, 11, 14, 18, 15, 15, 12, 14, 15, 13, 20, 15, 16, 15, 19, 20, 14, 18, 20, 13, 15, 10, 15, 19, 17, 18, 12, 15, 14, 18, 17, 17, 19, 12, 20], [0, 2, 1, 0, 1, 1, 1, 0, 2, 2, 1, 2, 2, 2, 0, 1, 1, 2, 1, 2, 2, 0, 2, 2, 2, 2, 0, 1, 2, 1, 2, 2, 0, 2, 0, 2, 0, 2, 1, 0, 2, 1, 0, 1, 0, 1, 1, 1, 1, 2, 16, 10, 11, 15, 15, 16, 20, 19, 17, 11, 17, 13, 17, 18, 10, 18, 15, 14, 12, 15, 15, 20, 20, 20, 19, 20, 20, 13, 20, 20, 18, 13, 15, 16, 20, 14, 15, 20, 12, 13, 20, 20, 11, 18, 14, 14, 12, 13, 15, 13], [2, 2, 1, 1, 1, 0, 2, 0, 2, 1, 1, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 2, 1, 0, 1, 0, 2, 2, 1, 0, 2, 0, 2, 1, 0, 1, 2, 0, 0, 0, 2, 2, 0, 17, 14, 14, 12, 15, 10, 15, 16, 10, 20, 10, 10, 12, 19, 19, 16, 19, 20, 11, 14, 14, 17, 18, 16, 16, 10, 10, 10, 16, 16, 10, 19, 19, 12, 19, 19, 17, 20, 19, 15, 13, 15, 15, 10, 18, 11, 15, 15, 15, 17], [0, 1, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 1, 2, 2, 0, 2, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 17, 19, 14, 18, 18, 15, 17, 12, 17, 11, 17, 14, 16, 12, 17, 11, 11, 19, 10, 11, 10, 13, 14, 11, 15, 17, 19, 17, 18, 15, 20, 19, 15, 20, 15, 18, 11, 12, 11, 11, 10, 19, 13, 16, 13, 11, 18, 14, 11, 10], [1, 0, 1, 1, 2, 2, 2, 0, 2, 0, 1, 1, 2, 2, 1, 2, 2, 0, 2, 0, 1, 0, 0, 1, 0, 1, 1, 2, 1, 0, 1, 1, 1, 1, 2, 0, 2, 0, 1, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 1, 20, 16, 10, 12, 13, 16, 16, 19, 18, 13, 10, 14, 12, 10, 15, 13, 12, 12, 18, 19, 17, 15, 16, 19, 17, 12, 18, 17, 10, 16, 14, 11, 16, 19, 16, 19, 10, 17, 20, 19, 15, 17, 20, 11, 12, 13, 15, 13, 13, 10], [2, 1, 0, 1, 0, 1, 2, 2, 2, 0, 1, 2, 1, 0, 2, 1, 1, 0, 1, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 0, 2, 2, 1, 0, 1, 2, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 13, 19, 13, 17, 15, 11, 15, 16, 16, 13, 19, 14, 12, 16, 20, 10, 15, 13, 11, 19, 16, 16, 15, 13, 20, 10, 18, 20, 10, 19, 12, 18, 12, 10, 10, 13, 15, 10, 12, 16, 20, 17, 18, 10, 12, 20, 14, 11, 17, 13], [0, 2, 0, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 1, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 2, 0, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 0, 2, 1, 0, 19, 17, 10, 19, 17, 11, 15, 12, 10, 13, 16, 18, 17, 12, 20, 14, 13, 16, 16, 13, 17, 12, 10, 10, 20, 16, 18, 14, 18, 19, 10, 20, 14, 17, 10, 10, 10, 20, 16, 16, 11, 12, 16, 15, 17, 11, 12, 18, 17, 17], [2, 1, 1, 1, 2, 1, 2, 0, 2, 1, 0, 1, 2, 0, 1, 0, 2, 2, 2, 1, 1, 2, 2, 0, 0, 2, 1, 1, 1, 2, 2, 0, 1, 2, 2, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 20, 10, 17, 15, 11, 20, 18, 10, 16, 20, 12, 20, 12, 17, 19, 16, 12, 18, 16, 15, 11, 14, 19, 20, 12, 11, 12, 15, 15, 15, 16, 10, 18, 11, 18, 17, 14, 18, 20, 18, 18, 20, 17, 11, 10, 17, 16, 14, 15, 10], [2, 2, 2, 2, 1, 0, 2, 1, 0, 0, 0, 2, 1, 0, 0, 1, 1, 0, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 2, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 2, 1, 1, 2, 1, 0, 1, 1, 2, 13, 17, 15, 11, 15, 20, 19, 14, 12, 19, 14, 10, 10, 19, 17, 16, 15, 14, 17, 16, 19, 13, 17, 20, 20, 13, 20, 20, 15, 18, 20, 15, 19, 13, 20, 14, 17, 10, 14, 10, 10, 18, 13, 16, 17, 12, 14, 12, 18, 12], [0, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 2, 2, 0, 1, 0, 2, 2, 2, 0, 1, 0, 2, 2, 1, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 0, 2, 0, 2, 13, 19, 18, 19, 19, 12, 17, 11, 13, 15, 20, 12, 12, 15, 17, 16, 17, 14, 18, 16, 20, 16, 12, 19, 13, 14, 11, 12, 20, 15, 11, 18, 16, 19, 13, 11, 10, 18, 20, 16, 20, 17, 12, 16, 15, 14, 15, 10, 12, 11], [1, 0, 1, 0, 0, 2, 1, 2, 0, 2, 0, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 2, 2, 2, 1, 0, 2, 2, 1, 0, 0, 2, 1, 2, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 18, 18, 12, 19, 19, 14, 19, 20, 11, 15, 20, 20, 13, 20, 12, 16, 18, 16, 16, 14, 13, 14, 16, 15, 17, 19, 14, 14, 20, 13, 19, 17, 17, 13, 18, 20, 11, 11, 16, 16, 17, 15, 15, 13, 11, 20, 12, 20, 12, 10], [1, 2, 1, 0, 0, 1, 0, 1, 1, 0, 2, 0, 0, 2, 0, 1, 2, 1, 2, 2, 1, 0, 1, 0, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 2, 2, 2, 0, 0, 1, 2, 0, 2, 1, 1, 2, 1, 10, 16, 18, 13, 18, 20, 11, 10, 12, 11, 20, 14, 16, 19, 17, 13, 13, 14, 15, 20, 12, 14, 17, 20, 18, 13, 15, 11, 18, 15, 14, 17, 14, 16, 12, 20, 13, 12, 11, 11, 10, 20, 15, 10, 10, 14, 16, 10, 13, 20], [1, 1, 0, 1, 2, 2, 1, 2, 0, 1, 2, 0, 2, 2, 1, 0, 2, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 2, 0, 1, 2, 2, 0, 0, 2, 1, 0, 0, 13, 20, 19, 18, 12, 19, 15, 10, 12, 12, 15, 13, 18, 18, 10, 10, 18, 11, 10, 13, 12, 16, 20, 18, 13, 12, 11, 15, 15, 18, 12, 16, 15, 11, 13, 17, 19, 10, 16, 13, 14, 10, 17, 10, 12, 18, 13, 14, 15, 20], [1, 2, 1, 2, 1, 1, 2, 0, 2, 0, 0, 2, 1, 2, 2, 2, 0, 1, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2, 0, 0, 2, 2, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 2, 0, 1, 0, 0, 0, 15, 20, 20, 18, 18, 18, 13, 19, 10, 13, 13, 14, 14, 13, 19, 18, 15, 17, 13, 14, 20, 19, 11, 19, 19, 16, 19, 16, 16, 19, 20, 17, 20, 15, 12, 13, 15, 11, 20, 14, 14, 10, 18, 20, 17, 11, 11, 19, 12, 11], [0, 1, 2, 1, 1, 0, 2, 2, 1, 2, 2, 1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 0, 2, 1, 1, 1, 2, 0, 1, 1, 0, 0, 2, 2, 2, 0, 2, 1, 20, 13, 14, 15, 18, 12, 14, 12, 19, 11, 16, 13, 20, 16, 20, 20, 12, 14, 17, 10, 12, 14, 20, 13, 12, 17, 13, 12, 14, 14, 16, 10, 12, 18, 10, 15, 20, 15, 18, 18, 14, 10, 19, 10, 20, 17, 13, 14, 10, 18], [2, 1, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 1, 2, 0, 1, 1, 0, 2, 2, 2, 1, 1, 2, 0, 1, 0, 2, 1, 0, 1, 2, 2, 1, 1, 2, 2, 2, 0, 1, 0, 2, 1, 1, 2, 1, 2, 0, 0, 2, 10, 19, 11, 16, 20, 12, 13, 13, 16, 18, 18, 11, 18, 15, 15, 11, 12, 18, 11, 18, 20, 20, 13, 16, 20, 14, 11, 12, 11, 10, 17, 16, 15, 15, 17, 13, 12, 11, 11, 17, 16, 11, 15, 15, 15, 14, 20, 18, 15, 11], [0, 2, 2, 2, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 0, 1, 2, 2, 1, 2, 1, 19, 19, 18, 11, 19, 17, 17, 16, 13, 11, 14, 17, 15, 17, 10, 10, 18, 15, 16, 13, 13, 18, 16, 18, 16, 11, 19, 14, 11, 17, 13, 14, 13, 18, 14, 17, 11, 11, 12, 13, 20, 19, 19, 20, 17, 14, 14, 18, 17, 14], [0, 1, 0, 1, 0, 1, 1, 0, 2, 0, 1, 1, 0, 0, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 0, 1, 0, 1, 1, 1, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 2, 12, 17, 16, 19, 18, 18, 14, 12, 16, 17, 13, 13, 18, 12, 14, 20, 14, 17, 17, 19, 12, 15, 19, 10, 12, 10, 12, 14, 12, 14, 20, 14, 18, 17, 18, 18, 19, 10, 14, 15, 18, 12, 13, 15, 17, 20, 17, 20, 16, 10], [0, 1, 1, 2, 0, 0, 2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 2, 1, 2, 2, 2, 1, 1, 1, 0, 0, 1, 1, 2, 2, 0, 2, 0, 1, 1, 0, 2, 2, 2, 0, 19, 15, 18, 18, 10, 14, 18, 13, 12, 16, 17, 15, 18, 18, 18, 13, 17, 20, 10, 11, 18, 15, 13, 20, 15, 13, 12, 10, 12, 17, 15, 16, 11, 19, 14, 17, 13, 20, 12, 15, 19, 10, 20, 12, 20, 18, 11, 10, 16, 11]]
available = [[11, 10, 11, 10, 6, 13, 8, 9, 5, 12, 7, 7, 9, 10, 11, 15, 9, 5, 10, 7, 8, 9, 15, 15, 13, 6, 11, 12, 6, 9, 5, 9, 10, 12, 11, 15, 13, 5, 10, 5, 12, 9, 10, 9, 10, 15, 12, 8, 8, 14, 134, 148, 125, 141, 133, 144, 142, 133, 114, 123, 124, 125, 131, 103, 102, 143, 137, 133, 144, 124, 148, 139, 146, 132, 134, 100, 134, 138, 136, 128, 149, 133, 142, 100, 126, 108, 110, 136, 115, 119, 118, 142, 105, 109, 125, 109, 100, 128, 109, 114], [10, 7, 5, 8, 14, 5, 11, 10, 6, 12, 9, 11, 6, 8, 15, 14, 6, 14, 14, 7, 8, 9, 12, 15, 6, 14, 10, 6, 13, 9, 12, 10, 14, 14, 13, 11, 9, 9, 6, 14, 8, 8, 8, 15, 5, 5, 12, 8, 10, 14, 141, 126, 106, 126, 112, 132, 126, 137, 147, 109, 139, 129, 138, 108, 123, 148, 139, 116, 109, 120, 110, 143, 114, 114, 132, 138, 102, 131, 147, 144, 105, 138, 147, 139, 146, 103, 141, 115, 146, 150, 138, 135, 106, 138, 138, 122, 109, 131, 125, 127], [14, 12, 12, 8, 10, 15, 7, 15, 5, 13, 12, 6, 7, 15, 8, 14, 15, 9, 14, 5, 12, 14, 7, 9, 6, 9, 12, 12, 9, 15, 10, 15, 15, 11, 10, 9, 14, 11, 7, 10, 12, 5, 15, 8, 6, 6, 6, 14, 7, 15, 135, 117, 102, 136, 116, 112, 145, 141, 123, 102, 104, 128, 146, 125, 112, 149, 120, 129, 118, 125, 114, 113, 147, 131, 137, 129, 104, 122, 111, 141, 147, 150, 106, 127, 146, 110, 129, 130, 134, 134, 144, 116, 124, 116, 114, 138, 146, 147, 136, 131], [13, 12, 5, 10, 13, 6, 15, 6, 10, 8, 13, 5, 9, 6, 8, 13, 14, 15, 9, 12, 10, 13, 10, 7, 12, 10, 15, 8, 7, 12, 8, 9, 12, 8, 7, 9, 6, 8, 8, 5, 9, 8, 6, 6, 11, 12, 15, 6, 6, 15, 116, 105, 126, 112, 119, 126, 130, 128, 130, 113, 122, 147, 127, 130, 143, 145, 115, 112, 115, 112, 119, 109, 135, 116, 137, 125, 142, 132, 114, 119, 118, 101, 102, 127, 114, 108, 113, 102, 112, 126, 101, 125, 144, 143, 131, 125, 131, 149, 146, 107], [12, 14, 10, 6, 12, 8, 10, 12, 11, 12, 7, 9, 6, 6, 6, 15, 8, 9, 5, 11, 9, 9, 5, 11, 13, 7, 6, 14, 9, 12, 12, 14, 9, 14, 6, 13, 10, 8, 13, 12, 11, 6, 11, 5, 15, 5, 8, 5, 6, 9, 113, 126, 124, 130, 132, 127, 138, 150, 128, 140, 109, 136, 100, 102, 147, 128, 129, 128, 114, 124, 145, 103, 125, 140, 100, 115, 120, 105, 122, 102, 149, 114, 139, 146, 127, 106, 125, 101, 119, 127, 134, 135, 118, 149, 136, 111, 136, 116, 124, 121], [15, 9, 11, 8, 14, 14, 12, 10, 15, 12, 14, 14, 5, 11, 11, 13, 14, 12, 11, 15, 13, 15, 10, 12, 12, 8, 13, 9, 12, 11, 12, 6, 13, 15, 13, 11, 9, 5, 15, 9, 8, 7, 13, 9, 5, 12, 5, 15, 13, 12, 122, 137, 135, 128, 140, 115, 102, 145, 143, 148, 112, 105, 144, 144, 138, 103, 120, 149, 116, 137, 146, 113, 127, 144, 113, 136, 147, 114, 140, 130, 124, 104, 119, 102, 111, 109, 144, 141, 123, 143, 124, 108, 110, 125, 113, 132, 106, 124, 148, 119], [5, 11, 11, 11, 10, 10, 15, 8, 5, 13, 7, 12, 9, 12, 10, 12, 7, 14, 12, 8, 6, 7, 11, 8, 10, 11, 15, 11, 15, 7, 15, 14, 15, 10, 10, 8, 5, 11, 5, 13, 9, 11, 11, 13, 10, 9, 11, 10, 8, 9, 144, 139, 104, 120, 123, 100, 137, 108, 108, 144, 145, 122, 148, 120, 104, 149, 116, 124, 114, 106, 150, 143, 133, 127, 135, 112, 115, 137, 103, 137, 108, 100, 150, 108, 120, 101, 129, 113, 133, 115, 101, 114, 115, 100, 119, 123, 150, 140, 116, 113], [14, 11, 6, 11, 12, 5, 6, 13, 13, 11, 9, 13, 11, 8, 5, 8, 9, 8, 9, 15, 15, 11, 10, 10, 13, 11, 9, 7, 13, 15, 5, 8, 12, 12, 7, 12, 14, 5, 9, 10, 15, 10, 5, 9, 14, 12, 6, 13, 9, 5, 142, 127, 128, 107, 131, 100, 104, 126, 136, 123, 104, 130, 110, 146, 119, 138, 137, 120, 109, 112, 104, 143, 134, 109, 101, 142, 146, 106, 122, 114, 134, 146, 134, 146, 149, 116, 148, 148, 145, 146, 104, 146, 143, 124, 129, 144, 128, 135, 123, 105], [8, 5, 11, 6, 11, 5, 9, 6, 7, 10, 15, 5, 9, 10, 14, 5, 8, 5, 5, 11, 13, 6, 9, 11, 11, 6, 9, 9, 15, 12, 13, 7, 7, 13, 14, 13, 7, 12, 6, 5, 9, 11, 11, 12, 13, 15, 15, 8, 8, 6, 113, 112, 139, 106, 111, 132, 107, 121, 124, 114, 102, 148, 115, 139, 114, 132, 146, 128, 110, 105, 106, 105, 144, 113, 140, 142, 104, 101, 126, 108, 135, 125, 143, 143, 133, 117, 110, 104, 117, 144, 147, 135, 124, 127, 113, 132, 125, 116, 115, 104], [15, 7, 13, 9, 11, 13, 15, 8, 11, 14, 9, 5, 5, 9, 15, 5, 15, 13, 10, 13, 8, 14, 14, 6, 14, 8, 15, 13, 12, 7, 12, 15, 13, 14, 6, 8, 6, 7, 9, 6, 9, 5, 10, 12, 13, 13, 11, 5, 11, 15, 101, 102, 139, 104, 116, 150, 101, 149, 135, 131, 107, 133, 121, 101, 102, 108, 119, 110, 115, 139, 117, 142, 104, 121, 115, 144, 116, 129, 136, 109, 119, 102, 136, 112, 119, 124, 150, 144, 116, 146, 131, 111, 140, 140, 127, 108, 126, 129, 134, 133]]
copies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


import multipacking
multipacking.solve(I, B, R, required, available, copies)

# optimal objective value is: 0.0
