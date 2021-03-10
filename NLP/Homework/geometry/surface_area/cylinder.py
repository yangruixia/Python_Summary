def surface_area_cylinder():
    try:
        r = int(input('Please enter the radius of the bottom edge of the cylinder: '))
        h = int(input('Please enter the height of the cylinder: '))
        import math
        surface_area = math.pi*r*(r+h)*2
        print('The surface area of the cylinder is: {:.10f}'.format(surface_area))
    except ValueError:
        print('Bad value: need some value else')