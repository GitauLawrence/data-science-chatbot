from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sentence_transformers import SentenceTransformer, util
import numpy as np
import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
import json

class ActionAnswerQuestion(Action):
    def __init__(self):
        # Load the Sentence BERT model
        self.model = SentenceTransformer('all-mpnet-base-v2')

        # Load question embeddings
        self.question_embeddings = np.load('question_embeddings.npy')

        # Load question to index mapping
        with open('question_to_index.json', 'r') as f:
            self.question_to_index = json.load(f)

        # Create a reverse mapping from index to context
        self.index_to_context = {index: context for context, index in self.question_to_index.items()}

        # Load your question-answer dataset from CSV
        self.data = pd.read_csv('data.csv')

        # Normalize question in the DataFrame
        self.data['question'] = self.data['question'].str.strip().str.lower()

        print("Data loaded successfully")

    def name(self) -> Text:
        return "action_answer_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Get the user's question
        user_question = tracker.latest_message['text']
        print(f"User question: {user_question}")

        # 2. Get the user's intent
        user_intent = tracker.latest_message['intent'].get('name')
        print(f"User intent: {user_intent}")

        # 3. Encode the user's question using Sentence BERT
        question_embedding = self.model.encode(user_question)

        # 4. Calculate cosine similarity
        cos_scores = util.cos_sim(question_embedding, self.question_embeddings)[0]
        print(f"Cosine similarity scores: {cos_scores}")

        # 5. Find the index of the most similar context
        top_result_index = int(np.argmax(cos_scores))
        print(f"Top result index: {top_result_index}")

        # Print to check if top_result_index is a valid key
        print(f"Top result index type: {type(top_result_index)}")

        # Set a similarity threshold
        similarity_threshold = 0.65  # You can adjust this value

        # 6. Retrieve the most similar question, corresponding answer, and context
        matched_question = None
        matched_answer = None
        matched_context = None

        # Check if the top score is above the threshold
        if cos_scores[top_result_index] >= similarity_threshold:
            for question, index in self.question_to_index.items():
                if index == top_result_index:
                    matched_question = question
                    break

            if matched_question:
                matched_row = self.data[self.data['question'] == matched_question]
                if not matched_row.empty:
                    matched_answer = matched_row.iloc[0]['answer']
                    matched_context = matched_row.iloc[0]['context']

        # 7. Respond based on whether a match was found
        if matched_answer:
            # Provide the answer directly
            dispatcher.utter_message(text=matched_answer)

            # Store the matched context in a slot
            return [SlotSet("context", matched_context)]
        else:
            dispatcher.utter_message(text="I couldn't find a relevant answer to your question in my knowledge base.")

        return []

class ActionProvideContext(Action):
    def name(self) -> Text:
        return "action_provide_context"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the context from the slot
        context = tracker.get_slot("context")

        if context:
            dispatcher.utter_message(text=f"Here's the context: {context}")
        else:
            dispatcher.utter_message(text="I don't have any context stored for the previous question.")

        return []