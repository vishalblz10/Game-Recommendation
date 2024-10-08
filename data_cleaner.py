class DataCleaner:
    def __init__(self, df_games):
        """
        Initialize with the games DataFrame.
        """
        self.df_games = df_games

    def clean_data(self):
        """
        Clean the game DataFrame by handling missing values and formatting.
        
        Returns:
            pd.DataFrame: Cleaned games DataFrame.
        """
        initial_shape = self.df_games.shape
        
        # Drop rows with missing values in critical columns
        self.df_games.dropna(subset=['title', 'price_final', 'user_reviews'], inplace=True)

        # Convert data types
        self.df_games['price_final'] = self.df_games['price_final'].replace('[\$,]', '', regex=True).astype(float)
        self.df_games['user_reviews'] = self.df_games['user_reviews'].astype(int)
        self.df_games['positive_ratio'] = self.df_games['positive_ratio'].astype(float)  # Assuming positive_ratio is float
        # Add more conversions as needed

        # Check for duplicates
        initial_duplicates = self.df_games.duplicated().sum()
        self.df_games.drop_duplicates(inplace=True)
        final_duplicates = self.df_games.duplicated().sum()

        # Reset index
        self.df_games.reset_index(drop=True, inplace=True)

        cleaned_shape = self.df_games.shape

        print(f"Cleaned data: {initial_shape} -> {cleaned_shape} rows")
        print(f"Removed {initial_duplicates - final_duplicates} duplicate rows")
        
        # Additional checks for column types
        print("Data types after cleaning:")
        print(self.df_games.dtypes)
        
        # Check for any remaining missing values
        missing_values = self.df_games.isnull().sum().sum()
        if missing_values > 0:
            print(f"Warning: There are still {missing_values} missing values in the data.")
        else:
            print("No missing values remain in the data.")

        return self.df_games
