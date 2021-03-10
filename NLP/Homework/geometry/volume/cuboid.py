def volume_cuboid():
    try:
        l = int(input('Please enter the height of the cuboid: '))
        m = int(input('Please enter the length of the bottom edge of the cuboid: '))
        n = int(input('Please enter the width of the bottom edge of the cuboid: '))
        volume = m*n*l
        print('The volume of this cuboid is: {:.10f}'.format(volume))
    except ValueError:
        print('Bad value: need some value else')