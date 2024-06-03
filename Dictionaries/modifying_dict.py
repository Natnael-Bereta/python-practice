alien = {'color': 'green', 'y_position': '25', 'x_position': '0' , 'speed': 'medium'}
if alien['speed'] == 'slow':
    y_increment = 1
elif alien['speed'] == 'medium':
    y_increment = 2
else:
    y_increment = 3
alien['y_position'] = int(alien['y_position']) + y_increment
print(f'New speed: {alien['y_position']}')