import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Limpa as listas globais antes de cada teste
        from app import times, campeonatos
        times.clear()
        campeonatos.clear()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), " Seja bem vindo!!!")

    def test_get_times_empty(self):
        response = self.app.get('/times')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    def test_post_time(self):
        time_data = {"nome": "Flamengo", "estado": "RJ"}
        response = self.app.post('/times',
                               data=json.dumps(time_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Time adicionado com sucesso!'})

    def test_get_times_after_post(self):
        time_data = {"nome": "Flamengo", "estado": "RJ"}
        self.app.post('/times',
                     data=json.dumps(time_data),
                     content_type='application/json')
        response = self.app.get('/times')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 1)

    def test_get_campeonatos_empty(self):
        response = self.app.get('/campeonatos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    def test_post_campeonato(self):
        campeonato_data = {"nome": "Brasileirão", "ano": 2024}
        response = self.app.post('/campeonatos',
                               data=json.dumps(campeonato_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Campeonato adicionado com sucesso!'})

    def test_get_campeonatos_after_post(self):
        campeonato_data = {"nome": "Brasileirão", "ano": 2024}
        self.app.post('/campeonatos',
                     data=json.dumps(campeonato_data),
                     content_type='application/json')
        response = self.app.get('/campeonatos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 1)
        self.assertEqual(json.loads(response.data)[0], campeonato_data)

    def test_page_not_found(self):
        response = self.app.get('/rota_inexistente')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {'error': 'Pagina nao encontrada!'})

if __name__ == '__main__':
    unittest.main()
