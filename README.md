# Data Science and Machine Learning Q&A Chatbot

This project implements a question-answering chatbot using Rasa Open Source, designed to provide information and answer questions related to data science and machine learning concepts, algorithms, and techniques.  The chatbot utilizes Sentence-BERT embeddings for semantic similarity matching to retrieve answers from a predefined knowledge base. It also includes a simple, responsive web-based frontend for easy interaction.

## Features

*   **Question Answering:** Answers user questions based on a curated knowledge base of data science and machine learning topics.
*   **Semantic Similarity:** Uses Sentence-BERT (`all-mpnet-base-v2`) embeddings to match user questions to the most relevant questions in the knowledge base, even with variations in phrasing.
*   **Rasa Framework:** Built on the Rasa Open Source conversational AI framework, providing robust NLU and dialogue management.
*   **Custom Action:** Implements a Python custom action (`action_answer_question`) to handle the core question-answering logic.
*   **Fallback Handling:** Includes a fallback mechanism (`utter_default`) for cases where the chatbot doesn't understand the user's question.
*   **Context Handling (Optional):**  Provides the option to show the context associated with an answer, upon user request (using the `show_context` intent and `action_provide_context` action).
*   **Web Frontend:** Includes a basic, responsive web interface (HTML, CSS, JavaScript) for interacting with the chatbot.
*   **Typing Indicator**: Includes a typing indicator for a better user experience
*   **Quick Replies**: Includes quick replies.
* **User and Bot Avatars:** Includes user and bot avatars.

## Prerequisites

*   **Python 3.8, 3.9, or 3.10:**  Rasa 3.x requires one of these Python versions.  *Do not use Python 3.11+*.  Using a virtual environment (conda or venv) is highly recommended.
*   **Git:**  For cloning the repository.
* **yq (Optional, but strongly recommended for YAML formatting):** Installation instructions for `yq` are below. Using `yq` will prevent YAML syntax errors.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/GitauLawrence/data-science-chatbot.git)  # Replace with your repository URL
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a virtual environment (choose ONE method):**

    *   **Using conda (recommended):**

        ```bash
        conda create -n chatbot python=3.10  # Or 3.8 or 3.9
        conda activate chatbot
        ```

    *   **Using venv:**

        ```bash
        python3.10 -m venv .venv  # Or python3.9, python3.8
        source .venv/bin/activate  # On Linux/macOS
        .venv\Scripts\activate  # On Windows
        ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
   *(Make sure you created the requirements.txt using `pip freeze > requirements.txt`)*

4. **Install yq (Optional, but HIGHLY recommended):**
   This helps in automatically formatting your yaml files.
    * **Windows (using Chocolatey - Recommended):**
    Open Command Prompt as Administrator
      ```
      choco install yq -y
      ```
    * **Windows (using scoop):**
      ```
      scoop install yq
      ```
     * **macOS (using Homebrew):**
      ```bash
      brew install yq
      ```
     * **Linux (using Snap):**
       ```bash
       sudo snap install yq
       ```

5.  **Generate Embeddings:**

    Run the `generate_embeddings.py` script to create the question embeddings and index:

    ```bash
    python generate_embeddings.py
    ```
    This script reads your `data.csv` file, generates embeddings using the Sentence-BERT model, and saves them to `question_embeddings.npy` and `question_to_index.json`.  Make sure your `data.csv` is correctly formatted.

## Running the Chatbot

1.  **Start the Action Server (in one terminal):**

    ```bash
    rasa run actions --debug
    ```

    The `--debug` flag is helpful for development.

2.  **Start the Rasa Server (in a *separate* terminal):**

    ```bash
    rasa run -m models --enable-api --cors "*" --debug
    ```

3.  **Open the Frontend:**

    Open the `frontend/index.html` file in your web browser. You can do this by simply double-clicking the `index.html` file, or by right-clicking and selecting "Open with" -> your browser. No separate web server is needed for this basic setup.

4.  **Chat!:**  Type your data science and machine learning questions into the input field and press Enter or click the "Send" button.

## Project Structure

2.0 Pro Experimental. Lacks access to real-time info and some Gemini features.
Okay, let's craft a professional and informative README.md file for your data science chatbot project. I'll include sections for description, features, installation, usage, contributing (optional), and license (also optional, but highly recommended). I'll use Markdown formatting for readability.

Markdown

# Data Science and Machine Learning Q&A Chatbot

This project implements a question-answering chatbot using Rasa Open Source, designed to provide information and answer questions related to data science and machine learning concepts, algorithms, and techniques.  The chatbot utilizes Sentence-BERT embeddings for semantic similarity matching to retrieve answers from a predefined knowledge base. It also includes a simple, responsive web-based frontend for easy interaction.

## Features

*   **Question Answering:** Answers user questions based on a curated knowledge base of data science and machine learning topics.
*   **Semantic Similarity:** Uses Sentence-BERT (`all-mpnet-base-v2`) embeddings to match user questions to the most relevant questions in the knowledge base, even with variations in phrasing.
*   **Rasa Framework:** Built on the Rasa Open Source conversational AI framework, providing robust NLU and dialogue management.
*   **Custom Action:** Implements a Python custom action (`action_answer_question`) to handle the core question-answering logic.
*   **Fallback Handling:** Includes a fallback mechanism (`utter_default`) for cases where the chatbot doesn't understand the user's question.
*   **Context Handling (Optional):**  Provides the option to show the context associated with an answer, upon user request (using the `show_context` intent and `action_provide_context` action).
*   **Web Frontend:** Includes a basic, responsive web interface (HTML, CSS, JavaScript) for interacting with the chatbot.
*   **Typing Indicator**: Includes a typing indicator for a better user experience
*   **Quick Replies**: Includes quick replies.
* **User and Bot Avatars:** Includes user and bot avatars.

## Prerequisites

*   **Python 3.8, 3.9, or 3.10:**  Rasa 3.x requires one of these Python versions.  *Do not use Python 3.11+*.  Using a virtual environment (conda or venv) is highly recommended.
*   **Git:**  For cloning the repository.
* **yq (Optional, but strongly recommended for YAML formatting):** Installation instructions for `yq` are below. Using `yq` will prevent YAML syntax errors.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)  # Replace with your repository URL
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a virtual environment (choose ONE method):**

    *   **Using conda (recommended):**

        ```bash
        conda create -n chatbot python=3.10  # Or 3.8 or 3.9
        conda activate chatbot
        ```

    *   **Using venv:**

        ```bash
        python3.10 -m venv .venv  # Or python3.9, python3.8
        source .venv/bin/activate  # On Linux/macOS
        .venv\Scripts\activate  # On Windows
        ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
   *(Make sure you created the requirements.txt using `pip freeze > requirements.txt`)*

4. **Install yq (Optional, but HIGHLY recommended):**
   This helps in automatically formatting your yaml files.
    * **Windows (using Chocolatey - Recommended):**
    Open Command Prompt as Administrator
      ```
      choco install yq -y
      ```
    * **Windows (using scoop):**
      ```
      scoop install yq
      ```
     * **macOS (using Homebrew):**
      ```bash
      brew install yq
      ```
     * **Linux (using Snap):**
       ```bash
       sudo snap install yq
       ```

5.  **Generate Embeddings:**

    Run the `generate_embeddings.py` script to create the question embeddings and index:

    ```bash
    python generate_embeddings.py
    ```
    This script reads your `data.csv` file, generates embeddings using the Sentence-BERT model, and saves them to `question_embeddings.npy` and `question_to_index.json`.  Make sure your `data.csv` is correctly formatted.

## Running the Chatbot

1.  **Start the Action Server (in one terminal):**

    ```bash
    rasa run actions --debug
    ```

    The `--debug` flag is helpful for development.

2.  **Start the Rasa Server (in a *separate* terminal):**

    ```bash
    rasa run -m models --enable-api --cors "*" --debug
    ```

3.  **Open the Frontend:**

    Open the `frontend/index.html` file in your web browser. You can do this by simply double-clicking the `index.html` file, or by right-clicking and selecting "Open with" -> your browser. No separate web server is needed for this basic setup.

4.  **Chat!:**  Type your data science and machine learning questions into the input field and press Enter or click the "Send" button.

## Project Structure

chatbot/
├── actions/
│   └── actions.py          # Custom action code.
├── data/
│   ├── nlu.yml             # NLU training data.
│   ├── rules.yml            # Dialogue rules.
│   ├── stories.yml          # Dialogue stories.
│   └── data.csv              # Knowledge base (CSV format).
├── models/                 # Trained Rasa models (ignored by Git).
├── config.yml              # Rasa configuration.
├── domain.yml              # Rasa domain.
├── credentials.yml         # (Empty in this basic setup).
├── endpoints.yml           # (Default action endpoint).
├── question_embeddings.npy     # (Generated by generate_embeddings.py).
├── question_to_index.json   # (Generated by generate_embeddings.py).
├── frontend/               # Frontend files.
│   ├── index.html
│   ├── style.css
│   └── script.js
│   └── avatar.png          # Bot avatar image
│   └── user-avatar.png     # User avatar image
├── generate_embeddings.py  # Script to generate embeddings.
└── README.md               # This file.

## Customization

*   **Knowledge Base (`data.csv`):**  Modify this file to add, remove, or update the questions and answers that the chatbot knows.
*   **NLU Data (`data/nlu.yml`):**  Add more training examples to existing intents, or create new intents to handle different types of questions.
*   **Stories/Rules (`data/stories.yml`, `data/rules.yml`):**  Modify the stories and rules to change the chatbot's conversation flow.
*   **Custom Actions (`actions/actions.py`):** Modify the `action_answer_question` to change how answers are retrieved or formatted.  Add new custom actions for additional functionality.
*   **Frontend (`frontend/`):**  Customize the appearance and behavior of the web interface by modifying the HTML, CSS, and JavaScript files.
* **Configuration(`config.yml`):** Fine tune your model configurations.

## Contributing (Optional)

If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature/fix: `git checkout -b feature/your-feature-name`
3.  Make your changes and commit them with clear, descriptive commit messages.
4.  Push your branch to your fork: `git push origin feature/your-feature-name`
5.  Create a pull request to the `main` branch of the original repository.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.  (You'll need to *create* a `LICENSE` file and choose a license.  MIT is a good, permissive open-source license.)
