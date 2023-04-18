import bpy

# Create a new cube mesh
mesh = bpy.data.meshes.new("BoxMesh")
cube_object = bpy.data.objects.new("BoxObject", mesh)

# Add the object to the scene
bpy.context.scene.collection.objects.link(cube_object)

# Define the vertices and faces of the mesh
verts = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]
faces = [(0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5)]

# Add the vertices and faces to the mesh
mesh.from_pydata(verts, [], faces)
mesh.update()
