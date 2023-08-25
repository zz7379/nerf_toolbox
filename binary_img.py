import cv2

# Load image in grayscale
# import ipdb;ipdb.set_trace()
input = 'p1.png'
img = cv2.imread(input, cv2.IMREAD_GRAYSCALE)

# Binarize image using thresholding
thresh_value = 222
max_value = 255
thresh_type = cv2.THRESH_BINARY
_, bin_img = cv2.threshold(img, thresh_value, max_value, thresh_type)
bin_img = cv2.cvtColor(bin_img, cv2.COLOR_GRAY2BGR)

# Save binarized image
cv2.imwrite(f'binarized_{input}', bin_img)
bin_img = ~bin_img
cv2.imwrite(f'binarized_{input}', bin_img)

