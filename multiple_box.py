import bpy
import random

num_boxes = 10  # number of boxes to create
min_size = 0.5  # minimum size of each box
max_size = 1.5  # maximum size of each box

for i in range(num_boxes):
    # Define the size and location of each box
    size = random.uniform(min_size, max_size)
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(0, 5)

    # Create a new cube mesh
    mesh = bpy.data.meshes.new("BoxMesh")
    cube_object = bpy.data.objects.new("BoxObject", mesh)

    # Add the object to the scene
    bpy.context.scene.collection.objects.link(cube_object)

    # Define the vertices and faces of the mesh
    verts = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]
    faces = [(0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5)]

    # Scale the vertices based on the size of the box
    for j in range(len(verts)):
        verts[j] = tuple([verts[j][k] * size for k in range(3)])

    # Translate the vertices based on the location of the box
    for j in range(len(verts)):
        verts[j] = tuple([verts[j][k] + [x, y, z][k] for k in range(3)])

    # Add the vertices and faces to the mesh
    mesh.from_pydata(verts, [], faces)
    mesh.update()
