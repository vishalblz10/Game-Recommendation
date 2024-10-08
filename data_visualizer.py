import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, df_games):
        """
        Initialize with the games DataFrame.
        """
        self.df_games = df_games

    def visualize_data(self):
        """
        Create visualizations to better understand the dataset.
        """
        # Price distribution
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df_games['price_final'], bins=30, kde=True)  # Use 'price_final' instead of 'Price'
        plt.title('Price Distribution of Games')
        plt.xlabel('Price (in $)')
        plt.ylabel('Frequency')
        plt.show()

        # Reviews distribution
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df_games['user_reviews'], bins=30, kde=True, color='orange')  # Use 'user_reviews'
        plt.title('Reviews Distribution of Games')
        plt.xlabel('Number of Reviews')
        plt.ylabel('Frequency')
        plt.show()

        # Positive vs Negative Reviews
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x=self.df_games['positive_ratio'], y=self.df_games['user_reviews'])
        plt.title('Positive Ratio vs User Reviews')
        plt.xlabel('Positive Ratio')
        plt.ylabel('User Reviews')
        plt.show()
