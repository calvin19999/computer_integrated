import bpy

# Define the dimensions of the box
width = 2
height = 2
depth = 2

# Create a new mesh object
mesh = bpy.data.meshes.new("Box")

# Create a list of vertices for the box
verts = [(0, 0, 0), (0, height, 0), (width, height, 0), (width, 0, 0),
         (0, 0, depth), (0, height, depth), (width, height, depth), (width, 0, depth)]

# Create a list of faces for the box
faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]

# Add the vertices and faces to the mesh
mesh.from_pydata(verts, [], faces)

# Create a new object for the mesh
obj = bpy.data.objects.new("Box", mesh)

# Add the object to the scene
bpy.context.scene.collection.objects.link(obj)
