'''
Test yourself!
For this exercise you will have to use not only what you have learned today,
but what you have learned about Python Data Structures and variable types too!

Okay, let’s see:

Take this list:
test_yourself = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
Calculate the mean of the list elements – by using only
those things that you have read in this and the previous articles!

Calculate the median of the list elements – by using only those things
that you have read in this and the previous articles!

https://data36.com/python-built-in-functions-methods-python-data-science-basics-3/
'''
# Ej1 - Mean
test_yourself = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(sum(test_yourself)/len(test_yourself))

# Ej2 - Median for odd len

num = len(test_yourself)
print(f"Len {num}")
if(num % 2) == 0:
    print("Even len")
    print(f"Element at ty[{round(len(test_yourself) / 2)}]")
    a = round(len(test_yourself) / 2)
    b = round(len(test_yourself) / 2) + 1
    print(f"Median is the mean of {a} and {b}")
    print((a + b) / 2)
else:
    print("Odd len")
    print(f"Element at ty[{round(len(test_yourself) / 2) - 1}]")
    print(test_yourself[round(len(test_yourself) / 2) - 1])
