# # script for resize background images
# import os
# import cv2
#
# directory = "C//Users//97254//Documents//CS//ThirdYear//final_project//model_code//resources//background_images"
# new_path = "C//Users//97254//Documents//CS//ThirdYear//final_project//model_code//resources//resized_background_images"
# for image_path in os.listdir(directory):
#     image = cv2.imread(image_path)
#     image = cv2.resize(image, dsize=(1674, 1049))
#     cv2.imwrite(image, new_path)
