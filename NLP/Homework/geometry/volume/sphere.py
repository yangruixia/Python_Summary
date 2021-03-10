def volume_sphere():
    try:
        r = int(input('Please enter the radius the sphere: '))
        import math
        volume = 4*math.pi*r*r*r/3
        print('The volume of this sphere is: {:.10f}'.format(volume))
    except ValueError:
        print('Bad value: need some value else')