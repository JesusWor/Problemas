# Problemas

Repositorio personal de soluciones a problemas de programacion, organizado por plataforma: LeetCode, HackerRank y competencias de tipo ICPC. Las soluciones estan escritas principalmente en C++, Java y Python.

Este no es un paquete ni una libreria instalable, sino una coleccion de codigo de referencia. Puede clonarse o forkearse directamente para consultar los enfoques, comparar soluciones o usarlo como base de estudio.

## Estructura del repositorio

```
Problemas/
├── LeetCode/
│   ├── Easy/
│   └── Medium/
│       └── <numero> <NombreDelProblema>/
│           ├── solucion.cpp
│           ├── solucion.py
│           └── Solucion.java
├── HackeRanck/
│   ├── Algorithms/
│   ├── Greedy/
│   └── Math/
├── ICPC2026-Fase0/
│   ├── Problemas/      # enunciados en PDF
│   └── Soluciones/     # codigo de las soluciones
└── README.md
```

Cada carpeta de problema puede incluir la misma solucion en mas de un lenguaje (C++, Python, Java), segun como se haya resuelto originalmente. No todos los problemas cuentan con las tres versiones.

Esta estructura esta pensada para crecer: pueden agregarse carpetas de problemas o plataformas nuevas sin necesidad de modificar este documento.

## Requisitos

- Compilador de C++ (g++ o equivalente)
- JDK (Java 8 o superior)
- Python 3

## Uso

### Clonar el repositorio

```bash
git clone https://github.com/JesusWor/Problemas.git
cd Problemas
```

### Crear un fork

Utilice el boton "Fork" en GitHub para obtener una copia propia y clone esa copia siguiendo el mismo procedimiento, reemplazando la URL por la de su fork.

### Ejecutar una solucion

```bash
# Python
python3 ruta/al/archivo.py

# C++
g++ ruta/al/archivo.cpp -o solucion && ./solucion

# Java
javac ruta/al/Archivo.java && java -cp ruta/al Archivo
```

Ajuste la ruta y el nombre del archivo o clase segun el problema que desee ejecutar.

## Lenguajes utilizados

- C++
- Java
- Python

## Temas cubiertos

| Categoria             | Ejemplos                                                              |
| ---------------------- | ---------------------------------------------------------------------- |
| Estructuras de datos   | Arreglos, listas ligadas, pilas, colas                                 |
| Algoritmos             | Busqueda, ordenamiento, greedy, matematicas                            |
| Programacion competitiva | Problemas de fases eliminatorias estilo ICPC (enunciado en PDF y solucion) |

## Contribuciones

Este es un repositorio de aprendizaje personal. Si encuentra un error o propone una solucion mas eficiente, puede abrir un issue o un pull request. Se agradece cualquier retroalimentacion.

## Aviso

Estas soluciones tienen fines educativos. Se recomienda usarlas como referencia para comprender distintos enfoques y no enviarlas directamente como propias a ninguna plataforma de evaluacion.

## Licencia

Distribuido bajo licencia MIT. Si el archivo `LICENSE` aun no existe en la raiz del repositorio, se recomienda agregarlo con el texto estandar de dicha licencia.

---

Mantenido por [JesusWor](https://github.com/JesusWor)