from langchain.document_loaders import PyPDFLoader, DirectoryLoader     # Data injection from (dirctory and pdf)
from langchain.text_splitter import RecursiveCharacterTextSplitter      # Chunk creation from antire Corpus
from langchain.embeddings import HuggingFaceEmbeddings                  # Vector embading creation from text data



#### Loding PDF file from data folder (Data injection)
def load_pdf(data):
    '''Extract data from the PDF'''
     
    loader = DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents = loader.load()
    return documents


#Create text chunks function
def text_split(extracted_data):
    '''Converting the PDF text into chunks'''
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20) 
    text_chunks = text_splitter.split_documents(extracted_data)      # spliting data
    return text_chunks


#download Hugging face embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings