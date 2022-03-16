"""
Note to self: {detection algorithm}
x, y and z: Real-world 3D coordinates in meters with the origin at the center between hips.

Note so self(2): {2d point cloud}
the x,y origin (0,0) is in the middle of the chest. 

approx of difference between the origin in x--> ~0
approx of difference between the origin in y --> ~0.362

"""

# API's
import cv2
import mediapipe as mp
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import matplotlib.pyplot as plt
import csv

# helper class
import convertObjectToImage


def print_connections():
    mp_pose = mp.solutions.pose
    for lndmrk in mp_pose.PoseLandmark:
        print(lndmrk, lndmrk.value)
    print(mp_pose.POSE_CONNECTIONS)
    print([list(x) for x in mp_pose.POSE_CONNECTIONS])


def process_image(img):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)
    image = cv2.imread(img)
    with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return results


"algorithm for fixing y values:"
"y= detection(body_part)*(-1)"
"fixed_y=y+(-0.352)"
"return fixed_y"


def modify_points(results, stl_file, plot_Mesh, plot_2d, plot_3d):
    if (plot_Mesh == True):
        plot_mesh(stl_file)
    mp_pose = mp.solutions.pose
    # lists to csv file
    x_mod_list = []
    y_mod_list = []
    z_mod_list = []

    for body_part in mp_pose.PoseLandmark:
        print(body_part, '\n', results.pose_world_landmarks.landmark[body_part])
        print('this is the modified point: ', (-1) * results.pose_world_landmarks.landmark[body_part].x,
              (-1) * results.pose_world_landmarks.landmark[body_part].y - 0.362,
              results.pose_world_landmarks.landmark[body_part].z, '\n')
        x_modified = (-1) * results.pose_world_landmarks.landmark[body_part].x
        y_modified = (-1) * results.pose_world_landmarks.landmark[body_part].y - 0.352 + 0.1
        z_modified = results.pose_world_landmarks.landmark[body_part].z
        # append to lists
        x_mod_list.append(x_modified)
        y_mod_list.append(y_modified)
        z_mod_list.append(0)

        "plot in 2D --> use (X,Z) points {all points on sane plane y=0}"
        if (plot_2d == True):
            plt.plot(x_modified, 0, y_modified, marker="X", markersize=10, markeredgecolor="red", markerfacecolor="red")

        "plot in 3D --> use estimations for depth"
        if (plot_3d == True):
            plt.plot(x_modified, (-1) * (z_modified), y_modified, marker="x", markersize=10,
                     markeredgecolor="green", markerfacecolor="green")

    # export modified points to xyz file
    # data=[x_mod_list,y_mod_list,z_mod_list]
    create_xyz_file(x_mod_list, y_mod_list, z_mod_list)

    # show outputs --> 1. image with detected body parts 2. 3d plot of the object and subplot of body parts
    plt.show()
    cv2.waitKey(0)


######### HELPERS ###########

def create_xyz_file(x_mod_list, y_mod_list, z_mod_list):
    data = zip(x_mod_list, y_mod_list, z_mod_list)
    with open("Assests/modified_points.xyz", "a") as f:
        coords = [map(str, tupl) for tupl in data]
        writer = csv.writer(f, delimiter=' ')
        for line in coords:
            writer.writerow(line)


def plot_mesh(stl_file):
    # we want to plot the points we found as landmarks on the 3d object
    # plot the mesh in 3D
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    your_mesh = mesh.Mesh.from_file('Assests/stl_file.stl')
    your_mesh_cpy = mesh.Mesh.from_file('Assests/stl_file.stl')
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))


##### MAIN FUNCTION #####

def Skeleton_main():
    # upload the object as stl file
    stl_file = 'Assests/stl_file.stl'
    img = 'projectedImageOutput/projected_model.png'
    print(convertObjectToImage.main_function(stl_file))
    results = process_image(img)
    modify_points(results, stl_file, plot_Mesh=True, plot_2d=True, plot_3d=False)


######### CALL THE MAIN FUNCTION #########
Skeleton_main()
