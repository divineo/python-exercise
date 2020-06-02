#Python3 code

"""
Problem 1 :- Sum to N

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = 2, 7, 11, 15, target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return 0, 1.
"""

arr = [2, 7, 11, 15]
target = 9

def findpair(arr, target):

	#ignore last element in array
	for i in range(len(arr) - 1):

		#goes till last element
		for j in range(i + 1, len(arr)):

			#if target is found, print
			if arr[i] +arr[j] == target:
				print("Pair found at index", i, "and", j)
				return

	#if pair does not exist for the target
	print("Pair not found")

findpair(arr, target)
