# -*-coding:Utf-8 -*
import os

class DictionnaireOrdonne:
	"""Notre dictionnaire ordonn�. L'ordre des donn�es est maintenu
	et il peut donc, contrairement aux dictionnaires usuels �tre tri�
	ou voir l'ordre de ses donn�es invers�es."""
	
	def __init__(self, base = {}, **donnees):
		"""Constructeur de notre objet. Il peut ne prendre aucun param�tre
		(dans ce cas le dictionnaire sera vide) ou contruire un 
		dictionnaire remplis gr�ce :
		- au dictionnaire 'base' pass� en premier param�tre
		- aux valeurs que l'on retrouve dans 'donnees' """
		
		self._cles = [] # liste contenant nos cl�s
		self._valeurs = [] # Liste contenant les valeurs correspondant � nos cl�s
		
		# On v�rifie que 'base' est un dictionnaire exploitable
		if type(base) not in(dict, DictionnaireOrdonne):
			raise TypeError ( \
				"Le type attendu est un dictionnaire(usuel ou ordonn�)")
				
		# On r�cup�re les donn�es de base
		for cle in base:
			self[cle] = base[cle]
			
		# On r�cup�re les donn�es de 'donnees'
		for cle in donnees:
			self[cle] = donnees[cle]
			
	def __repr__(self):
		"""Repr�sentation de notre objet. C'est cette cha�ne qui sera affich�e 
		quand on saisit directement le dictionnaire dans l'interpr�teur, ou en
		utilisant la fonction 'rep' """
		
		chaine = "{"
		premier_passage = True
		for cle, valeur in self.items():
			if not premier_passage:
				chaine += ", " # On ajoute la virgule comme s�parateur
			else:
				premier_passage = False
			chaine += repr(cle) + ": " + repr(valeur)
		chaine += "}"
		return chaine
		
	def __str__(self):
		"""Fonction appel�e quand on souhaite afficher le dictionnaire gr�ce
		� la fonction 'print' ou le convertir en cha�ne gr�ce au constructeur
		'str'. On redirige sur __repr__"""
		
		return repr(self)
		
	def __len__self():
		# Renvoie la taille du dictionnaire
		return len(self._cles)
		
	def __contains__(self, cle):
		"""Renvoie True si la cl� est dans la liste des cl�s, False sinon"""
		return cle in self._cles
		
	def __getitem__(self, cle):
		"""Renvoie la valeur correspondant � la cl� si elle existe,
		l�ve une exception KeyError sinon"""
		
		if cle not in self._cles:
			raise KeyError( \
				"La cl� {0} ne se trouve pas dans le dictionnaire".format( \
				cle))
				
		else:
			indice = self._cles.index(cle)
			return self._valeurs[indice]
	def __setitem__(self, cle, valeur):
		"""M�thode sp�ciale quand on cherche � modifier une cl�
		pr�sente dans le dictionnaire. Si la cl� n'est pas pr�sente, on l'ajoute
		� la fin du dictionnaire"""
		
		if cle in self._cles:
			indice = self._cles.index(cle)
			self._valeurs[indice] = valeur
		else:
			self._cles.append(cle)
			self._valeurs.append(valeur)
			
	def __delitem__(self, cle):
		"""M�thode appel�e quand on souhaite supprimer une cl�"""
		if cle not in self._cles:
			raise KeyError( \
				"La cl� {0} ne se trouve pas dans le dictionnaire".format( \
				cle))
		else:
			indice = self._cles.index(cle)
			del self._cles[indice]
			del self._valeurs[indice]
			
	def __iter__(self):
		"""M�thode de parcours de l'objet. On renvoie l'it�rateur des cl�s"""
		return iter(self._cles)
		
	def __add__(self, autre_objet):
		"""On renvoie un dictionnaire contenant les deux
		dictionnaires, mis bout � bout (d'abord self puis autre_objet)"""
		if type(autre_objet) is not type(self):
			raise TypeError( \
				"Impossible de concat�ner {0} et {1}".format( \
				type(self), type(autre_objet)))
		else:
			nouveau = DictionnaireOrdonne()
			
			# On commence par copier self dans le dictionnaire
			for cle, valeur in self.items():
				nouveau[cle] = valeur
				
			# On copie ensuite autre_objet
			for cle, valeur in autre_objet.items():
				nouveau[cle] = valeur
				return nouveau
				
	def items(self):
		"""Renvoie un g�n�rateur contenant les couples (cle, valeur)"""
		for i, cle in enumerate(self._cles):
			valeur = self._valeurs[i]
			yield (cle, valeur)
			
	def keys(self):
		"""Cette m�thode renvoie la liste des cl�s"""
		return list(self._cles)
		
	def values(self):
		"""Cette m�thode renvoie la liste des valeurs"""
		return list(self._valeurs)
		
	def reverse(self):
		"""Inversion du dictionnaire"""
		# On cr�e deux listes vides qui contiennent le nouvel ordre des cl�s
		# et valeurs
		cles = []
		valeurs = []
		for cle, valeur in self.items():
			# On ajoute les cl�s et valeurs au d�but de la liste
			cles.insert(0, cle)
			valeurs.insert(0, valeur)
		# On met ensuite � jour nos listes
		self._cles = cles
		self._valeurs = valeurs
		
	def sort(self):
		"""M�thode premettant de trier le dictionnaire en fonction de ses cl�s"""
		# On trie les cl�s
		cles_triees = sorted(self._cles)
		# on cr�e une liste de valeurs encore vide
		valeurs = []
		# On parcours ensuite la liste des cl�s tri�es
		for cle in cles_triees:
			valeur = self[cle]
			valeurs.append(valeur)
		# Enfin, on met � jour notre liste de cl�s et de valeurs
		self._cles = cles_triees
		self._valeurs = valeurs
		
# On met en pause le syst�me (Windows)
os.system("pause")
	