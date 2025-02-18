import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim 

def compare_images(img1, img2, threshold=0.9):
    """Compare two images using Structural Similarity Index (SSIM)."""
    img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        return False  # If any image is missing, assume not similar

    img1 = cv2.resize(img1, (256, 256))
    img2 = cv2.resize(img2, (256, 256))

    similarity = ssim(img1, img2)
    return similarity >= threshold

def remove_similar_images(folder_path, threshold=0.9):
    """Deletes images in a folder that are similar to their 5 neighbors, keeping only the last occurrence."""
    images = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png'))])

    if not images:
        print("No images found in the folder.")
        return

    keep = set(images)  # Start by assuming we keep all images

    for i in range(len(images)):
        for j in range(1, 6):  # Compare with 5 above and 5 below
            if i + j < len(images):  # Check below
                if compare_images(images[i], images[i + j], threshold):
                    keep.discard(images[i])  # Remove the earlier duplicate

            if i - j >= 0:  # Check above
                if compare_images(images[i], images[i - j], threshold):
                    keep.discard(images[i - j])  # Remove the earlier duplicate

    # Delete images that are not in the keep set
    for img in images:
        if img not in keep:
            os.remove(img)
            print(f"Deleted: {img}")

    print("Similar image removal completed. Remaining images:", len(keep))

# Example usage
folder_path = "path_to_your_images"
remove_similar_images(folder_path, threshold=0.9)
