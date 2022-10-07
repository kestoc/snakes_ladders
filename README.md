# **PRUEBA TÉCNICA VEEVART - JUEGO SERPIENTES Y ESCALERAS**

## **Autor:** Kevin Steven Ocampo Morales :nerd_face:

## **Prerrequisitos:**
- Python3, ya que es el lenguaje de programación usado para desarrollar la prueba.
- Terminal ubicado en la carpeta del proyecto para ejecutar el programa.

## **Como ejecutar el programa:**
Primero se debe bajar o clonar el proyecto del repositorio GitHub. Una vez teniendo el proyecto en la máquina 
y cumpliendo con todos los prerrequisitos, podemos ejecutar en la terminal el comando:
```
python main.py < input.txt > output.txt
ó
python3 main.py < input.txt > output.txt
```
Y de esta manera se ejecutará el programa con el caso de prueba del archivo *input.txt* y el resultado estará en *output.txt*.
**Nota: el *> output.txt* es opcional, es para una mejor visualización, pero puede no ponerse y mostrar el resultado en consola.**

**Cabe resaltar que para probar con otros casos, se debe seguir la sintaxis definida en el archivo *input.txt* la cual corresponde a la siguiente:**
```
Tamaño del tablero, e.g. 5
Listado de ubicaciones de las serpientes y a donde descienden, e.g. 14 4 19 8 22 20 24 16
Listado de ubicaciones de las escaleras y a donde ascienden, e.g. 3 11 10 12 9 18 6 17
```

## **Como ejecutar las pruebas unitarias:**
Para ejecutar las 8 pruebas construidas para verificar el correcto funcionamiento del juego se debe ejecutar el siguiente comando en la terminal del proyecto:
```
python test.py
ó
python3 test.py
```
Y si se desea tener un poco más de información sobre el resultado de las pruebas ejecutadas, se debe ejecutar el siguiente comando:
```
python -m unittest -v test
ó
python3 -m unittest -v test
```