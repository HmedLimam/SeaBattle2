import pandas as pd
import cv2
import numpy as np
from collections import Counter

def get_most_recurring():
    """
    Get the most recurring cells from the SeaBattle2.csv file.

    Returns:
        Counter: A Counter object with cell names as keys and their counts as values.
    """
    df = pd.read_csv("SeaBattle2.csv")
    df = df[df["count"] > 0]
    pd.set_option('display.max_rows', None)
    df = df.sort_values(by="count", ascending=False)

    # Flatten the DataFrame into a list
    flattened_list = [cell_name for cell_name, count in zip(df["cell_name"], df["count"]) for _ in range(count)]
    return Counter(flattened_list)

def get_next_most_recurring(iteration=None):
    """
    Get the next most recurring cell based on the iteration provided.

    Args:
        iteration (int, optional): The iteration index. Defaults to None.

    Returns:
        str: The cell name of the next most recurring cell.
    """
    item_counts = get_most_recurring()
    if not iteration:
        return item_counts.most_common()[0][0]
    else:
        return item_counts.most_common()[iteration][0]

def get_alpha(n):
    """
    Convert a numeric value to its corresponding alphabet.

    Args:
        n (int): The numeric value to convert.

    Returns:
        str: The corresponding alphabet character.
    """
    char_dict = {i: chr(ord('A') + i) for i in range(10)}
    return char_dict[n]

def get_grid_coordinates(cell):
    """
    Get the grid coordinates for a given cell name.

    Args:
        cell (str): The cell name (e.g., 'A0').

    Returns:
        tuple: The row and column coordinates of the cell.
    """
    alpha_part = cell[:-1]
    numeric_part = cell[-1]
    col = int(numeric_part)
    row = ord(alpha_part.upper()) - ord('A')
    return row, col

def create_heatmap():
    """
    Create a heatmap based on the cell counts from the SeaBattle2.csv file.

    Returns:
        np.ndarray: The generated heatmap as an image.
    """
    canvas_size = (600, 600)
    canvas = np.ones((canvas_size[0], canvas_size[1], 3), dtype=np.uint8) * 255  # White background

    # Define grid parameters
    grid_spacing = 60

    # Create vertical grid lines
    for x in range(0, canvas_size[1], grid_spacing):
        cv2.line(canvas, (x, 0), (x, canvas_size[0]), (0, 0, 0), 1)

    # Create horizontal grid lines
    for y in range(0, canvas_size[0], grid_spacing):
        cv2.line(canvas, (0, y), (canvas_size[1], y), (0, 0, 0), 1)

    item_counts = get_most_recurring()
    max_count = max(item_counts.values())

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4
    font_thickness = 1

    for item in item_counts:
        row, col = get_grid_coordinates(item)
        intensity = item_counts[item]
        color = (0, min(255, int(255 * (intensity / max_count))), min(255, int(255 * (1 - intensity / max_count))))

        cv2.rectangle(canvas, (col * grid_spacing, row * grid_spacing),
                      ((col + 1) * grid_spacing, (row + 1) * grid_spacing), color, -1)

        cv2.putText(canvas, str(f"{get_alpha(row)}{col + 1} ({intensity})"),
                    (int((col + 0.15) * grid_spacing), int((row + 0.6) * grid_spacing)),
                    font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

    # Display the canvas with the grid
    cv2.imshow('Grid', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return canvas


if __name__ == '__main__':
    create_heatmap()
