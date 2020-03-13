# Program to display the Fibonacci sequence up to n-th term
# using while loop

n_terms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n_terms:
       print("***", n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print()

n_1, n_2 = 0, 1

if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
   
# using for loop
for num in range(0, n_terms):
    print("-->", n_1)
    n_th = n_1 + n_2
    n_1 = n_2
    n_2 = n_th
        

