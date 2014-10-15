from django.db import models
import re

RE_CEDEX = re.compile(r'(.*)\b\s*cedex.*$' , re.IGNORECASE|re.MULTILINE)
class Entreprise(models.Model):
	nom = models.CharField(max_length=100)
	adresse = models.CharField(max_length=250)
	codePostal= models.CharField(max_length=10)
	ville = models.CharField(max_length=50)
	pays = models.CharField(max_length=30)
	telephone = models.CharField(max_length=20)
	latitude = models.DecimalField(max_digits=13, decimal_places=10)
	longitude = models.DecimalField(max_digits=13, decimal_places=10)
	
	def __str__(self):
		return self.nom
		
	@property
	def latlng(self):
		retrun[self.latitude,self.longitude]
		
	@latlng.setter
	def latlng(self, x):
		self.latitude, self.longitude = x
		
	@property
	def ville_propre(self):
		v=self.ville
		m=RE_CEDEX.match(v)
		if m:
			v=m.group(1)
		return v		
