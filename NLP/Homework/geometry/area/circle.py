def area_circle():
    try:
        r = int(input('Please enter the radius of the circle:'))
        import math
        area = math.pi*r*r
        print('The area of this circle is: {:.10f}'.format(area))
    except ValueError:
        print('Bad value: need some value else')