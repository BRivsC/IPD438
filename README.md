# Comparativa de métodos de asignación de servidores CDN a clientes

Este repositorio contiene scripts y recursos utilizados para realizar pruebas de rendimiento en diversas redes de entrega de contenido (CDN). Incluye scripts de Python, gráficos generados a partir de los datos de las pruebas, registros detallados de las pruebas y un paper que documenta los hallazgos.

## Contenido

- `test_CDNs.py`: Un script de Python que realiza pruebas de rendimiento en varios servicios CDN como AWS, Cloudflare y Bing. Mide el tiempo de respuesta y el ancho de banda. Incluye un parámetro `N` con el que se puede cambiar el número de requerimientos que se le hacen a los servicios.
- `plots/`: Carpeta que contiene gráficos generados a partir de los datos de las pruebas, presentados en el paper.
- `logs/`: Carpeta que contiene los registros de las pruebas realizadas, con detalles de tiempo de respuesta y ancho de banda.
- `Informe_final_IPD438_Bastián_Rivas.pdf`: Un PDF del paper que documenta los hallazgos de las pruebas y análisis de rendimiento.

## Requisitos
Los experimentos se hicieron en máquinas virtuales montadas en Microsoft Azure con Ubuntu 22.04.5 LTS (GNU/Linux 6.5.0-1025-azure x86_64), 1 vCPU, 1 GiB RAM y con Python 3.10.12

## Correr experimento
Para correr el experimento basta con subir `test_CDNs.py` y ejecutarlo con
```
python test_CDNs.py
```
Los resultados se guardan en un archivo `cdn_performance.log`. Recomiendo ajustar sus nombres en base a las zonas donde se monten las máquinas.

## Autor
Bastián Rivas, para el ramo IPD438 de la UTFSM el 2024.
