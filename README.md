# 🚀 Bionova Project

This project was created for the **GreenTech Hackathon** organized by **Tekno-Family**. It is a local-hosted **RAG (Retrieval-Augmented Generation)** system that combines retrieval and generation methods. The application leverages a **Large Language Model (LLM)** to respond exclusively to specific data retrieved from a **vector database (ChromaDB)**, ensuring accurate and context-aware responses.

## 📥 Installation

Get started in no time by following these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/omagomadov/bionova
    cd bionova-project
    ```

2. **Set up a virtual environment** (recommended):
    ```bash
    # On MacOS
    source venv/bin/activate  
    # On Windows 
    venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run make**:
    ```bash
    make
    ```

5. **Download the required LLM**:
    Use [Ollama](https://ollama.com) to download the necessary language model. For this project, it is recommended to use the **Mistral** model:
    ```bash
    ollama pull mistral
    ```

6. **Start the Ollama service**:
    Launch the Ollama service by running:
    ```bash
    ollama serv
    ```

7. **Launch the application**:  
    Run the following command to start the app on your localhost:
    ```bash
    streamlit run app.py
    ```
    Open your browser and navigate to the provided URL to access the application.

## 🌳 Project Structure

Below is the directory structure of the project:

    ```
    bionova-project/
    ├── CSVs
    │   └── data.csv
    ├── Makefile
    ├── README.md
    ├── app.py
    ├── load_data.py
    └── requirements.txt
    ```


