#A python program to print all +ve number in a range .

# List of  Numbers 
list1 = [12,-7,5,64, -14]
list2 = [12,14,-95,3]
num = 0
a=0
# using while loop for list 1    
while(num < len(list1)):
    # checking condition
     if list1[num] >= 0:
         print(list1[num], end = " ")
     num += 1
# using while loop for list 2    
while(a < len(list2)):
    # checking condition
     if list2[a] >= 0:
         print(list2[a], end = " ")
     a += 1      
        
