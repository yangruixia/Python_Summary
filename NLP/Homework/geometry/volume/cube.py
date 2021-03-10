def volume_cube():
    try:
        l = int(input('Please enter the side length of the cube: '))
        volume = l*l*l
        print('The volume of this cube is: {:.10f}'.format(volume))
    except ValueError:
        print('Bad value: need some value else')