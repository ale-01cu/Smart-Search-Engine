from .pln import PLN

class Query:
	query: str
	text_procesor: PLN

	def __init__(self, query: str) -> None:
		self.query = query
		self.text_procesor = PLN()

	@property	
	def query_terms(self) -> dict:
		return self.text_procesor.get_processed_terms(query)

	@property
	def query_terms_joined(self) -> str:
		return " ".join(self.query_terms.items())