import numpy
from stl import mesh
import matplotlib.pyplot as plt


def main_function(stl_file):
    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(stl_file)

    # Set Y values in each point to 0
    for vector in your_mesh.vectors:
        for point in vector:
            point[1] = 0

    # Save x and y values in lists --> then we cast it to numpy array for plotting the image out
    projected_obj_pointsX = []  # only x values of each point
    projected_obj_pointsY = []  # only y values of each point
    projected_obj_points = []  # (x,y)

    # Pack each point coordinates in a list
    for vector in your_mesh.vectors:
        for point in vector:
            point_2d = []
            point_2d.append(point[0])
            point_2d.append(point[2])
            projected_obj_points.append(point_2d)
            projected_obj_pointsY.append(point[2])
            projected_obj_pointsX.append(point[0])

    # cast to numpy array
    numpyList = numpy.array(projected_obj_points)
    xNPlist = numpy.array(projected_obj_pointsX)
    yNPlist = numpy.array(projected_obj_pointsY)

    # Set the data of the 2d points --> and plot as a histogram
    data = [xNPlist, yNPlist]
    plt.hist2d(data[0], data[1], bins=300, cmin=1)  # Note- if we want more specification of points increase bins
    plt.axis('off')
    plt.savefig('projectedImageOutput/projected_model')
