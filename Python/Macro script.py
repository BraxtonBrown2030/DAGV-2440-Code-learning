import maya.cmds as cmds

# base snowball
cmds.polySphere(radius=3, sx=20, sy=20, ax=[0, 1, 0], createUVs=2, ch=1)
cmds.move([0, 3, 0])

# middle snowball
cmds.polySphere(radius=2, sx=20, sy=20, ax=[0, 1, 0], createUVs=2, ch=1)
cmds.move([0, 7.4, 0])

# top snow sphere
cmds.polySphere(radius=1.3, sx=20, sy=20, ax=[0, 1, 0], createUVs=2, ch=1)
cmds.move([0, 10, 0])

# tophat core
cmds.polyCylinder(ch=True, o=True, radius=0.985857, h=2.413298, sc=1)
cmds.move([0, 12.5, 0])

# top hat bottom
cmds.polyCylinder(ch=True, o=True, radius=1.733, h=0.271772, sc=1)
cmds.move([0, 11.5, 0])

# nose
cmds.polyCone(ch=True, o=True, r=0.903975, h=2.4072)
cmds.move([0,10,2])

# left eye
cmds.polySphere(radius=.5, subdivisionsX=4, subdivisionsY=4, ax=[0, 1, 0], ch=1)
cmds.move([1,10,.5])
cmds.rotate(relative = True, worldspace = True,forceorderXYZ=[0,45.5,0])
cmds.rotate(relative = True, worldspace = True,forceorderXYZ=[90,0,0])
cmds.rotate(relative = True, worldspace = True,forceorderXYZ=[0,64.675845,0])
cmds.move([0, 0.2284, 0 ])
cmds.move([-0.109809, 0, 0])
cmds.move([0, 0.10354, 0])
cmds.move([-0.072252, 0, 0])

# right eye
cmds.polySphere(radius=.5, subdivisionsX = 4,subdivisionsY = 4, ax =[0,1,0], ch=1)
cmds.move([-1,10,.5])
cmds.rotate(relative = True, worldspace= True,forceorderXYZ=[0,45.7,0])
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[90,0,0])
cmds.rotate(relative=True,worldspace=True,foceorderXYZ=[0,-58.7,0])
cmds.move(0,0.326359,0 , relative=True)
cmds.move(0,-0.165871,0, relative=True, wd=True,os=True)

# left arm
cmds.polyCylinder(ch=True,o=True,r=0.340915, h=3.374187,subdivisionsCaps = 1)
cmds.move(-3.439, 7.755, -0.056)
cmds.rotate(relative=True, worldspace=True,forceorderXYZ=[0,0,-100.464601])

# right arm
cmds.polyCylinder(ch=True,o=True,r=0.340915, h=3.374187,subdivisionsCaps = 1)
cmds.move(3.439, 7.755, 0.056)
cmds.rotate(relative=True, worldspace=True,forceorderXYZ=[0,0,100.464601])

# button one
cmds.polySphere(radius=0.5, subdivisionsX = 4,subdivisionsY = 4,axis = [0, 1, 0] , ch=1)
cmds.move([0,3.2,2.8])
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[90, 0, 0])

# button two
cmds.polySphere(radius=0.5, subdivisionsX = 4,subdivisionsY = 4,axis = [0, 1, 0] , ch=1)
cmds.move([0, 4.332, 2.535])
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[69.747, 0, 0])

# button three
cmds.polySphere(radius=0.5, subdivisionsX = 4,subdivisionsY = 4,axis = [0, 1, 0] , ch=1)
cmds.move(0, 5.217, 1.748)
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[51.950, 0, 0])

# button four
cmds.polySphere(radius=0.5, subdivisionsX = 4,subdivisionsY = 4,axis = [0, 1, 0] , ch=1)
cmds.move(0, 6.820, 1.710)
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[102.415, 0, 0])

# button five
cmds.polySphere(radius=0.5, subdivisionsX = 4,subdivisionsY = 4,axis = [0, 1, 0] , ch=1)
cmds.move(0, 7.746, 1.710)
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[77.765, 0, 0])

#button six
cmds.polySphere(radius=0.5, subdivisionsX = 4,subdivisionsY = 4,axis = [0, 1, 0] , ch=1)
cmds.move(0, 8.624, 1.410)
cmds.rotate(relative=True,worldspace=True,forceorderXYZ=[61.915, 0, 0])
