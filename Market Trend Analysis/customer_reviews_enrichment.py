# pip install pandas nltk pyodbc sqlalchemy

import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis if not already present
nltk.download('vader_lexicon')

# Function to fetch data from a SQL database using a SQL query
def fetch_data_from_sql():
    # Define the connection string with parameters for the database connection
    conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost,1433;"
    "Database=PortfolioProject_MarketingAnalytics;"
    "UID=sa;"
    "PWD=Admin@1234;"
    "TrustServerCertificate=yes;"
)


    
    # Establish the connection
    conn = pyodbc.connect(conn_str)
    
    # SQL query to fetch customer reviews data
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM customer_reviews"

    
    # Fetch data into DataFrame
    df = pd.read_sql(query, conn)
    
    # Close the connection
    conn.close()
    
    return df

# Fetch data
customer_reviews_df = fetch_data_from_sql()

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment score
def calculate_sentiment(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']

# Categorize sentiment using both score and rating
def categorize_sentiment(score, rating):
    if score > 0.05:
        if rating >= 4:
            return 'Positive'
        elif rating == 3:
            return 'Mixed Positive'
        else:
            return 'Mixed Negative'
    elif score < -0.05:
        if rating <= 2:
            return 'Negative'
        elif rating == 3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:
        if rating >= 4:
            return 'Positive'
        elif rating <= 2:
            return 'Negative'
        else:
            return 'Neutral'

# Score bucketing
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'

# Apply transformations
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Output preview
print(customer_reviews_df.head())

# Save to CSV
customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)
