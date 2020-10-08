digits = input('Digits to text: ')
digits_var = {
    '1': 'One',
    '2': "Two",
    '3': 'Three',
    '4': 'notFour'
}
output = ''
for ch in digits:
    output += digits_var.get(ch, "!") + ' '
print(output)