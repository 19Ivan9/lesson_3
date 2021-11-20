print('tack1')

if __name__ == '__main__':
    name = 'ivan'
    day = ' SATURDAY    '
    name = name.capitalize()
    day = day.strip()
    day = day.lower()
    day = day.capitalize()
    rez = 'Good day {}! {} is a perfect day to learn some python'.format(name, day)
    print(rez)

    print('tack2')

    first_name = 'Ivan'
    last_name = 'Prokopenko'
    rez = 'Hallo' + ' ' + first_name + ' ' + last_name + '!'
    print(rez)

    print('tack3')
    a, b = 3, 6
    print('a+b=' + str(a + b) + '\n' + 'a-b=' + str(a - b) + '\n'
          + 'a/b=' + str(a / b) + '\n' + 'a*b=' + str(a * b) + '\n'+
          'a**b ' + str(a ** b) + '\n' + 'a//b=' + str(a // b) + '\n' + 'a%b=' + str(a % b))
