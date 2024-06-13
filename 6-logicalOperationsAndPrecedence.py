#Task 1
number_a = 6
number_b = 8
number_c = 3

regular_total = number_a + number_b / number_c
parenthesis_total = (number_a + number_b) / number_c
print(regular_total, parenthesis_total)

#Task 2
if(((number_a * number_c) + (number_b / number_a)) > 20):
    print('Final number is greater than 20!')
elif(((number_a * number_c) + (number_b / number_a)) < 20):
    print('Final number is less than 20!')
else:
    print('Final number is 20!')