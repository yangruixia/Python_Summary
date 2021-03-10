def area_square():
    try:
        m = int(input('Please enter the length of the square:'))
        n = int(input('Please enter the width of the square:'))
        area = m*n
        print('The area of this square is: {:.10f}'.format(area))
    except ValueError:
        print('Bad value: need some value else')