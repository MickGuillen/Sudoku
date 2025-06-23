# Proyecto: Sudoku en Python

Este proyecto implementa un algoritmo para resolver tableros de Sudoku utilizando un enfoque de **fuerza bruta con backtracking**. A través del uso de recursividad y validaciones adicionales, como las diagonales principales, el programa encuentra la solución del tablero inicial proporcionado.

## Descripción

El programa recibe un tablero de Sudoku incompleto (con ceros representando espacios vacíos) y busca completarlo cumpliendo las reglas clásicas del juego:  
- No se repiten números del 1 al 9 en la misma fila, columna o subcuadro 3x3.  
- Como validación adicional, también se asegura que no se repitan números en las diagonales principales.

Durante la ejecución, el sistema muestra el Sudoku resuelto, el tiempo que tardó en encontrar la solución y la cantidad total de operaciones realizadas.

## Tecnologías utilizadas

- Python 3.x  
- Módulo `time` (para calcular el tiempo de ejecución)  

## Instrucciones de uso

### 1. Clonar o copiar el script

Descarga el archivo `.py` o copia el código directamente a tu entorno local.

### 2. Ejecutar el programa

Puedes correr el archivo desde cualquier entorno de desarrollo que soporte Python, como IDLE, VS Code o desde la terminal:
python sudoku_solver.py

### 3. Resultados esperados

El programa imprimirá en consola:

- El tablero completamente resuelto.
- El tiempo total que tardó en encontrar la solución.
- El número de operaciones realizadas durante el proceso de resolución.

## Funcionalidades

- ✅ Resolución automática de tableros de Sudoku con validación clásica y de diagonales.  
- 📈 Muestra estadísticas de rendimiento: tiempo de ejecución y número de operaciones.  
- 🔁 Algoritmo recursivo de backtracking eficiente.  
- 🧩 Representación visual del tablero antes y después de ser resuelto.  

## Autor

Desarrollado por [Alan Guillen](https://github.com/MickGuillen)


