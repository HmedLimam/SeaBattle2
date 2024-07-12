import glob
import cv2
import numpy as np
import pandas as pd

def reset_db():
    """
    Reset the database by setting the 'count' of all cells to 0.
    """
    df = pd.read_csv("SeaBattle2.csv")
    df['count'] = 0
    df.to_csv('SeaBattle2.csv', index=False)

def update_db(cell_name):
    """
    Update the database by incrementing the 'count' of the specified cell.

    Args:
        cell_name (str): The name of the cell to update.
    """
    df = pd.read_csv("SeaBattle2.csv")
    df.loc[df['cell_name'] == cell_name, 'count'] += 1
    df.to_csv('SeaBattle2.csv', index=False)

def one_image(path, update=False, reset=False, show=False):
    """
    Process a single image to analyze cell opacities, update the database, 
    and optionally display the processed image with overlays.

    Args:
        path (str): The path to the image to process.
        update (bool): Whether to update the database.
        reset (bool): Whether to reset the database before processing.
        show (bool): Whether to display the processed image.
    """
    if reset:
        reset_db()

    image_path = path
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = 10, 10
    cell_size = 79  # Adjust this value based on your preference

    char_dict = {i: chr(ord('A') + i) for i in range(10)}

    # Create a new three-channel image with the same dimensions as the grayscale image
    img_gray_colored = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

    # Draw grid lines
    for i in range(0, rows * cell_size, cell_size):
        cv2.line(img_gray_colored, (0, i), (cols * cell_size, i), (0, 255, 0), 1)  # Green horizontal lines
    for j in range(0, cols * cell_size, cell_size):
        cv2.line(img_gray_colored, (j, 0), (j, rows * cell_size), (0, 255, 0), 1)  # Green vertical lines

    # Draw circles in cells based on opacity sum
    for i in range(0, rows * cell_size, cell_size):
        for j in range(0, cols * cell_size, cell_size):
            cell = img_gray[i:i + cell_size, j:j + cell_size]
            opacity_sum = np.sum(cell)
            cell_name = f"{char_dict[i // cell_size]}{j // cell_size}"

            if opacity_sum <= 1020000:  # Adjust threshold as needed
                color = (0, 255, 0)  # Green color
                if update:
                    update_db(cell_name)
            else:
                color = (0, 0, 255)  # Red color

            center = (j + cell_size // 2, i + cell_size // 2)
            cv2.circle(img_gray_colored, center, 10, color, -1)  # Draw filled circle

    if show:
        result_img = cv2.addWeighted(img_gray_colored, 0.7, img, 0.3, 0)
        scaled_img_gray_colored = cv2.resize(result_img, (0, 0), fx=0.8, fy=0.8)
        cv2.imshow('Overlay Result', scaled_img_gray_colored)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def process_images():
    """
    Process all images in the 'images' folder, update the database, 
    and return the number of images processed.

    Returns:
        int: The number of images processed.
    """
    data_images = glob.glob("images/*.jpg")
    for img in data_images:
        one_image(img, update=True, reset=False, show=False)
    return len(data_images)
