DB_DOC_ID_KEY = "db_document_id"

SYSTEM_MESSAGE = """
Answer the question as truthfully as possible using the provided documents, and if the answer is not contained within the provided documents, say "I don't know".
Here are the rules that you must follow:
* For questions, you must look into provided documents to find the answer and then write a response.
""".strip()

NODE_PARSER_CHUNK_SIZE = 512
NODE_PARSER_CHUNK_OVERLAP = 10
