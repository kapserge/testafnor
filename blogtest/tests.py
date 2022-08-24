from django.test import TestCase, Client, RequestFactory

# Create your tests here.
import pytest

from django.urls import reverse
from rest_framework import status
from .models import Obfuscated
from .serializers import ObfuscatedSerializer

client = Client()
class GetAllObfTest(TestCase):
	def setUp(self):
		self.test = Obfuscated.objects.create(NUMDOS ='NUMDOS',NUMDOSVERLING ='NUMDOSVERLING',ANCART='ANCART',FILIERE='FILIERE',ETAPE='ETAPE',VERLING='VERLING',FORMAT='FORMAT')

	def test_get_all_puppies(self):
		response = client.get(reverse('obf_list'))
		obf = Obfuscated.objects.all()
		serializer = ObfuscatedSerializer(obf, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_single_puppy(self):
		response = client.get(
            reverse('get_single', kwargs={'pk': self.test.pk}))
		obf = Obfuscated.objects.get(pk=self.test.pk)
		serializer = ObfuscatedSerializer(obf)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
        