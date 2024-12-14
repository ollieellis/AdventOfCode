from typing import List
from itertools import pairwise
from copy import copy

def get_nums(line: str):
    nums = line[:-1].split(" ")
    return [int(i) for i in nums]

def is_safe(nums: List[int]):
    deltas = [b - a for a, b in pairwise(nums)]
    return all(1<= d <= 3 for d in deltas) or all(1 <= -d <= 3 for d in deltas)

def line_safe(line: str):
    nums = get_nums(line)
    return is_safe(nums)

def is_safe_dampened(line: str):
    nums = get_nums(line)
    if is_safe(nums):
        return True
    
    for i in range(len(nums)):
        nums_copy = copy(nums)
        nums_copy.pop(i)
        if is_safe(nums_copy):
            return True
    
    return False



with open('reports.txt', 'r') as file:
    lines = file.readlines()

count = sum([line_safe(l) for l in lines])
print(count)

count2 = sum([is_safe_dampened(l) for l in lines])
print(count2)