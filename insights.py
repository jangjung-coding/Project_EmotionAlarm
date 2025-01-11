# insights.py

from collections import Counter
from response_storage import load_responses

def generate_insights():
    responses = load_responses()
    
    if not responses:
        return "No responses yet. Start reflecting today!"

    # Analyze most common words in responses (basic example)
    all_responses = " ".join([resp["response"] for resp in responses])
    words = all_responses.split()
    
    most_common_words = Counter(words).most_common(3)
    
    insights = "\nYour Top Words:\n"
    for word, count in most_common_words:
        insights += f"- {word}: {count} times\n"
    
    return insights
