# Twitter Bitcoin Sentiment Analysis using PySpark

This project implements a sentiment analysis system for Bitcoin-related tweets using PySpark, combining both traditional sentiment analysis techniques (VADER, AFINN) and machine learning approaches.

## Project Overview

The project analyzes Twitter data related to Bitcoin to understand public sentiment and its potential correlation with Bitcoin price movements. It uses a combination of:
- VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis
- AFINN sentiment scoring
- Machine learning models (Logistic Regression, Naive Bayes)
- PySpark for big data processing

## Features

- Data preprocessing and cleaning of Twitter text data
- Multiple sentiment analysis approaches:
  - VADER sentiment analysis
  - AFINN sentiment scoring
  - Combined sentiment metrics
- Text feature extraction using:
  - Tokenization
  - Stop words removal
  - TF-IDF vectorization
- Machine learning classification
- Support for both balanced and unbalanced datasets

## Dataset

The project uses multiple Twitter datasets:
- balanced_twitter_btc_small.csv
- balanced_twitter_btc_big.csv
- unbalanced_twitter_btc_big.csv

Each dataset contains the following features:
- user_followers: Number of followers for the tweet author
- user_verified: Verification status of the user
- date: Tweet timestamp
- text: Raw tweet text
- hard_cleaned_text: Heavily preprocessed text
- soft_cleaned_text: Lightly preprocessed text
- vader_sentiment: Sentiment score from VADER
- afinn_sentiment: Sentiment score from AFINN
- sentiment: Combined sentiment score
- label: Sentiment classification (0: Positive, 1: Neutral, 2: Negative)

## Requirements

- Python 3.x
- PySpark
- NLTK
- pandas
- matplotlib
- seaborn
- wordcloud

For detailed package versions, see `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ameer22l7555/twitter-btc-sentiment-analysis-pyspark.git
cd twitter-btc-sentiment-analysis-pyspark
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Download required NLTK data:
```python
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')
```

## Usage

The main analysis is contained in the `Analysis.ipynb` Jupyter notebook. To run the analysis:

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `Analysis.ipynb`
3. Follow the notebook cells for step-by-step analysis

## Project Structure

```
├── Analysis.ipynb          # Main analysis notebook
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── Documentation.docx     # Detailed project documentation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.