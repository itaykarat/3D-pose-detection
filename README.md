# 3D pose detection


### Motivation: 

Finding 3D coordinates of interest points on a human body model.

### Project:
* INPUT: Given a 3d model of a human body. {.obj file}

* OUTPUT: set of 3D points of key points on the model body.

### Note:
* OBJ file is a file containing a 3D point cloud.
* If we project all the points in the OBJ file we can plot an image.

### Algorithm:
1. Read all 3d points from the model.

2. Project each point (remove Z values)

3. Use mediaPipe model for landmarks detection on the projected point cloud.



## Authors

- [@ItayKarat](https://github.com/itaykarat)


## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)




<img width="614" alt="image" src="https://user-images.githubusercontent.com/60778119/172612139-5ece4b74-ad7e-432a-a690-288fd7e4b39c.png">

<img width="517" alt="image (4)" src="https://user-images.githubusercontent.com/60778119/172611815-76c00fa5-fd01-46df-ad51-5e56f3dfc0b1.png">

<img width="482" alt="image (5)" src="https://user-images.githubusercontent.com/60778119/172611829-787ee05e-7315-4aef-82c4-68e0ca8816cf.png">

<img width="513" alt="image" src="https://user-images.githubusercontent.com/60778119/172612908-a97df005-b3e3-4996-8d54-b5b4f1b8279c.png">

<img width="509" alt="image" src="https://user-images.githubusercontent.com/60778119/172612233-5f532d05-3cc6-4b31-ba58-b4519e37ffe8.png">

<img width="515" alt="image" src="https://user-images.githubusercontent.com/60778119/172612292-2238a485-9eef-4f88-ad3f-98b08b9715e5.png">

## Output visualization:


<img width="612" alt="image" src="https://user-images.githubusercontent.com/60778119/172612362-e672c41c-4fbd-448e-991f-9ad85257ac49.png">



