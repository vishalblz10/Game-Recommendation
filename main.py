from data_reader import DataReader
from data_cleaner import DataCleaner
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer

if __name__ == "__main__":
    games_path = "D:/inputs/game_data/games.csv"
    recommendations_path = "D:/inputs/game_data/recommendations.csv"

    # Step 1: Read Data
    reader = DataReader(games_path, recommendations_path)
    if reader.read_data():
        # Step 2: Clean Data
        cleaner = DataCleaner(reader.df_games)
        cleaned_df = cleaner.clean_data()

        # Step 3: Analyze Data
        analyzer = DataAnalyzer(cleaned_df)
        insights = analyzer.analyze_data()

        print("Insights:")
        for key, value in insights.items():
            print(f"{key}: {value}")

        # Step 4: Visualize Data
        visualizer = DataVisualizer(cleaned_df)
        visualizer.visualize_data()
