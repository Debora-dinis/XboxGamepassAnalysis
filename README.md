
# Xbox Game Pass Scraper
Curiosity about what's on Xbox Game Pass Ultimate and the absence of readily available datasets led to the creation of this web scraper. You can check out all the Game Pass analysis results right [here](https://debora-dinis.github.io/project7.html).
This Python script scrapes game data from the Xbox Game Pass website and creates several CSV files containing information about the games, their platforms, genres, and features. This documentation provides an overview of the code and its functionality.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [File Structure](#file-structure)

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- Selenium library installed. You can install it using pip:

  ```
  pip install selenium
  ```

- Chrome WebDriver installed and added to your system's PATH.

- The following Python packages should be installed: pandas.

  ```
  pip install pandas
  ```

## Usage

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/xbox-game-pass-scraper.git
   ```

2. Navigate to the project directory:

   ```
   cd xbox-game-pass-scraper
   ```

3. Run the script:

   ```
   python scrape_xbox_game_pass.py
   ```

4. After running the script, the following CSV files will be generated:

   - `platforms.csv`: Contains information about which platform each game is available on.
   - `genres.csv`: Contains information about the genres of each game.
   - `features.csv`: Contains information about various features of each game.
   - `xbox.csv`: Contains detailed information about all the games available on Xbox Game Pass.

## Code Explanation

The script consists of the following main components:

- Importing necessary libraries, including Selenium and pandas.
- Configuring a headless Chrome browser using Selenium to scrape data from the Xbox Game Pass website.
- Extracting game data and storing it in a dictionary.
- Creating data frames to store information about platforms, genres, and features for each game.
- Populating these data frames with 1s and 0s to represent whether each game possesses the respective attributes.
- Exporting the data frames to CSV files.



## File Structure

- `scrape_xbox_game_pass.py`: The main Python script for scraping Xbox Game Pass data.
- `gamesByFeature.py`: Module for extracting games by feature.
- `gamesByGenre.py`: Module for extracting games by genre.
- `gamesByPlatform.py`: Module for extracting games by platform.
- `utils/set200games.py`: Utility module to set the number of games per page to 200.
- `xboxallgames.py`: Module for extracting all games.
- `platforms.csv`: CSV file containing platform information.
- `genres.csv`: CSV file containing genre information.
- `features.csv`: CSV file containing feature information.
- `xbox.csv`: CSV file containing detailed game information.











