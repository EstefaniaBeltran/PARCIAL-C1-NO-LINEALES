
# REAMDE Parcial: Estructuras de Datos No Lineales

## Abstract
En el presente trabajo se desarrollará la implementación de quince ejercicios de estructuras de datos no lineales que abordan problemas computacionales importantes. Se tendrán 6 temáticas principales, en los árboles N-arios se modeló una jerarquía universitaria, un sistema de archivos con búsqueda y eliminación recursiva, un árbol genealógico con cálculo de generaciones, un menú jerárquico de aplicación y un sistema de dependencias de software con análisis de impacto. Para los árboles Trie se implementó autocompletado con generador de sugerencias, un corrector ortográfico basado en diccionario, un clasificador de intenciones mediante árbol de decisión, un diccionario multilenguaje con significados por idioma  y un motor de búsqueda que integra Trie con heap para priorizar resultados por relevancia. Por otro lado en el módulo de tablas hash se desarrolló un registro de estudiantes con manejo de colisiones por encadenamiento y métodos mágicos (setitem y getitem), junto con una comparación experimental de rendimiento frente a los árboles Trie. Finalmente, se implementaron estructuras basadas en heaps: un heap mínimo con operaciones fundamentales, un planificador de tareas con prioridad y time stamp utilizando sobrecarga de lt, y una simulación de red que procesa paquetes según su prioridad. 
Todas las implementaciones cumplen con type hints, docstrings estilo Google y generadores para eficiencia de memoria, demostrando su aplicabilidad en sistemas operativos, bases de datos, redes de telecomunicaciones y motores de búsqueda, donde la elección adecuada de la estructura de datos determina la eficiencia computacional del sistema.

##  Descripción General

Este repositorio contiene la solución completa al parcial de las semanas 5 y 6 de la asignatura **Estructuras de Datos No Lineales**. Se implementan **15 ejercicios** que cubren:

- **Árboles N-arios**: organización universitaria, sistema de archivos, árbol genealógico, menús de aplicación, dependencias de software.
- **Árboles Trie**: autocompletado, corrector ortográfico, clasificador de intenciones, diccionario multilenguaje, motor de búsqueda con priorización.
- **Tablas Hash**: registro de estudiantes con manejo de colisiones, comparación Hash vs Trie.
- **Heaps y Colas de Prioridad**: heap mínimo, planificador de tareas, simulación de red con prioridad de paquetes.

Cada ejercicio cumple con los estándares de la industria: **type hints**, **docstrings estilo Google**, **PEP8** y uso de **generadores** para recorridos eficientes en memoria. Además, se implementan métodos mágicos como `__iter__`, `__setitem__`, `__getitem__` y `__lt__` según lo requerido.


##  Estructura del Proyecto

```bash
├── src/                          # Código fuente de los ejercicios
│   ├── ejercicio01.py            # Estructura Organizacional (Árbol N-ario)
│   ├── ejercicio02.py            # Sistema de Archivos
│   ├── ejercicio03.py            # Árbol Genealógico
│   ├── ejercicio04.py            # Menú de Aplicación
│   ├── ejercicio05.py            # Dependencias de Software
│   ├── ejercicio06.py            # Autocompletado (Trie)
│   ├── ejercicio07.py            # Corrector Ortográfico
│   ├── ejercicio08.py            # Clasificador de Intenciones
│   ├── ejercicio09.py            # Diccionario Multilenguaje (Trie)
│   ├── ejercicio10.py            # Motor de Búsqueda (Trie + Heap)
│   ├── ejercicio11.py            # Registro de Estudiantes (Hash Table)
│   ├── ejercicio12.py            # Comparación Hash vs Trie
│   ├── ejercicio13.py            # Heap Mínimo
│   ├── ejercicio14.py            # Planificador de Tareas
│   └── ejercicio15.py            # Simulación de Red
├── tests/                         # Pruebas unitarias (unittest)
│   └── test_ejercicios.py         # Archivo único con todos los tests
├── README.md                       # Este archivo
├── INFORME                        # Archivo con toda la parte 1 .pdf
```



##  Requerimientos

- Python **3.10** o superior.
- No se requieren librerías externas; todo se implementa con la biblioteca estándar (`heapq`, `typing`, `datetime`, etc.).



##  Ejecución

Cada ejercicio es independiente y puede ejecutarse directamente como script principal:

```bash
python src/ejercicio01.py
python src/ejercicio02.py
...
python src/ejercicio15.py
```

Todos los archivos incluyen un bloque `if __name__ == "__main__":` que ejecuta un ejemplo demostrativo de la funcionalidad implementada.


##  Pruebas Unitarias

Se incluye un archivo de pruebas `test.py` que contiene tests para todos los ejercicios. Para ejecutarlas:

```bash
# Desde la raíz del proyecto
python -m unittest tests/test_ejercicios.py
```

O si se prefiere `pytest` (instalarlo previamente):

```bash
pytest tests/test_ejercicios.py
```

Las pruebas verifican:
- Correcta inserción, búsqueda y eliminación en cada estructura.
- Comportamiento de los métodos mágicos.
- Generación de sugerencias en Tries.
- Ordenamiento por prioridad en heaps.
- Manejo de colisiones en tabla hash.



##  Análisis de Complejidad Big O

### Ejercicios 1–5: Árboles N-arios

| Operación           | Complejidad |
|---------------------|-------------|
| Inserción de hijo   | O(1)*       |
| Recorrido completo  | O(n)        |
| Búsqueda por nombre | O(n)        |
| Eliminación         | O(n)        |

*O(1) usando diccionario para acceso directo por nombre.

### Ejercicios 6–10: Árboles Trie

| Operación               | Complejidad        |
|-------------------------|--------------------|
| Inserción               | O(L) (L = longitud)|
| Búsqueda exacta         | O(L)               |
| Búsqueda por prefijo    | O(L + M) (M = número de sugerencias) |
| Sugerencias (generador) | O(L + M)           |

### Ejercicios 11–12: Tablas Hash

| Operación               | Complejidad promedio | Peor caso    |
|-------------------------|----------------------|--------------|
| Inserción               | O(1)                 | O(n)         |
| Búsqueda                | O(1)                 | O(n)         |
| Eliminación             | O(1)                 | O(n)         |

*El peor caso ocurre cuando muchas colisiones degeneran en listas largas.*

### Ejercicios 13–15: Heaps y Colas de Prioridad

| Operación               | Complejidad |
|-------------------------|-------------|
| Inserción (heappush)    | O(log n)    |
| Extracción (heappop)    | O(log n)    |
| Consulta del mínimo     | O(1)        |



##  Características Implementadas

- **Type Hints** en todas las funciones y métodos.
- **Docstrings estilo Google** (descripción, Args, Returns, Raises cuando corresponde).
- **Generadores** (`yield`) para recorridos de árboles y sugerencias, optimizando memoria.
- **Métodos mágicos**:
  - `__iter__` en árboles y tabla hash.
  - `__setitem__` y `__getitem__` en la tabla hash (Ejercicio 11).
  - `__lt__` en las clases `Tarea` y `Paquete` para ordenamiento en heaps (Ejercicios 14 y 15).
- Manejo de colisiones en tabla hash mediante **encadenamiento**.
- **Comparación experimental** entre Hash y Trie (Ejercicio 12) con medición de tiempos.



