import bpy

def testtest():
    for obj in bpy.context.selected_objects:
        obj.show_wire = True