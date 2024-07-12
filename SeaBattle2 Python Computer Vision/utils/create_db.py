import pandas as pd

def generate_cell_names():
    """
    Generate cell names from A0 to J9.

    Returns:
        list: A list of cell names from A0 to J9.
    """
    return [f"{chr(65 + i)}{j}" for i in range(10) for j in range(10)]

def create_dataframe(cell_names):
    """
    Create a DataFrame with cell names and default count values set to 0.

    Args:
        cell_names (list): A list of cell names.

    Returns:
        pd.DataFrame: A DataFrame with cell names and count values.
    """
    return pd.DataFrame({'cell_name': cell_names, 'count': 0})

def save_dataframe_to_csv(df, filename):
    """
    Save the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        filename (str): The name of the CSV file.
    """
    df.to_csv(filename, index=False)

def main():
    """
    Main function to generate cell names, create a DataFrame,
    save it to a CSV file, and display the DataFrame.
    """
    cell_names = generate_cell_names()
    df = create_dataframe(cell_names)
    save_dataframe_to_csv(df, 'SeaBattle2.csv')


if __name__ == '__main__':
    main()