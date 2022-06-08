# 3D-pose-detection
Problem: I couldn't find any good API for finding Body key points on a human body 3D model.

**Below- implementation of my solution to that problem.

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
3. Apply mediaPipe function to detect human parts.



<img width="517" alt="image (4)" src="https://user-images.githubusercontent.com/60778119/172611815-76c00fa5-fd01-46df-ad51-5e56f3dfc0b1.png">

<img width="482" alt="image (5)" src="https://user-images.githubusercontent.com/60778119/172611829-787ee05e-7315-4aef-82c4-68e0ca8816cf.png">

<img width="614" alt="image" src="https://user-images.githubusercontent.com/60778119/172612139-5ece4b74-ad7e-432a-a690-288fd7e4b39c.png">

<img width="509" alt="image" src="https://user-images.githubusercontent.com/60778119/172612233-5f532d05-3cc6-4b31-ba58-b4519e37ffe8.png">

<img width="515" alt="image" src="https://user-images.githubusercontent.com/60778119/172612292-2238a485-9eef-4f88-ad3f-98b08b9715e5.png">

Final result --> key points on the 3D model:
<img width="612" alt="image" src="https://user-images.githubusercontent.com/60778119/172612362-e672c41c-4fbd-448e-991f-9ad85257ac49.png">



