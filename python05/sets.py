#!/usr/bin/env

var1 = {'3','14','15','9','26','5','35','9'}
print(var1)

var2 = {'60','22','14','0','9'}
print(var2) 

diff= var1-var2
print(f"difference is :{diff}")

un = var1|var2
print(f"union is: {un}")

int=var1&var2
print(f"intersection is:{int}")

sym=var1^var2
print(f"symmetrical is:{sym}")
