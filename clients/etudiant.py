from src.modules import Etudiant

class EtudiantModel(Etudiant):
	"""
	\# name <string>
	"""
	def __init__(self):
		self.name = None

	def save(self):
		if self.name == None:
			return 'Please entry good name before save data'
		self.add(name=self.name)
		return 'operation success !'

	def put(self):
		pass

	def get(self):
		return self.find()

	def delete(self):
		pass