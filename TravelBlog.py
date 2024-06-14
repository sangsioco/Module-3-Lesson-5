import re

# Writing to the travel_blogs.txt file
with open("travel_blogs.txt", 'w') as file:
    file.write(
        '1. "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."\n'
        '2. "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."\n'
        '3. "The city tour was a bit disappointing. The guide wasn\'t very knowledgeable, and the attractions were overcrowded."\n'
        '4. "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."\n'
        '5. "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."\n'
        '6. "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."\n'
        '7. "The food on our trip was excellent. We sampled delicious local cuisine at every stop."\n'
        '8. "The historical tour was enlightening. We learned so much about the culture and heritage of the region."\n'
        '9. "Overall, our travel experience was fantastic. We made unforgettable memories and can\'t wait for our next adventure!"\n'
    )

# Define positive and negative words
positive_words = {"amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "relaxed", "stunning", "memorable", "mesmerizing", "excellent", "delicious", "enlightening", "fantastic", "unforgettable"}
negative_words = {"bad", "disappointing", "poor", "lackluster", "scarce", "overcrowded"}

def sentiment_analysis(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        # Tokenize the text into words
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Count positive and negative words
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        
        return positive_count, negative_count
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return 0, 0

def main():
    # Perform sentiment analysis
    positive_count, negative_count = sentiment_analysis("travel_blogs.txt")
    
    # Print the results
    print(f"Number of positive words: {positive_count}")
    print(f"Number of negative words: {negative_count}")

if __name__ == "__main__":
    main()
