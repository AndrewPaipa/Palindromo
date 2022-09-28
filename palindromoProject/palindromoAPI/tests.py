from django.test import SimpleTestCase, Client
from django.http import JsonResponse

# Create your tests here.
class UsuarioTestCase(SimpleTestCase):
    
    def setUp(self):                  #Condiciones de inicio
        self.client = Client()

    #teste a ''

    def test_index_get(self):
        response = self.client.get('')
        print(response)

    def test_index_post(self):
        response = self.client.post('')
        print(response)
        
    def test_index_put(self):
        response = self.client.put('')
        print(response)

    def test_index_delete(self):
        response = self.client.delete('')
        print(response)
        

    #teste a '/palindromo/'

    def test_palindromo_get(self):
        response = self.client.get('/palindromo/')
        print(response)

    def test_palindromo_post(self):
        response = self.client.post('/palindromo/', {'expression':'ojozajaxee'})
        print(response)
        
    def test_palindromo_put(self):
        response = self.client.put('/palindromo/')
        print(response)

    def test_palindromo_delete(self):
        response = self.client.delete('/palindromo/')
        print(response)