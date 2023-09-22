from ABC import abc, abstractmethod

class ResultInterface(abc):
	@abstractmethod
	def get_id_tagged_content(self) -> dict:
		raise NotImplementedError	    

	@abstractmethod
	def get_terms(self) -> dict:
		raise NotImplementedError
		      
