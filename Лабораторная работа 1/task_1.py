numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers1 = numbers[:4] + numbers[5:]
sum_numbers = sum(numbers1)
len_numbers = len(numbers)
average = sum_numbers/len_numbers
numbers[4] = average
print ("Измененный список:", numbers)