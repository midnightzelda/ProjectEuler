#Dylan Blake


#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

total = []
num = 0
answer = 0


#adds number to eligibal list if under 1000
while num < 1000 :  
    # Increment the value of the variable "num by 3"
    total.append(num)
    num = num+3

num = 0    

while num < 1000 :  
    # Increment the value of the variable "num by 5"
    total.append(num)
    num = num+5
    

total = list(set(total))

#calculates the sum of all the numbers
for x in range(0, len(total)):    
   answer = answer + total[x];    
  

print(answer)    



