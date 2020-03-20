# Going to have to use vpython
import numpy as np
from vpython import *


AU = 149.6
time = 24*60**2
#
theta_mercury = 0.07073160621761658
theta_venus = 0.027948243992606283
theta_earth = 0.016748663101604278
theta_mars = 0.009136638876700307


# radii in Astronomical units
radius_sun = 0
radius_mer_maj = 0.387
radius_mercury_min = 0.3787808836
radius_venus_maj = 0.723
radius_venus_min = 0.7229822863
radius_earth_maj = 1
radius_earth_min = 0.998554896
radius_mars_maj = 1.523
radius_mars_min = 1.516650426

patch_sun = sphere(pos=vector(0, 0, 0), radius=0.1, make_trail=False, color=color.yellow)
patch_mer = sphere(pos=vector(69.8 / AU, 0, 0), radius=0.1, make_trail=True, retain = 10, color=color.red)
patch_v = sphere(pos=vector(108.9 / AU, 0, 0), radius=0.1, make_trail=True, retain = 10, color=color.blue)
patch_e = sphere(pos=vector(152.1 / AU, 0, 0), radius=0.1, make_trail=True, retain = 10, color=color.green)
patch_mar = sphere(pos=vector(249.2 / AU, 0, 0), radius=0.1, make_trail=True, retain = 10, color=color.red)

scene.camera.rotate(angle=45)
i = 0
di = 1
while (i <= 1000):
    rate(60)
    patch_mer.pos.x = ((np.sqrt(0.387**2 - 0.37878**2)) + 0.387 * np.cos(theta_mercury * i)) * np.cos(3 * (np.pi)/2 + (1.5/100) * i/365.25) - 0.37878 * np.sin(theta_mercury * i) * np.sin(3 * (np.pi)/2 + (1.5/100) * i/365.25)
    patch_mer.pos.y = ((np.sqrt(0.387**2 - 0.37878**2)) + 0.387 * np.cos(theta_mercury * i)) * np.sin(3 * (np.pi)/2 + (1.5/100) * i/365.25) + 0.37878 * np.sin(theta_mercury * i) * np.cos(3 * (np.pi)/2 + (1.5/100) * i/365.25)
    patch_mer.pos.z = 0

    patch_v.pos.x = (1.4/149.6) + radius_venus_maj * cos(theta_venus * i)
    patch_v.pos.y = radius_venus_min * sin(theta_venus * i)
    patch_v.pos.z = 0

    patch_e.pos.x = (5/149.6) + radius_earth_maj * np.cos(theta_earth * i)
    patch_e.pos.y = radius_earth_min * np.sin(theta_earth * i)
    patch_e.pos.z = 0

    patch_mar.pos.x = (42.6/149.6) + radius_mars_maj * np.cos(theta_mars * i)
    patch_mar.pos.y = radius_mars_min * np.sin(theta_mars * i)
    patch_mar.pos.z = 0

    i = i + di
print("Fin")
