from flask import Flask, request, jsonify
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
from nltk.corpus import wordnet
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
# initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Initialize Sentiment Intensity Analyzer
sid = SentimentIntensityAnalyzer()


# Define keywords and responses
greeting_keywords = ['hi', 'hello', 'hey', 'hi there', 'hello there']
symptom_keywords = ['anxious', 'anxiety', 'stressed', 'stress', 'depressed', 'depression', 'sad', 'lonely']
thought_keywords = ['negative', 'pessimistic', 'hopeless', 'helpless', 'overthinking', 'rumination']
behavior_keywords = ['avoidance', 'procrastination', 'isolation']
technique_keywords = ['thought challenging', 'behavioral activation', 'relaxation', 'self-care']
goodbye_keywords = ['exit', 'quit', 'goodbye', 'bye']

greetings = ['Hello! I\'m an AI chatbot programmed to assist with mental health concerns. How are you feeling today?', 
             'Hi! I\'m here to help with your mental health concerns. How can I assist you today?', 
             'Welcome! I\'m an AI chatbot designed to support you with your mental health. What\'s been on your mind lately?']
symptom_responses = ['I\'m sorry to hear that you are feeling {}. Can you tell me more about what\'s been causing your {}?', 
                     'It sounds like you are experiencing {}. Would you like to talk more about what\'s been going on?', 
                     'Feeling {} can be tough. Would you like to tell me more about what\'s been happening?']
thought_responses = ['I\'m sorry you are having negative thoughts. Let\'s challenge them. Can you provide me an example of one negative thought you are having?',
                     'I understand you are having pessimistic thoughts. Can you provide me an example?',
                     'I\'m sorry to hear that you feel hopeless. Can you give me an example of a negative thought you\'ve been having?']
behavior_responses = ['I see that you are avoiding certain situations. Let\'s work on this. Can you give me an example of one situation you have been avoiding?',
                      'Procrastination can be tough. Can you tell me more about the tasks you have been putting off?',
                      'It sounds like you have been isolating yourself. Would you like to talk more about why that is?']
technique_responses = ['Great, let\'s start with a thought challenging exercise. Here\'s an example: {}, can you provide me an alternative thought to this?',
                       'Behavioral activation can be helpful. Let\'s set a goal to complete one task today, even if it\'s small. What do you want to accomplish?',
                       'Self-care is important. Let\'s try a relaxation technique such as deep breathing or progressive muscle relaxation. Would you like to try one now?']
unknown_response = ['I\'m sorry, I don\'t understand. Can you please rephrase that?', 
                    'I\'m not sure I understand what you mean. Can you please clarify?', 
                    'I\'m having trouble understanding. Can you please provide more information?']
goodbye_responses = ['Goodbye!', 'Take care.', 'Until next time.']



def get_wordnet_pos(token):
    tag = nltk.pos_tag([token])[0][1][0].upper() #extract the information
    tag_dict = {"J": wordnet.ADJ, #map
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN) #guess noun if unknown


# Define a function to process user input
def process_input(user_input):
    # Get sentiment score
    sentiment_score = sid.polarity_scores(user_input)['compound']
    
    # Initialize variables
    greeting = False
    symptom = False
    thought = False
    behavior = False
    technique = False
    goodbye = False
    
    # tokenize user input
    tokens = nltk.word_tokenize(user_input.lower())
    
    # lemmatize tokens
    lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokens]
    
    # check for keywords
    if any(keyword in lemmatized_tokens for keyword in greeting_keywords):
        greeting = True
    if any(keyword in lemmatized_tokens for keyword in symptom_keywords):
        symptom = True
    if any(keyword in lemmatized_tokens for keyword in thought_keywords):
        thought = True
    if any(keyword in lemmatized_tokens for keyword in behavior_keywords):
        behavior = True
    if any(keyword in lemmatized_tokens for keyword in technique_keywords):
        technique = True
    if any(keyword in lemmatized_tokens for keyword in goodbye_keywords):
        goodbye = True
    
    # generate a response based on the keywords
    if greeting:
        response = random.choice(greetings)
    elif symptom:
        response = random.choice(symptom_responses)
    elif thought:
        response = random.choice(thought_responses)
    elif behavior:
        response = random.choice(behavior_responses)
    elif technique:
        response = random.choice(technique_responses)
    elif goodbye:
        response = random.choice(goodbye_responses)
    else:
        response = random.choice(unknown_response)
    
    return response

# Initialize Flask app
app = Flask(__name__, static_url_path='', static_folder='static')

# Define a route to handle user input and return the sentiment analysis result
@app.route('/chatbot', methods=['POST'])

# Define a function to start the chatbot
def chatbot():

    while True:
        # Get user input
        user_input = request.form['user_input']

        # Check for exit command
        if user_input.lower() in ['exit', 'quit', 'goodbye', 'bye']:
            print("Goodbye!")
            break

        # Generate a response and print it
        response_ = process_input(user_input)
        print(response_)
        return jsonify({'response': response_})

# Define a route to serve the website
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)