"""1. Count numbers (*)
Use a for statement to count from:

  a)   -10 to 10 with one increment (*)

  b)   -10 to 10 with two increment (*"""

#a)
for x in range(-11,10):
    x += 1
    print(x)

#b)
for x in range(-11,10,2):
    x += 1 
    print(x)


 
""" Arithmetic sum (*)
Use a for statement to compute the following sums:"""
#a) 
total_sum = 0
for x in range(1,101):
    total_sum += x
print(total_sum)
  
#b) 
total_sum = 0
for x in range(1,100,2):
    total_sum += x
print(total_sum)    


"""Multiplication table (*)"""

"""Use for statement(s) to:

  a)   print out the 6th multiplication table from 0 to 10 (*)

  b)   let the user input the table, start and end of the table. (*)

  c)   print out a full multiplication table from 0 to 10. (**)"""

#a) 
for x in range(1,10):
    multiplication = x*6
    print(multiplication)

#b)

#table_user_= input("Which tabel are you interested in?") ## 4
#start_user = input("Specify the start of the table") ## 1
#table_end = input("Specify the end of the table") ## 9

for user_input in range(1,10):
    table_four = user_input * 4
    print(table_four)


for x in range(0,11):
    for y in range(0,11):
        print(f"{x * y:4}", end ="")


        # Faculty (*)
#Use a for statement to compute n!.
#n! = 1*2*3*...*(n-1) * n
     

#Let the user input 






