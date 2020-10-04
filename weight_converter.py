user_weight = float(input('Weight: '))
lbs_or_kg = input(f"Lbs or Kg: ")

if lbs_or_kg.lower() == 'l':
    user_pounds = user_weight * 0.45
    print(f"You weigh {user_pounds} kilograms.")
else:
    user_kilograms = user_weight * 2.205
    print(f'You weigh {user_kilograms} pounds.')

#this is where it all starts falling apart, in a sense. What if a character different from k or l is used? What if a special or numerical char is used? Seems to just skip to the 'else' section.