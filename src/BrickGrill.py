

"""script.py

Primo script per FreeCAD

"""


"""filename.py

Here a short but significant description of what the script do

"""

import FreeCAD
from FreeCAD import Base, Vector
import Part
from math import pi, sin, cos

DOC = FreeCAD.activeDocument()
DOC_NAME = "Pippo"

def clear_doc():
	"""
	 Clear the active document deleting all the objects
	"""
	for obj in DOC.Objects:
		DOC.removeObject(obj.Name)

def setview():
	"""Rearrange View"""
	FreeCAD.Gui.SendMsgToActiveView("ViewFit")
	FreeCAD.Gui.activeDocument().activeView().viewAxometric()

if DOC is None:
	FreeCAD.newDocument(DOC_NAME)
	FreeCAD.setActiveDocument(DOC_NAME)
	DOC = FreeCAD.activeDocument()
else:
	clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5


def cubo(nome, lung, larg, alt):
	obj_b = DOC.addObject("Part::Box", nome)
	obj_b.Length = lung
	obj_b.Width = larg
	obj_b.Height = alt

	DOC.recompute()

	return obj_b

# objects definition

std_brick_l = 190.5 # length of the standard brick
std_brick_w = 95.25  # width of the standard brick
std_brick_h = 57.15  # height of the standard brick

half_brick_l = std_brick_l*0.5 # length of the standard brick


concr_width = 4  # The thickness of the concrete
n_width = 6
n_back_wall = 14


#obj = cubo("test_cube", std_brick_h, std_brick_w, std_brick_l)


for i_h in range(0, 13):

#
#   Building the left wall
#

	oddRaw = False
	if i_h%2 == 1:
		oddRaw = True;

	#
	#   Building the left side wall
	#

	if oddRaw == True:
		for i in range(0, n_width ):
			std_brick_1 = cubo("brick_%d_1" %(i), std_brick_h, std_brick_w, std_brick_l)
			std_brick_1.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), 0, i*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))
			std_brick_2 = cubo("brick_%d_2" %(i), std_brick_h, std_brick_w, std_brick_l)
			std_brick_2.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_w , i*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))
		std_brick_edge = cubo("brick_%d_2" %(n_width), std_brick_h, std_brick_w, std_brick_l)
		std_brick_edge.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l, n_width*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))
	else:
		std_brick_edge = cubo("brick_%d_2" %(n_width), std_brick_h, std_brick_w, std_brick_l)
		std_brick_edge.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l, 0), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))

		for i in range(0, n_width ):
			std_brick_1 = cubo("brick_%d_1" %(i), std_brick_h, std_brick_w, std_brick_l)
			std_brick_1.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), 0, i*(std_brick_l+concr_width) + std_brick_w), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))

			if i < n_width - 1:
				std_brick_2 = cubo("brick_%d_2" %(i), std_brick_h, std_brick_w, std_brick_l)
				std_brick_2.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_w , i*(std_brick_l+concr_width) + std_brick_w), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))
			else:
				half_brick = cubo("brick_back_%d_%d" %(i_h, n_back_wall+1), std_brick_h, std_brick_w, half_brick_l)
				half_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_w , i*(std_brick_l+concr_width) + std_brick_w), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))

	#
	#   Building the Back wall
	#

	if oddRaw == False:
		for i_bw in range(0, n_back_wall+1):
			std_brick = cubo("brick_back_%d_%d" %(i_h, i_bw), std_brick_h, std_brick_w, std_brick_l)
			std_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), 0.5*std_brick_l + (i_bw+1)*(std_brick_l+concr_width), n_width*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))
		#half_brick = cubo("brick_back_%d_%d" %(i_h, n_back_wall+1), std_brick_h, std_brick_w, half_brick_l)
#		half_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l + (n_back_wall)*(std_brick_l+concr_width) + half_brick_l, n_width*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))
	else:
#		half_brick = cubo("brick_back_%d_%d" %(i_h, 0), std_brick_h, std_brick_w, half_brick_l)
#		half_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l + half_brick_l+concr_width, n_width*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))
		for i_bw in range(0, n_back_wall + 1):
			std_brick = cubo("brick_back_%d_%d" %(i_h, i_bw+1), std_brick_h, std_brick_w, std_brick_l)
			std_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l + (i_bw+1)*(std_brick_l+concr_width), n_width*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))


	#
	#   Building the right side wall
	#

	if oddRaw == False:
		for i in range(0, n_width ):
			std_brick_1 = cubo("brick_Right_%d_1" %(i), std_brick_h, std_brick_w, std_brick_l)
			std_brick_1.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l, i*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))
			std_brick_2 = cubo("brick_Right_%d_2" %(i), std_brick_h, std_brick_w, std_brick_l)
			std_brick_2.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_w + (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l , i*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))

		std_brick = cubo("brick_back_%d_%d" %(i_h, n_back_wall+1), std_brick_h, std_brick_w, std_brick_l)
		std_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l + (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l, n_width*(std_brick_l+concr_width)), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))
	else:
		std_brick_edge = cubo("brick_Right_%d_2" %(n_width), std_brick_h, std_brick_w, std_brick_l)
		std_brick_edge.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_l + (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l, 0), FreeCAD.Rotation(0, 0, 90), Vector(0, 0, 0))

		for i in range(0, n_width ):
			std_brick_2 = cubo("brick_Right_%d_2" %(i), std_brick_h, std_brick_w, std_brick_l)
			std_brick_2.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), std_brick_w + (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l, i*(std_brick_l+concr_width) + std_brick_w), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))

			if i < n_width - 1:
				std_brick_1 = cubo("brick_Right_%d_1" %(i), std_brick_h, std_brick_w, std_brick_l)
				std_brick_1.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l, i*(std_brick_l+concr_width) + std_brick_w), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))
			else:
				half_brick = cubo("brick_Right_%d_%d" %(i_h, n_back_wall+1), std_brick_h, std_brick_w, half_brick_l)
				half_brick.Placement = FreeCAD.Placement(Vector(i_h*(std_brick_h + concr_width), (n_back_wall+1)*(std_brick_l+concr_width) + half_brick_l, i*(std_brick_l+concr_width) + std_brick_w), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))



setview()
