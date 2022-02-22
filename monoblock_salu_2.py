#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import paramak


# In[2]:


rotated_circle = paramak.ExtrudeCircleShape(
    points=[
         (0, 0),
       
        
    ],
    radius=.95,
    distance=1.2,
    workplane='XZ',
    stl_filename='part0.stl',
)

rotated_circle.show()


# In[ ]:





# In[3]:


grey_part = paramak.ExtrudeMixedShape(
    points=[
         (-1.15, -1.25, 'straight'),
         (1.15, -1.25, 'straight'),
         (1.15, 1.75, 'straight'),
         (-1.15, 1.75, 'straight'),
         
    ],
    distance=1.2,
    color=(0.5,0.5,0.5),
    cut=rotated_circle,
    material_tag='tungsten',
    stp_filename='part1.stp',
    stl_filename='part1.stl',
)

grey_part.show()


# In[ ]:





# In[4]:


rotated_straights = paramak.RotateMixedShape(
    points=[
         (.75, -.6, 'straight'),
         (.95, -.6, 'straight'),
         (.95, .6, 'straight'),
         (.75, .6, 'straight'),
         
    ],
    workplane='XY',
    rotation_angle=360,
    material_tag='Cu',
    stl_filename='part2.stl',
)

rotated_straights.show()


# In[ ]:





# In[5]:


rotated_straights1 = paramak.RotateMixedShape(
    points=[
         (.6, -.6, 'straight'),
         (.75, -.6, 'straight'),
         (.75, .6, 'straight'),
         (.6, .6, 'straight'),
         
    ],
    workplane='XY',
    rotation_angle=360,
    material_tag='cuzrcr',
    stl_filename='part3.stl',
)

rotated_straights1.show()


# In[6]:


myreactor=paramak.Reactor([grey_part,rotated_straights,rotated_straights1])
myreactor.show()


# In[7]:


import openmc
w=openmc.Material(name='w')
w.add_element('W',1)
w.set_density('g/cc',19.3)
w


# In[ ]:





# In[8]:



zirconium=openmc.Material(name='zirconium')
zirconium.add_element('zirconium',1)
zirconium.set_density('g/cc',6.6)
zirconium


# In[ ]:





# In[9]:



cr=openmc.Material(name='cr')
cr.add_element('Cr',1)
cr.set_density('g/cc',7.19)
cr


# In[ ]:





# In[10]:



cu=openmc.Material(name='cu')
cu.add_element('Cr',.012)
cu.add_element('Zr',.0007)
cu.set_density('g/cc',8.96)
cu


# In[ ]:





# In[11]:



copper=openmc.Material(name='copper')
copper.add_element('copper',1)
copper.set_density('g/cc',8.96)
copper


# In[21]:



ource = openmc.Source()

# sets the location of the source to x=0 y=0 z=0
source.space = openmc.stats.Point((0, 0, 50))

# sets the direction to isotropic
source.angle = openmc.stats.Isotropic()

# sets the energy distribution to 100% 14MeV neutrons
source.energy = openmc.stats.Discrete([14e6], [1])


# In[27]:


import paramak_neutronics
my_model = paramak_neutronics.NeutronicsModel(
    geometry=myreactor,
    source=source,
    simulation_batches=500,  # this should be increased to get a better mesh tally result
    simulation_particles_per_batch=100000,  # this should be increased to get a better mesh tally result
    materials = {'tungsten':w,'Cu':copper,'cuzrcr':cu},
    mesh_tally_3d=['(n,Xt)','heating','damage-energy'],
    mesh_tally_2d=['(n,Xt)','heating'],
    
    mesh_3d_resolution=(25,5,25),
    mesh_3d_corners=[(-1.15,-0.6,-1.25),(1.15,0.6,1.75)]
)

my_model.simulate()


# In[60]:


get_ipython().system('ls *.h5m')


# In[16]:





# In[ ]:




