import pandas as pd
import json

def csv_to_json(csv_filepath, json_filepath):
    """Converts a CSV file to a JSON file with the specified format."""

    try:
        df = pd.read_csv(csv_filepath)

        data = []
        for index, row in df.iterrows():
            data.append({
                "Context": row['Context'],  # Replace 'context' with your context column name
                "Question": row['Question'],  # Replace 'question' with your question column name
                "Answer": row['Answer']  # Replace 'answer' with your answer column name
            })

        with open(json_filepath, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Successfully converted {csv_filepath} to {json_filepath}")

    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_filepath}")
    except KeyError as e:
        print(f"Error: Column name {e} not found in the CSV file. Please check the column names.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:

csv_file = r'C:\Users\wanji\chatbot\chatbot\maindataset.csv' 
json_file = r'C:\Users\wanji\chatbot\chatbot\data.json'
csv_to_json(csv_file, json_file)