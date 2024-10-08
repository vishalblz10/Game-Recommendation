import pandas as pd

class DataReader:
    def __init__(self, games_path, recommendations_path):
        """
        Initialize with paths to the games and recommendations datasets.
        """
        self.games_path = games_path
        self.recommendations_path = recommendations_path
        self.df_games = None
        self.df_recom = None

    def read_data(self):
        """
        Read the datasets and store them in DataFrames.
        
        Returns:
            bool: True if data is read successfully, False otherwise.
        """
        try:
            self.df_games = pd.read_csv(self.games_path)
            self.df_recom = pd.read_csv(self.recommendations_path)
            print("Data read successfully.")
            self.print_columns()
            return True
        except Exception as e:
            print(f"Error reading data: {e}")
            return False

    def print_columns(self):
        """
        Print the columns of the DataFrames.
        """
        print("Columns in the Games DataFrame:")
        print(self.df_games.columns.tolist())
        
        print("\nColumns in the Recommendations DataFrame:")
        print(self.df_recom.columns.tolist())