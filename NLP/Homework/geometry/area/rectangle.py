def area_rectangle():
    try:
        l = int(input('Please enter the length of the rectangle:'))
        area = l*l
        print('The area of this rectangle is: {:.10f}'.format(area))
    except ValueError:
        print('Bad value: need some value else')