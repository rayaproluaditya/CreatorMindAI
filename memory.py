import chromadb

client = chromadb.Client()

collection = client.create_collection("content")

def save_data(data):

    collection.add(
        documents=[data],
        ids=["id"+str(len(data))]
    )
