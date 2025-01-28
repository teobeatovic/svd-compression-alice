# SVD for Image Compression: Alice and the Cheshire Cat
# Overview
Using Singular Value Decomposition (SVD), a 1600×1170 drawing of Alice conversing with the Cheshire Cat is compressed and approximated. The image is treated as a matrix where black pixels are represented by 0 and white pixels by 1. SVD is performed on the binary matrix representation of the Alice image and approximations with ranks k = {1, 3, 10, 20, 50, 100, 150, 200, 400, 800, 1170} are reconstructed. The reconstructed image for k = 150 is saved.

# Files
* p5_image.gif: Input image of Alice and the Cheshire Cat in black-and-white GIF format.
* SVD_compression.py: The code processes the image, applies SVD, and reconstructs low-rank approximations.
* recovered_drawing_k150.gif: Output image for k = 150 rank approximation.

# Dependencies
The following libraries are required to run the Python script:
* Pillow: For image loading, processing, and saving.
* NumPy: For matrix operations and Singular Value Decomposition (SVD).

# How to Run
1. Place the p5_image.gif file in your local system and update the image_path variable in the script with its location.
2. Execute the Python script SVD_compression.py.
3. The reconstructed image for k = 150 will be saved as recovered_drawing_k150.gif in the same folder.
