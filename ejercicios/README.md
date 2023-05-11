# Módulo 3: Fundamentos Python

1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra asociada con esa calificación, de acuerdo con la siguiente tabla:

    |valor|equivalencia|
    |---|---|
    |0   - 2|D|
    |2.1 - 5|C|
    |5.1 - 6|B|
    |6.1 - 7|A|

2. Utilizando dos while anidados, construya la tablas de mutiplicacion. Ejemplo:

    ```python 
    while condicion1:
        while condicion2:
            .....

3. Escriba un programa que calcule el máximo común divisor entre dos números enteros.

4. Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
    
    Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

5. Escriba un programa que elimine un signo de exclamación del final de una cadena. Puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

6. Se le ha asignado un tarea para programar un algoritmo para una lavadora, debe investigar cuanta agua se necesita para lavar prendas con las siguientes características: *algodon*, *nylon*, *poliester*. Debe investigar para una lavadora de xx kg cuantas prendas de cada una puede lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente

    Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, entonces necesitas **5 * 1.1 ^ (14 - 10)** cantidad de agua.

    Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
    La función aceptará 2 argumentos: carga lavadora y ropa.

7. Cree una función notaFinal, que calcule la nota final de un estudiante en función de dos parámetros: una nota para el examen y una cantidad de proyectos completados.

    Esta función debe tomar dos argumentos: examen - calificación del examen (de 0 a 100); proyectos - número de proyectos completados (de 0 en adelante);
    Esta función debería devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:

    - 100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
    - 90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
    - 75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.


