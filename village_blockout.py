
import maya.cmds as cmds
import math

# Parameters for easier adjustments
wall_width = 11.5
wall_height = 1
wall_depth = 1
well_radius = 1
well_height = 1
gate_wall_width = 6

def create_wall(name, x, z, y_rotation):
    wall = cmds.polyCube(w=wall_width, h=wall_height, d=wall_depth, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1, name=name)[0]
    cmds.xform(wall, piv=(0, wall_height/2, 0), ws=True)
    cmds.move(x, wall_height/2, z, wall)
    cmds.rotate(0, y_rotation, 0, wall)
    return wall

def create_gate_wall(name, x, z, y_rotation):
    wall = cmds.polyCube(w=gate_wall_width, h=wall_height, d=wall_depth, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1, name=name)[0]
    cmds.xform(wall, piv=(0, wall_height/2, 0), ws=True)
    cmds.move(x, wall_height/2, z, wall)
    cmds.rotate(0, y_rotation, 0, wall)
    return wall

def create_well(radius, height):
    well_obj = cmds.polyCylinder(r=radius, h=height, sx=32, sy=1, sz=1, ax=(0, 1, 0), rcp=0, cuv=3, ch=1)[0]
    cmds.move(0, height/2, 0, well_obj)
    return well_obj

# Create well at the center
well = create_well(well_radius, well_height)

# Create walls
se_gate_wall = create_gate_wall("south_wall", 6.5, 10, 0)
sw_gate_wall = create_gate_wall("sw_gate_wall", -6.5, 10, 0)
north_wall = create_wall("north_wall", 0, -11.5, 0)
north_west_wall = create_wall("north_west_wall", -11.5, -5, 60)
south_west_wall = create_wall("south_west_wall", -11.5, 5, -60)
north_east_wall = create_wall("north_east_wall", 11.5, -5, -60)
south_east_wall = create_wall("south_east_wall", 11.5, 5, 60)

# Deselect all objects
cmds.select(clear=True)
