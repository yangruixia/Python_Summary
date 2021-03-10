def surface_area_sphere():
    try:
        r = int(input('Please enter the radius the sphere: '))
        import math
        surface_area = math.pi*r*r*4
        print('The surface area of this sphere is: {:.10f}'.format(surface_area))
    except ValueError:
        print('Bad value: need some value else')