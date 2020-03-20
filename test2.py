from vpython import*

sun =  sphere( pos=vector(0,0,0), radius=0.25, color=vector(1,0,0), make_trail=True, retain = 100, trail_color = vector(1,1,1), opacity = 1.0 )
my_sphere = sphere( pos=vector(1,0,0), radius=0.25, color=vector(1,0,0), make_trail=True, retain = 100, trail_color = vector(1,1,1), opacity = 1.0 )
my_sphere2 = sphere( pos=vector(-1,0,0), radius=0.25, color=vector(1,0,0), make_trail=True, retain = 100, trail_color = vector(1,1,1), opacity = 1.0 )

# color = vector() uses RGB code.
#my_sphere.visible = False
time = 0 # Time in simulation.
dt = 0.01 # Time step size.
# Make a loop.
while (time <= 1000):
    rate(100) # Number of frames/loops per second.
    # my_sphere.pos.x = my_sphere.pos.x + dx # Dot indicates an attribute.
    my_sphere.pos.x = cos(time)
    my_sphere.pos.y = sin(time)
    my_sphere2.pos.x = -cos(time)
    my_sphere2.pos.y = -sin(time)
    time = time + dt

print("End of program.")
