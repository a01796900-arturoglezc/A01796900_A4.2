# Actividad A4.2 – Pruebas y Calidad de Software

## Información general

Este repositorio contiene la solución de la **Actividad A4.2**, la cual consta de **tres programas desarrollados en Python**, enfocados en el manejo de archivos, control de errores, estructuras de control y cumplimiento del estándar **PEP-8**, verificados con el analizador estático **pylint**.

Todos los programas:

* Se ejecutan desde **línea de comandos**
* Reciben un **archivo de texto como parámetro**
* Manejan **errores sin detener la ejecución**
* Generan **salida en consola y en archivo**
* Incluyen el **tiempo de ejecución**
* Obtienen **calificación 10/10 en pylint**

---

## Requisitos del sistema

Para ejecutar los programas se necesita:

* **Python 3.10 o superior**
* Sistema operativo Windows, macOS o Linux
* Consola / Terminal (PowerShell, CMD o Terminal)
* Paquete `pylint` para verificación

### Instalación de pylint

```bash
pip install pylint
```

---

## Estructura del repositorio

```
A01796900_A4.2/
│
├── Problema 1/
│   ├── computeStatistics.py
│   ├── testCase1.txt
│   ├── ...
│   ├── testCase7.txt
│   └── StatisticsResults.txt
│
├── Problema 2/
│   ├── convertNumbers.py
│   ├── testCase1.txt
│   ├── ...
│   ├── testCase7.txt
│   └── ConvertionResults.txt
│
└── Problema 3/
    ├── wordCount.py
    ├── testCase1.txt
    ├── ...
    ├── testCase7.txt
    └── WordCountResults.txt
```

---

## Programa 1 – Compute Statistics

### Descripción

Calcula estadísticas descriptivas a partir de un archivo con números:

* Media
* Mediana
* Moda
* Varianza
* Desviación estándar

### Ejecución

Desde la carpeta **Problema 1**:

```bash
python computeStatistics.py testCase1.txt
```

### Salida

* Resultados en consola
* Archivo generado: `StatisticsResults.txt`

---

## Programa 2 – Converter

### Descripción

Convierte números decimales a:

* Binario
* Hexadecimal

Las conversiones se realizan **sin usar funciones nativas** como `bin()` o `hex()`.

### Ejecución

Desde la carpeta **Problema 2**:

```bash
python convertNumbers.py testCase1.txt
```

### Salida

* Resultados en consola
* Archivo generado: `ConvertionResults.txt`

---

## Programa 3 – Count Words

### Descripción

Identifica todas las palabras distintas dentro de un archivo de texto y cuenta cuántas veces aparece cada una.

* No distingue mayúsculas/minúsculas
* Ignora signos de puntuación

### Ejecución

Desde la carpeta **Problema 3**:

```bash
python wordCount.py testCase1.txt
```

### Salida

* Resultados en consola
* Archivo generado: `WordCountResults.txt`

---

## Casos de prueba y resultados

Los **casos de prueba (`testCase1.txt` a `testCase7.txt`)** se encuentran dentro de cada carpeta de problema.

---

## Verificación con pylint

Cada programa fue analizado con pylint obteniendo:

```
Your code has been rated at 10.00/10
```
Se usa "# pylint: disable=invalid-name" ya que genera el error con el nombre del archivo siendo camelCase

Esto garantiza:

* Cumplimiento total de PEP-8
* Ausencia de errores, advertencias y malas prácticas

---

## Autor

**Nombre:** Arturo González Corona
**Matrícula:** A01796900
**Actividad:** A4.2 – Pruebas y Calidad de Software