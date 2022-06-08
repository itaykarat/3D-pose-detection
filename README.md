# 3D-pose-detection
Auto skeleton detection of 3D model of  person



INPUT: Given a 3d model of a human body. {.obj file}

OUUTPUT: return an image wich will represent the projection of that model on a plane.




Gemeral info;
3D model will be a point cloud {each point in 3D}


Algo:
The solution in the code is simple.
1. Read all 3d points from the model.
2. Project each point to the plane --> simple projection [point from model from type = (x,y,z)  ===> projection will just remove z values, beacuse model is alligned]
3. After we have a cloud of 2d points we can plot them in 2D AKA Image.


Attached :
1. Screenshot of the 3D model given
2. projected model as an image.
