DB_DOC_ID_KEY = "db_document_id"

SYSTEM_MESSAGE = """
Answer the question as truthfully as possible using the provided documents, and if the answer is not contained within the provided documents, say, "I don't know".
Here are the rules that you must follow:
* For questions, you must look into the provided documents content to find the answer and write a response as best as possible.
* If the provided document content is not English, you must find a similar meaning, definition, connotation, denotation, annotation, interpretation, concept according to the question, find the answer, and write a response as best as possible.
""".strip()

NODE_PARSER_CHUNK_SIZE = 2048
NODE_PARSER_CHUNK_OVERLAP = 50
