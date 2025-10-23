#!/usr/bin/env python3 
numbers=[101,2,15,22,95,33,2,27,72,15,52]
sort_num=sorted(numbers)
even=0
odd=0
for num in sort_num:
	if num%2==0:
	 even += num
	else:
	 odd += num
print(even)
print(odd)
