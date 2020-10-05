numbers = [5, 2, 6, 2, 11 ,532, 4444, 6667]
numbers.pop()
print(numbers)

numbers.append(6667)
print(numbers)

numbers.insert(0, 4444)
print(numbers)

print(532 in numbers) #???

print(numbers.count(2))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numberssequel = numbers.copy()
numbers.pop()

print(numbers)
print(numberssequel)

indiv = []
for number in numbers:
    if number not in indiv:
        indiv.append(number)
print(indiv)
        
        

numbers.clear()
print(numbers)

numbers.insert(2, 5555)
print(numbers)

print(numbers[0])