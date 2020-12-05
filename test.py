#File to permit has use model test

from clients.etudiant import EtudiantModel

etd = EtudiantModel()
etd.name = 'koffi bruce'
etd.save()
print(etd.get())
