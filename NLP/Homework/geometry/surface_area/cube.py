def surface_area_cube():
    try:
        l = int(input('Please enter the side length of the cube: '))
        surface_area = 6*l*l
        print('The surface area of this cube is: {:.10f}'.format(surface_area))
    except ValueError:
        print('Bad value: need some value else')