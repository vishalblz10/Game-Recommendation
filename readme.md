Game Recommendation System
Description
This project implements a game recommendation system using a dataset of user recommendations and game details from the Steam Store. The system includes data reading, cleaning, analysis, and visualization components, allowing users to gain insights into the gaming market and player preferences.

Dataset
The dataset used in this project contains over 41 million cleaned and preprocessed user recommendations (reviews) from the Steam Store. It includes detailed information about games and add-ons, as well as user profiles.

Dataset Files
games.csv: Contains information about games, including ratings, pricing, release date, and more.
recommendations.csv: Contains user reviews, including whether the user recommends a product.
Dataset Download
You can download the dataset from the following link: Dataset Download URL

Installation
To run this project, you need to have Python installed on your machine. Additionally, you will need the following libraries:

pandas
matplotlib
seaborn
You can install these libraries using pip:

bash
Copy code
pip install pandas matplotlib seaborn
Usage
Clone this repository:
bash
Copy code
git clone <https://github.com/vishalblz10/Game-Recommendation.git
cd Game-Recommendation-System
Update the dataset paths in the main.py file to point to your local copies of the games.csv and recommendations.csv files.

Run the main script:

bash
Copy code
python main.py
This will read the data, clean it, analyze it, and generate visualizations based on the insights gained from the dataset.

Code Structure
data_reader.py: Contains the DataReader class for reading data from CSV files.
data_cleaner.py: Contains the DataCleaner class for cleaning and preprocessing the data.
data_analyzer.py: Contains the DataAnalyzer class for analyzing the data and generating insights.
data_visualizer.py: Contains the DataVisualizer class for visualizing the data.
Acknowledgements
The dataset was collected from the Steam Official Store. All rights on the dataset thumbnail image belong to the Valve Corporation.

License
This project is licensed under the MIT License.

Instructions
Dataset download link- https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam/data