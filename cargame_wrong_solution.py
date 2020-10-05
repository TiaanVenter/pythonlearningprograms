car_state = False
u_input = input(f'>')

if car_state == True:
    print('Car is stopped!')

if u_input == 'start':
    car_state = True
    print('Car has started!')
elif u_input == 'stop':
    car_state == False
    print('Car has stopped!')
else:
    print('''I don''t understand that...''')