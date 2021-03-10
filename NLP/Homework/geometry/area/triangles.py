def area_triangles():
    try:
        d = int(input('Please enter the bottom edge length of the triangle:'))
        h = int(input('Please enter the height od the trangle:'))
        area = d*h/2
        print('The area of this trangle is: {:.10f}'.format(area))
    except ValueError:
        print('Bad value: need some value else')