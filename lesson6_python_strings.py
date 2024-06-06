# # Product Review Analysis

# # Task 1

# # Program that searches through a series of keywords such as "good", "excellent", "bad", "poor", and "average". Print each review with the keywords in uppercase.

python_reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."] 

keywords = ["good", "excellent", "bad", "poor", "average"]

for reviews in python_reviews:
    for keyword in keywords:
        if keyword in reviews:
            reviews = reviews.replace(keyword, keyword.upper())
    print(reviews)

# Task 2

# Function that tallies number of positiv and negative words in each review. Function should return the count of positive and negative words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def counts():
    positive_count = 0
    negative_count = 0
    for review in python_reviews:
        for word in positive_words:
            if word in review:
                positive_count += 1
        for word in negative_words:
            if word in review:
                negative_count += 1
    
    print(f"Positive words: {positive_count}, Negative count {negative_count}")

counts()

# Task 3 Review Summary

# Implement a function that takes the first 30 characters of a review and appends "…" to create a summary.

def review_summary():
    for review in python_reviews:
        summary = review[:31]

        print(summary + "...")
print("Summary Review")

review_summary()
    


