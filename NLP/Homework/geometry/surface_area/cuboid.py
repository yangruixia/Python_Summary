def surface_area_cuboid():
    try:
        l = int(input('Please enter the height of the cuboid: '))
        m = int(input('Please enter the length of the bottom edge of the cuboid: '))
        n = int(input('Please enter the width of the bottom edge of the cuboid: '))
        surface_area = 2*m*n + 2*(m+n)*l
        print('The surface area of this cuboid is: {:.10f}'.format(surface_area))
    except ValueError:
        print('Bad value: need some value else')