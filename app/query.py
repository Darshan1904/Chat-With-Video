from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

transcript = """Illegitimate access detection systems in hospital logs perform post hoc detection instead of runtime access restriction to allow widespread access in emergencies. We study the effectiveness of adversarial machine learning strategies against such detection systems on a large-scale dataset consisting of a year of access logs at a major hospital. We study a range of
graph-based anomaly detection systems, including heuristicbased and Graph Neural Network (GNN)-based models. We
find that evasion attacks, in which covering accesses (that is,
accesses made to disguise a target access) are injected during
evaluation period of the target access, can successfully fool
the detection system. We also show that such evasion attacks
can transfer among different detection algorithms. On the
other hand, we find that poisoning attacks, in which adversaries inject covering accesses during the training phase of
the model, do not effectively mislead the trained detection
system unless the attacker is given unrealistic capabilities
such as injecting over 10,000 accesses or imposing a high
weight on the covering accesses in the training algorithm.
To examine the generalizability of the results, we also apply
our attack against a state-of-the-art detection model on the
LANL network lateral movement dataset, and observe similar
conclusions."""

# Initialize the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
# Generate embeddings for the transcript
transcript_embeddings = embeddings.embed_documents([transcript])

# Initialize the FAISS vector store with the embeddings
vectorDB = FAISS.from_texts([transcript], embeddings)

# Retrieve the retriever from the vector store
retriever = vectorDB.as_retriever()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0
)

# Create a Q&A chain
QA_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Invoke the Q&A chain and get a response for user query
query = "suggest a topic for this text"

response = QA_chain.invoke({"query": query})

# Print the response
print(response["result"])