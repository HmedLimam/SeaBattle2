from load_data import reset_db, process_images
from manip_data import create_heatmap
from cv2 import imwrite
from datetime import datetime as dt

def main():
    """
        Main function to reset the database, process images, create a heatmap,
        and save the heatmap with a timestamp.
    """

    # Reset the database (SeaBattle2.csv)
    reset_db()

    # Process all images in the images/ folder
    # You can alternatively call one_image() to process images one at a time,
    # especially useful after adding a new image.
    dataset_size = process_images()

    # Create a heatmap from the processed images
    heatmap = create_heatmap()

    # Save the heatmap with a timestamp in the heatmaps/ folder
    current_date = dt.now()
    imwrite(f"heatmaps/Heatmap - {dataset_size} images - {current_date.day}{current_date.strftime('%b')}.jpg", heatmap)


if __name__ == '__main__':
    main()