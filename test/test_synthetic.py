import matplotlib.pyplot as plt
import synthetic.imc as imc
import astropy.units as u
import synthetic.vu as vu
import numpy as np
import math

#TODO This is not working for near zero positions!!! (it is fault of the wcs i think!)
univ=vu.Universe()
univ.create_source('example',1.0*u.deg,1.0*u.deg)
univ.create_source('example2',1.01*u.deg,0.99*u.deg)
model=imc.IMC('Gaussian',np.array([10,7])*u.arcsec,math.pi/9.*u.rad,'33SO2',300*u.K,30*u.km/u.s,np.array([0.0,0.0])*u.km/(u.s*u.arcsec))
model2=imc.IMC('Gaussian',np.array([3,10])*u.arcsec,math.pi/3.*u.rad,'33SO2',280*u.K,20*u.km/u.s,np.array([0.0,0.0])*u.km/(u.s*u.arcsec))
model.set_velocity(150*u.km/u.s)
model2.set_velocity(100*u.km/u.s)
univ.add_component('example',model)
univ.add_component('example2',model2)
(cube,tab)=univ.gen_cube(np.array([1.0,1.0])*u.deg,np.array([1.0,1.0])*u.arcsec, np.array([200,200])*u.arcsec,300*u.GHz, 0.005*u.GHz, 2*u.GHz, 0.5)
#univ.save_cube(cube,'p33SO2-obs1.fits')
print tab
plt.plot(cube.get_stacked(axis=(1,2)))
plt.show()
plt.clf
plt.imshow(cube.get_stacked())
plt.show()
#cube.animate(10,True)

