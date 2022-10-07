from unittest import result
import snakes_ladders
import unittest

"""
    Autores: Kevin Ocampo 

    Fecha: 10/7/2022

    Descripción: Este archivo contiene las pruebas realizadas al juego 'Serpientes y Escaleras' con Unittest.

    Version: 1.0
"""

#Probando que el juego finalice con un tablero de tamaño 5
class test1(unittest.TestCase):
    def setUp(self):
        self.n = 5

    def test(self):
        result = snakes_ladders.game(self.n)
        self.assertEqual(result,"Fin")

    def tearDown(self):
        self.assertGreaterEqual(snakes_ladders.value,self.n*self.n)

#Probando que el juego lance error cuando se envia un valor diferente de int
class test2(unittest.TestCase):
    def setUp(self):
        self.n = "Hola"

    def test(self):
        with self.assertRaises(AssertionError):
            result = snakes_ladders.game(self.n)

#Probando que el juego lance error cuando se envia un valor entero negativo
class test3(unittest.TestCase):
    def setUp(self):
        self.n = -1

    def test(self):
        with self.assertRaises(AssertionError):
            result = snakes_ladders.game(self.n)

#Probando que el mensaje y valor devuelto para una casilla cualquiera (no hay serpiente ni escalera) es el correcto
class test4(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.val = 5
        snakes_ladders.snake = {14:4 , 19:8, 22:20, 24:16}
        snakes_ladders.ladders = {3:11, 10:12, 9:18, 6:17}
    
    def test(self):
        result = snakes_ladders.state(self.n,self.val)
        self.assertEqual(result[0],"Jugador avanza a cuadro")

    def tearDown(self):
        self.assertEqual(snakes_ladders.aux,self.val)
    
#Probando que el mensaje y valor devuelto para una casilla con serpiente es el correcto
class test5(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.val = 14
        self.down = 4
        snakes_ladders.snake = {14:4 , 19:8, 22:20, 24:16}
        snakes_ladders.ladders = {3:11, 10:12, 9:18, 6:17}
    
    def test(self):
        result = snakes_ladders.state(self.n,self.val)
        self.assertEqual(result[0],"Jugador desciende al cuadro")

    def tearDown(self):
        self.assertEqual(snakes_ladders.aux,self.down)

#Probando que el mensaje y valor devuelto para una casilla con escalera es el correcto
class test6(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.val = 3
        self.up = 11
        snakes_ladders.snake = {14:4 , 19:8, 22:20, 24:16}
        snakes_ladders.ladders = {3:11, 10:12, 9:18, 6:17}
    
    def test(self):
        result = snakes_ladders.state(self.n,self.val)
        self.assertEqual(result[0],"Jugador sube por la escalera al cuadro")

    def tearDown(self):
        self.assertEqual(snakes_ladders.aux,self.up)

#Probando con un valor no valido de casilla
class test7(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.val = -3
        snakes_ladders.snake = {14:4 , 19:8, 22:20, 24:16}
        snakes_ladders.ladders = {3:11, 10:12, 9:18, 6:17}
    
    def test(self):
        with self.assertRaises(AssertionError):
            result = snakes_ladders.state(self.n,self.val)

#Probando con un valor de tipo diferente
class test8(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.val = []
        snakes_ladders.snake = {14:4 , 19:8, 22:20, 24:16}
        snakes_ladders.ladders = {3:11, 10:12, 9:18, 6:17}
    
    def test(self):
        with self.assertRaises(AssertionError):
            result = snakes_ladders.state(self.n,self.val)
        