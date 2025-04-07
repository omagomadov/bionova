from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader, CSVLoader, PyPDFLoader

from dotenv import load_dotenv

load_dotenv()

urls = [""]

def WebsiteLoader(urls):
    loader = WebBaseLoader(urls)
    return loader.load()

def CSVFileLoader(file_paths):
    docs = []
    for file_path in file_paths:
        loader = CSVLoader(file_path=file_path)  # Load each CSV file individually
        docs.extend(loader.load())  # Append loaded data to the list
    return docs

def PDFLoader(pdf_files):
    docs = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(file_path=pdf_file)  # Load each PDF file individually
        docs.extend(loader.load())  # Append loaded data to the list
    return docs

# Uncomment if website scraping is done.
# url_list = WebsiteLoader(urls)

# Uncomment if CSV is used.
url_list = CSVFileLoader(file_paths=["CSVs/data.csv"])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)

# Combine all loaded documents
all_documents = url_list

splited_documents = text_splitter.split_documents(all_documents)
print(splited_documents)


embeddings  = OllamaEmbeddings(
  model='nomic-embed-text'
)
persist_directory = "./chroma_db"

vectorstore = Chroma.from_documents(
    documents=splited_documents,  # Ensure splited_documents contains valid data
    embedding=embeddings,
    persist_directory=persist_directory
)

# Step 2: Persist the database
vectorstore.persist()  # ✅ Saves data to disk
print("✅ Data successfully stored in ChromaDB!")
