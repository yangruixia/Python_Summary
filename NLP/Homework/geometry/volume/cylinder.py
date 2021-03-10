def volume_cylinder():
    try:
        r = int(input('Please enter the radius of the bottom edge of the cylinder: '))
        h = int(input('Please enter the height of the cylinder: '))
        import math
        volume = math.pi*r*r*h
        print('The volume of the cylinder is: {:.10f}'.format(volume))
    except ValueError:
        print('Bad value: need some value else')