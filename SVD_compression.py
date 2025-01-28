from PIL import Image
import numpy as np
from numpy.linalg import svd

# load the Alice image from Downloads folder in GIF format
image_path = '/Users/drazenbeatovic/Downloads/p5_image.gif'
Alice_image = Image.open(image_path)

# convert image to black and white binary format, where black is represented as 0, white as 1
Alice_image_bw = Alice_image.convert("1")

# save binary pixel values of image into an array
binary_matrix = np.array(Alice_image_bw).astype(int)

# perform SVD on the binary matrix and store result
U, S, VT = svd(binary_matrix, full_matrices=False)

k_values = [1, 3, 10, 20, 50, 100, 150, 200, 400, 800, 1170]

# loop over each rank and reconstruct Alice image based on rank k approximation
# stores images in a dictionary based on each k value
reconstructed_images = {}

for k in k_values:
    # take only k singular values for reconstruction
    S_k = np.diag(S[:k])
    U_k = U[:, :k]
    VT_k = VT[:k, :]
    Alice_image_k_reconstructed = np.dot(U_k, np.dot(S_k, VT_k))

    # clip pixel values in image to be between 0 and 1
    Alice_image_k_reconstructed = np.clip(Alice_image_k_reconstructed, 0, 1)

    # store current image in dictionary
    reconstructed_images[k] = Alice_image_k_reconstructed

# retrieve the recovered drawing for k = 150
Alice_k_150_image = reconstructed_images[150]

# scale and clip the current drawing pixel values back to normal pixel range [0 to 255]
Alice_k_150_image = (Alice_k_150_image * 255).astype(np.uint8)
Alice_k_150_image = np.clip(Alice_k_150_image, 0, 255)

# ensure data type of drawing is correct for image visualization
Alice_k_150_image = Alice_k_150_image.astype(np.uint8)

# save the recovered drawing to same folder
Alice_drawing_150 = Image.fromarray(Alice_k_150_image)
Alice_drawing_150.save('/Users/drazenbeatovic/Downloads/recovered_drawing_k150.gif')