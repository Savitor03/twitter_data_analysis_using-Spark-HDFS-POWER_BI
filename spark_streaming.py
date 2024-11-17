import tweepy

# Twitter API credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAErRwwEAAAAAkAzxq1f%2Bta57e9C2gbUbrDonyGc%3DGiN2Z3ZbBPSQMkUMYBmyUvJn5BIyDFhd4izjMfU3iypBds4Fkd'  # Replace with your actual Bearer Token

# Create a stream listener class using StreamingClient
class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)  # Print the tweet text

    def on_error(self, status_code):
        print(f"Error: {status_code}")
        return False  # Disconnect on error

# Initialize the stream listener
listener = MyStreamListener(bearer_token=bearer_token)

# Add rules to filter tweets based on keywords
try:
    listener.add_rules(tweepy.StreamRule("spark OR data OR big data"))  # Keywords to track
    print("Rules added successfully!")
except Exception as e:
    print(f"Error adding rules: {e}")

# Start streaming
print("Streaming tweets...")
listener.filter(tweet_fields=["text"])
