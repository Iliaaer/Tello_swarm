from fly_tello import FlyTello
my_tellos = list()


##my_tellos.append('0TQZHBRED0113W') # tello=1       Главный
my_tellos.append('0TQZHARED00ZWY') # tello=2       Запасной


with FlyTello(my_tellos) as fly:
    fly.takeoff()

    fly.forward(dist=100)

    fly.right(dist=50)
    fly.left(dist=50)

    fly.back(dist=50)

    # with fly.sync_these():
    #     fly.flip(direction='right', tello=1)
    #     fly.flip(direction='left', tello=2)

    # fly.flip(direction='right')
    # fly.flip(direction='left')
    '''with fly.sync_these():
        fly.flip(direction='left', tello=1)
        fly.flip(direction='right', tello=2)
    
    with fly.sync_these():
        fly.left(dist=50, tello=1)
        fly.right(dist=50, tello=2)
    
    fly.flip(direction='back')
    fly.flip(direction='back')

    fly.forward(dist=150)'''

    # fly.flip(direction='forward')
    # fly.flip(direction='right')
    # fly.flip(direction='back')
    # fly.flip(direction='back')
    # fly.flip(direction='left')
##    with fly.sync_these():
##        fly.curve(x1=60, y1=50, z1=15, x2=150, y2=-10, z2=50, speed=60, tello=1)
##        fly.curve(x1=60, y1=-20, z1=15, x2=150, y2=-50, z2=50, speed=60, tello=2)
##    with fly.sync_these():
##        fly.curve(x1=-60, y1=-50, z1=-15, x2=-150, y2=0, z2=0, speed=60, tello=1)
##        fly.curve(x1=-60, y1=20, z1=-15, x2=-150, y2=0, z2=0, speed=60, tello=2)
##    fly.rotate_cw(angle=270)
    

    # fly.back(dist=100)

    # fly.reorient(height=100, pad='m-2')
    # fly.left(dist=50)
    # fly.flip(direction='right')
    # fly.reorient(height=100, pad='m-2')
    # fly.curve(x1=50, y1=30, z1=0, x2=100, y2=30, z2=-20, speed=60)
    # fly.curve(x1=-50, y1=-30, z1=0, x2=-100, y2=-30, z2=20, speed=60)
    # fly.reorient(height=100, pad='m-2')
    # fly.rotate_cw(angle=360, tello=1)
    # fly.straight_from_pad(x=30, y=0, z=75, speed=100, pad='m-2')
    # fly.flip(direction='back')
    # fly.reorient(height=50, pad='m-2')
    fly.land()
