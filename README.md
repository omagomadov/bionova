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

4. **Download the required LLM**:
    Use [Ollama](https://ollama.com) to download the necessary language model. For this project, it is recommended to use the **Mistral** model:
    ```bash
    ollama pull mistral
    ```

5. **Start the Ollama service**:
    Launch the Ollama service by running:
    ```bash
    ollama serv
    ```

6. **Launch the application**:  
    Run the following command to start the app on your localhost:
    ```bash
    streamlit run app.py
    ```
    Open your browser and navigate to the provided URL to access the application.

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software as long as proper attribution is given. See the [LICENSE](LICENSE) file for more details.


