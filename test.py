#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Archivo único de pruebas unitarias para los 15 ejercicios del parcial.
Ejecutar con: python -m unittest tests/test_ejercicios.py
"""

import unittest
import sys
import os
import time
from datetime import datetime

# Agregar la carpeta src al path para poder importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar todos los módulos de ejercicios
import ejercicio01
import ejercicio02
import ejercicio03
import ejercicio04
import ejercicio05
import ejercicio06
import ejercicio07
import ejercicio08
import ejercicio09
import ejercicio10
import ejercicio11
import ejercicio12
import ejercicio13
import ejercicio14
import ejercicio15


# ----------------------------------------------------------------------
# Ejercicio 1: Estructura Organizacional
# ----------------------------------------------------------------------
class TestEjercicio01(unittest.TestCase):
    def test_creacion_nodo(self):
        nodo = ejercicio01.Nodo("Rectoria")
        self.assertEqual(nodo.nombre, "Rectoria")
        self.assertEqual(nodo.hijos, {})

    def test_agregar_hijo(self):
        padre = ejercicio01.Nodo("Padre")
        hijo = ejercicio01.Nodo("Hijo")
        padre.agregar_hijo(hijo)
        self.assertIn("Hijo", padre.hijos)
        self.assertEqual(padre.hijos["Hijo"], hijo)

    def test_recorrido(self):
        raiz = ejercicio01.Nodo("A")
        b = ejercicio01.Nodo("B")
        c = ejercicio01.Nodo("C")
        raiz.agregar_hijo(b)
        raiz.agregar_hijo(c)
        recorrido = list(raiz.recorrer())
        self.assertEqual(recorrido, ["A", "B", "C"])

    def test_ejemplo_universidad(self):
        arbol = ejercicio01.ejemplo_universidad()
        self.assertEqual(arbol.raiz.nombre, "Rectoria")
        self.assertEqual(len(arbol.raiz.hijos), 3)


# ----------------------------------------------------------------------
# Ejercicio 2: Sistema de Archivos
# ----------------------------------------------------------------------
class TestEjercicio02(unittest.TestCase):
    def test_creacion(self):
        nodo = ejercicio02.NodoArchivo("carpeta")
        self.assertEqual(nodo.nombre, "carpeta")
        self.assertEqual(nodo.hijos, {})

    def test_agregar_y_recorrer(self):
        raiz = ejercicio02.NodoArchivo("raiz")
        hijo = ejercicio02.NodoArchivo("hijo")
        raiz.agregar(hijo)
        self.assertIn("hijo", raiz.hijos)
        recorrido = list(raiz.recorrer())
        self.assertEqual(recorrido, ["raiz", "hijo"])

    def test_buscar(self):
        raiz = ejercicio02.NodoArchivo("raiz")
        docs = ejercicio02.NodoArchivo("docs")
        archivo = ejercicio02.NodoArchivo("nota.txt")
        docs.agregar(archivo)
        raiz.agregar(docs)
        encontrado = raiz.buscar("nota.txt")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "nota.txt")
        self.assertIsNone(raiz.buscar("noexiste"))

    def test_eliminar(self):
        raiz = ejercicio02.NodoArchivo("raiz")
        hijo = ejercicio02.NodoArchivo("hijo")
        raiz.agregar(hijo)
        self.assertTrue(raiz.eliminar("hijo"))
        self.assertNotIn("hijo", raiz.hijos)
        self.assertFalse(raiz.eliminar("hijo"))

    def test_ejemplo(self):
        sistema = ejercicio02.ejemplo_sistema_archivos()
        self.assertEqual(sistema.raiz.nombre, "sistema_archivos")
        self.assertEqual(len(sistema.raiz.hijos), 2)


# ----------------------------------------------------------------------
# Ejercicio 3: Árbol Genealógico
# ----------------------------------------------------------------------
class TestEjercicio03(unittest.TestCase):
    def test_creacion(self):
        p = ejercicio03.Persona("Juan")
        self.assertEqual(p.nombre, "Juan")
        self.assertEqual(p.hijos, {})

    def test_agregar_hijo(self):
        padre = ejercicio03.Persona("Padre")
        hijo = ejercicio03.Persona("Hijo")
        padre.agregar_hijo(hijo)
        self.assertIn("Hijo", padre.hijos)

    def test_recorrido(self):
        abuelo = ejercicio03.Persona("Abuelo")
        hijo = ejercicio03.Persona("Hijo")
        nieto = ejercicio03.Persona("Nieto")
        hijo.agregar_hijo(nieto)
        abuelo.agregar_hijo(hijo)
        recorrido = list(abuelo.recorrer())
        self.assertEqual(recorrido, ["Abuelo", "Hijo", "Nieto"])

    def test_generaciones(self):
        abuelo = ejercicio03.Persona("Abuelo")
        hijo = ejercicio03.Persona("Hijo")
        nieto = ejercicio03.Persona("Nieto")
        hijo.agregar_hijo(nieto)
        abuelo.agregar_hijo(hijo)
        self.assertEqual(abuelo.generaciones(), 3)
        self.assertEqual(hijo.generaciones(), 2)
        self.assertEqual(nieto.generaciones(), 1)

    def test_ejemplo(self):
        arbol = ejercicio03.ejemplo_familia()
        self.assertEqual(arbol.raiz.nombre, "Abuelo")
        self.assertEqual(arbol.altura(), 3)


# ----------------------------------------------------------------------
# Ejercicio 4: Menú de Aplicación
# ----------------------------------------------------------------------
class TestEjercicio04(unittest.TestCase):
    def test_creacion(self):
        nodo = ejercicio04.NodoMenu("Archivo")
        self.assertEqual(nodo.opcion, "Archivo")
        self.assertEqual(nodo.submenus, {})

    def test_agregar(self):
        principal = ejercicio04.NodoMenu("Principal")
        sub = ejercicio04.NodoMenu("Sub")
        principal.agregar(sub)
        self.assertIn("Sub", principal.submenus)

    def test_recorrido(self):
        raiz = ejercicio04.NodoMenu("Raiz")
        h1 = ejercicio04.NodoMenu("H1")
        h2 = ejercicio04.NodoMenu("H2")
        raiz.agregar(h1)
        raiz.agregar(h2)
        recorrido = list(raiz.recorrer())
        self.assertEqual(recorrido, ["Raiz", "  H1", "  H2"])

    def test_contar_niveles(self):
        raiz = ejercicio04.NodoMenu("Raiz")
        h1 = ejercicio04.NodoMenu("H1")
        h2 = ejercicio04.NodoMenu("H2")
        h1.agregar(ejercicio04.NodoMenu("H1.1"))
        raiz.agregar(h1)
        raiz.agregar(h2)
        contador = {}
        raiz.contar_por_nivel(0, contador)
        self.assertEqual(contador, {0: 1, 1: 2, 2: 1})

    def test_ejemplo(self):
        menu = ejercicio04.ejemplo_menu()
        self.assertEqual(menu.raiz.opcion, "Menú Principal")
        self.assertEqual(len(menu.raiz.submenus), 2)


# ----------------------------------------------------------------------
# Ejercicio 5: Dependencias de Software
# ----------------------------------------------------------------------
class TestEjercicio05(unittest.TestCase):
    def test_creacion(self):
        m = ejercicio05.Modulo("A")
        self.assertEqual(m.nombre, "A")
        self.assertEqual(m.dependencias, {})

    def test_agregar_dependencia(self):
        a = ejercicio05.Modulo("A")
        b = ejercicio05.Modulo("B")
        a.agregar_dependencia(b)
        self.assertIn("B", a.dependencias)

    def test_obtener_todas_dependencias(self):
        a = ejercicio05.Modulo("A")
        b = ejercicio05.Modulo("B")
        c = ejercicio05.Modulo("C")
        b.agregar_dependencia(c)
        a.agregar_dependencia(b)
        deps = a.obtener_todas_dependencias()
        self.assertEqual(deps, {"A", "B", "C"})

    def test_ejemplo(self):
        sistema = ejercicio05.ejemplo_dependencias()
        self.assertEqual(sistema.raiz.nombre, "Sistema")
        self.assertEqual(len(sistema.raiz.dependencias), 2)


# ----------------------------------------------------------------------
# Ejercicio 6: Autocompletado (Trie)
# ----------------------------------------------------------------------
class TestEjercicio06(unittest.TestCase):
    def setUp(self):
        self.trie = ejercicio06.Trie()
        self.trie.insertar("casa")
        self.trie.insertar("carro")
        self.trie.insertar("carta")

    def test_buscar(self):
        self.assertTrue(self.trie.buscar("casa"))
        self.assertTrue(self.trie.buscar("carro"))
        self.assertTrue(self.trie.buscar("carta"))
        self.assertFalse(self.trie.buscar("cas"))
        self.assertFalse(self.trie.buscar("perro"))

    def test_sugerir(self):
        sugerencias = list(self.trie.sugerir("ca"))
        self.assertCountEqual(sugerencias, ["casa", "carro", "carta"])
        self.assertEqual(list(self.trie.sugerir("car")), ["carro", "carta"])
        self.assertEqual(list(self.trie.sugerir("xyz")), [])

    def test_ejemplo(self):
        try:
            ejercicio06.ejemplo_trie()
        except Exception as e:
            self.fail(f"ejemplo_trie lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 7: Corrector Ortográfico
# ----------------------------------------------------------------------
class TestEjercicio07(unittest.TestCase):
    def setUp(self):
        self.trie = ejercicio07.Trie()
        self.corrector = ejercicio07.CorrectorOrtografico(self.trie)
        self.palabras = ["hola", "mundo", "python"]
        self.corrector.cargar_palabras(self.palabras)

    def test_verificar(self):
        self.assertTrue(self.corrector.verificar("hola"))
        self.assertTrue(self.corrector.verificar("mundo"))
        self.assertTrue(self.corrector.verificar("python"))
        self.assertFalse(self.corrector.verificar("java"))
        self.assertFalse(self.corrector.verificar("hol"))

    def test_ejemplo(self):
        try:
            ejercicio07.ejemplo_corrector()
        except Exception as e:
            self.fail(f"ejemplo_corrector lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 8: Clasificador de Intenciones
# ----------------------------------------------------------------------
class TestEjercicio08(unittest.TestCase):
    def test_creacion(self):
        nodo = ejercicio08.NodoDecision("¿Pregunta?")
        self.assertEqual(nodo.pregunta, "¿Pregunta?")
        self.assertEqual(nodo.opciones, {})

    def test_decidir(self):
        nodo = ejercicio08.NodoDecision("¿Color?", {"rojo": "manzana", "verde": "pera"})
        self.assertEqual(nodo.decidir("rojo"), "manzana")
        self.assertIsNone(nodo.decidir("azul"))

    def test_evaluar(self):
        raiz = ejercicio08.NodoDecision("¿Llueve?")
        si = ejercicio08.NodoDecision("Llevar paraguas", {"si": "salir con paraguas"})
        no = ejercicio08.NodoDecision("No llevar paraguas", {"no": "salir sin paraguas"})
        raiz.opciones["si"] = si
        raiz.opciones["no"] = no
        arbol = ejercicio08.ArbolDecision(raiz)

        respuestas = {"¿Llueve?": "si", "Llevar paraguas": "si"}
        resultado = arbol.evaluar(respuestas)
        self.assertEqual(resultado, "salir con paraguas")

        respuestas2 = {"¿Llueve?": "no"}
        resultado2 = arbol.evaluar(respuestas2)
        self.assertEqual(resultado2, "salir sin paraguas")

    def test_ejemplo(self):
        try:
            ejercicio08.ejemplo_decision()
        except Exception as e:
            self.fail(f"ejemplo_decision lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 9: Diccionario Multilenguaje
# ----------------------------------------------------------------------
class TestEjercicio09(unittest.TestCase):
    def setUp(self):
        self.dic = ejercicio09.DiccionarioMultilenguaje()
        self.dic.insertar("casa", "es", "hogar")
        self.dic.insertar("casa", "en", "house")
        self.dic.insertar("perro", "es", "animal")

    def test_buscar(self):
        self.assertEqual(self.dic.buscar("casa", "es"), "hogar")
        self.assertEqual(self.dic.buscar("casa", "en"), "house")
        self.assertIsNone(self.dic.buscar("casa", "fr"))
        self.assertEqual(self.dic.buscar("casa"), {"es": "hogar", "en": "house"})
        self.assertIsNone(self.dic.buscar("gato"))

    def test_sugerir(self):
        sugerencias = list(self.dic.sugerir("ca"))
        self.assertEqual(sugerencias, ["casa"])
        self.assertEqual(list(self.dic.sugerir("pe")), ["perro"])
        self.assertEqual(list(self.dic.sugerir("zz")), [])

    def test_ejemplo(self):
        try:
            ejercicio09.ejemplo_diccionario()
        except Exception as e:
            self.fail(f"ejemplo_diccionario lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 10: Motor de Búsqueda
# ----------------------------------------------------------------------
class TestEjercicio10(unittest.TestCase):
    def setUp(self):
        self.motor = ejercicio10.MotorBusqueda()
        self.motor.insertar("Ciencia de la Computación", 10)
        self.motor.insertar("Ciencias de la Educación", 5)
        self.motor.insertar("Ciencia de Datos", 8)

    def test_buscar(self):
        self.assertTrue(self.motor.buscar("Ciencia de Datos"))
        self.assertFalse(self.motor.buscar("Matemáticas"))

    def test_sugerir_orden(self):
        sugerencias = list(self.motor.sugerir("Ciencia"))
        self.assertEqual(len(sugerencias), 3)
        self.assertEqual(sugerencias[0][0], 10)
        self.assertEqual(sugerencias[0][1], "Ciencia de la Computación")
        self.assertEqual(sugerencias[1][0], 8)
        self.assertEqual(sugerencias[2][0], 5)

    def test_incrementar_relevancia(self):
        self.motor.incrementar_relevancia("Ciencia de Datos")
        sugerencias = list(self.motor.sugerir("Ciencia"))
        self.assertEqual(sugerencias[1][0], 9)

    def test_ejemplo(self):
        try:
            ejercicio10.ejemplo_motor()
        except Exception as e:
            self.fail(f"ejemplo_motor lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 11: Registro de Estudiantes (Hash Table)
# ----------------------------------------------------------------------
class TestEjercicio11(unittest.TestCase):
    def setUp(self):
        self.tabla = ejercicio11.HashTable(size=5)

    def test_set_get(self):
        self.tabla[101] = "Ana"
        self.assertEqual(self.tabla[101], "Ana")
        with self.assertRaises(KeyError):
            _ = self.tabla[999]

    def test_get_method(self):
        self.tabla[102] = "Luis"
        self.assertEqual(self.tabla.get(102), "Luis")
        self.assertIsNone(self.tabla.get(103))

    def test_actualizar(self):
        self.tabla[101] = "Ana"
        self.tabla[101] = "Ana María"
        self.assertEqual(self.tabla[101], "Ana María")

    def test_eliminar(self):
        self.tabla[101] = "Ana"
        del self.tabla[101]
        with self.assertRaises(KeyError):
            _ = self.tabla[101]

    def test_iteracion(self):
        datos = [(101, "Ana"), (102, "Luis"), (103, "Carlos")]
        for k, v in datos:
            self.tabla[k] = v
        recuperados = list(self.tabla)
        self.assertCountEqual(recuperados, datos)

    def test_factor_carga(self):
        self.assertEqual(self.tabla.factor_carga(), 0.0)
        self.tabla[1] = "A"
        self.tabla[2] = "B"
        self.assertAlmostEqual(self.tabla.factor_carga(), 0.4)
        self.tabla[3] = "C"
        self.tabla[4] = "D"
        self.tabla[5] = "E"
        self.assertAlmostEqual(self.tabla.factor_carga(), 1.0)

    def test_ejemplo(self):
        try:
            ejercicio11.ejemplo_hash()
        except Exception as e:
            self.fail(f"ejemplo_hash lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 12: Comparación Hash vs Trie
# ----------------------------------------------------------------------
class TestEjercicio12(unittest.TestCase):
    def test_hash_insert_search(self):
        ht = ejercicio12.HashTableStr(size=10)
        ht.insert("hola")
        self.assertTrue(ht.search("hola"))
        self.assertFalse(ht.search("mundo"))

    def test_trie_insert_search(self):
        trie = ejercicio12.Trie()
        trie.insert("hola")
        self.assertTrue(trie.search("hola"))
        self.assertFalse(trie.search("mundo"))

    def test_comparar_ejecuta(self):
        try:
            ejercicio12.comparar()
        except Exception as e:
            self.fail(f"comparar lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 13: Heap Mínimo
# ----------------------------------------------------------------------
class TestEjercicio13(unittest.TestCase):
    def setUp(self):
        self.heap = ejercicio13.MinHeap()

    def test_insert_peek(self):
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 3)

    def test_extract_min(self):
        valores = [5, 3, 7, 1, 4]
        for v in valores:
            self.heap.insert(v)
        extraidos = []
        while self.heap:
            extraidos.append(self.heap.extract_min())
        self.assertEqual(extraidos, sorted(valores))

    def test_empty_extract(self):
        with self.assertRaises(IndexError):
            self.heap.extract_min()

    def test_iter(self):
        valores = [4, 2, 6]
        for v in valores:
            self.heap.insert(v)
        self.assertCountEqual(list(self.heap), valores)

    def test_probar_heap(self):
        try:
            ejercicio13.probar_heap()
        except Exception as e:
            self.fail(f"probar_heap lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 14: Planificador de Tareas
# ----------------------------------------------------------------------
class TestEjercicio14(unittest.TestCase):
    def test_tarea_lt_prioridad(self):
        t1 = ejercicio14.Tarea(1, "Alta")
        t2 = ejercicio14.Tarea(2, "Baja")
        self.assertTrue(t1 < t2)
        self.assertFalse(t2 < t1)

    def test_tarea_lt_timestamp(self):
        t1 = ejercicio14.Tarea(1, "A")
        time.sleep(0.01)
        t2 = ejercicio14.Tarea(1, "B")
        self.assertTrue(t1 < t2)

    def test_planificador(self):
        p = ejercicio14.Planificador()
        t1 = ejercicio14.Tarea(2, "T2")
        t2 = ejercicio14.Tarea(1, "T1")
        p.agregar_tarea(t1)
        p.agregar_tarea(t2)
        self.assertEqual(len(p), 2)
        self.assertEqual(p.ejecutar_tarea(), t2)

    def test_ejemplo(self):
        try:
            ejercicio14.ejemplo_planificador()
        except Exception as e:
            self.fail(f"ejemplo_planificador lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejercicio 15: Simulación de Red
# ----------------------------------------------------------------------
class TestEjercicio15(unittest.TestCase):
    def test_paquete_lt(self):
        p1 = ejercicio15.Paquete(1, "Video")
        p2 = ejercicio15.Paquete(2, "Correo")
        self.assertTrue(p1 < p2)
        self.assertFalse(p2 < p1)

    def test_paquete_lt_timestamp(self):
        p1 = ejercicio15.Paquete(1, "A")
        time.sleep(0.01)
        p2 = ejercicio15.Paquete(1, "B")
        self.assertTrue(p1 < p2)

    def test_red(self):
        red = ejercicio15.Red()
        p1 = ejercicio15.Paquete(2, "Mensaje")
        p2 = ejercicio15.Paquete(1, "Video")
        red.enviar_paquete(p1)
        red.enviar_paquete(p2)
        self.assertEqual(red.paquetes_pendientes(), 2)
        self.assertEqual(red.procesar_paquete(), p2)

    def test_ejemplo(self):
        try:
            ejercicio15.ejemplo_red()
        except Exception as e:
            self.fail(f"ejemplo_red lanzó excepción: {e}")


# ----------------------------------------------------------------------
# Ejecutar todas las pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()