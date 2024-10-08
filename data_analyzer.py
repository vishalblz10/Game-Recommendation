class DataAnalyzer:
    def __init__(self, df_games):
        """
        Initialize with the games DataFrame.
        """
        self.df_games = df_games

    def analyze_data(self):
        """
        Analyze data for various insights, such as the distribution of prices and reviews.

        Returns:
            dict: A dictionary with insights.
        """
        insights = {
            'price_distribution': self.df_games['price_final'].describe(),  # Use 'price_final' instead of 'Price'
            'reviews_distribution': self.df_games['user_reviews'].describe(),  # Use 'user_reviews' instead of 'Reviews'
            'most_positive_game': self.df_games.loc[self.df_games['positive_ratio'].idxmax(), 'title'],  # Use 'title'
            'most_negative_game': self.df_games.loc[self.df_games['positive_ratio'].idxmin(), 'title']  # Use 'title'
        }
        return insights
