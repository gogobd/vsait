import os
import random
import shutil


def divide_images(directory_path):
    # Create "train" and "val" directories if they don't exist
    train_path = os.path.join(directory_path, "train")
    val_path = os.path.join(directory_path, "val")
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)

    # Get a list of all image files in the directory
    all_images = [
        file for file in os.listdir(directory_path) if file.endswith(".png")
    ]  # Change the extension accordingly

    # Randomly shuffle the list
    random.shuffle(all_images)

    # Select the first 50 images for "val"
    val_images = all_images[:50]

    # Move "val" images to the "val" directory
    for image in val_images:
        src = os.path.join(directory_path, image)
        dest = os.path.join(val_path, image)
        shutil.move(src, dest)

    # Move the rest to the "train" directory
    for image in all_images[50:]:
        src = os.path.join(directory_path, image)
        dest = os.path.join(train_path, image)
        shutil.move(src, dest)


divide_images(
    "/app/data/external/Shared Data/deeplearning/datasets/GTA/unpack/images/images"
)
divide_images(
    "/app/data/external/Shared Data/deeplearning/datasets/GTA/unpack/labels/labels"
)

print("Files successfully divided into 'train' and 'val' directories.")
