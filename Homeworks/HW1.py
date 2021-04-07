# First way to do the first question, create a list
list = ["I", "want", "to", "be", "a", "Top Learner"]
# then, swap the second half with the first half
list[0], list[1], list[2], list[3], list[4], list[5] = list[3], list[4], list[5], list[0], list[1], list[2]
print(list)

# Second way to do the first question might be,
list_2= ["I", "want", "to", "be", "a", "Top Learner"]
list_2a = list_2[:3] # First half
list_2b = list_2[3:] # Second half
list_2a, list_2b = list_2b, list_2a  # swapping
list_final = list_2a + list_2b
print(list_final)


# Second question
n= int(input("Please enter a single digit integer: "))
if n < 0:
    print("Please enter a positive number.")
elif n >= 10:
    print("Please enter a single digit number.")
else:
  for i in range(0, n+1):
    while (i%2)==0:
        print(i)
        i += 1
        continue
