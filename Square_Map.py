def square_num(number):
  return number * number
number = [4, 5, 2, 9]
print("The given List ",number)
result = map(square_num, number)
print("The square of given numbers: ")
print(list(result))
