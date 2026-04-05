# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:35:16 2026

@author: 2-106-03
"""

import sys

try:
    result = 1
    for i in range(1, len(sys.argv)):
        result *= float(sys.argv[i])
except ValueError:
    result = ''
    for i in range(1, len(sys.argv)):
        result += sys.argv[i]
        
print('Результат обработки:', result)