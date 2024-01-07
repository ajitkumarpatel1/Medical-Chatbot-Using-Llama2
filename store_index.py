from src.helper import load_pdf, text_split, download_hugging_face_embeddings  # Importing the local package 
from langchain.vectorstores import Pinecone                                    # Vector DB Vectore store
import pinecone                                                                # vector DB
from dotenv import load_dotenv                                                 # accesing .env file attribute
import os                                                                      # Operating system attribute for load_dotenv library

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

# Load the pdf in 'extracted_data'
extracted_data = load_pdf("data/")

# Split the data into chunks 
text_chunks = text_split(extracted_data)

# Dawnlode the embadings
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

index_name="medical-boat"   # name prent in pine cone

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)