from django.db import models


class Obfuscated (models.Model):

	NUMDOS = models.CharField( max_length=255)
	NUMDOSVERLING = models.CharField( max_length=255)
	ANCART = models.CharField( max_length=255)
	FILIERE = models.CharField( max_length=255)
	ETAPE = models.CharField( max_length=255)
	VERLING = models.CharField( max_length=255)
	FORMAT = models.CharField( max_length=255)
        


