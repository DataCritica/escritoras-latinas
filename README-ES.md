### [English](README.md)    
---

# Escritoras Latinoamericanas

Este repositorio fue desarrollado para el código y los datos detrás de la historia [Una constelación de escritoras latinoamericanas (nacidas en el siglo XX)](https://datacritica.org/portfolio/constelaciones-de-escritoras-latinoamericanas-nacidas-en-el-siglo-xx/)

El análisis utiliza extracción de datos de las entradas de Wikipedia para escritoras latinoamericanas y visualización de gráficos de red para crear una [aplicación web](http://escritoraslatam.datacritica.org/).

---

## Estructura de directorios

```
├── app.py                              # Archivo de la aplicación de Streamlit
├── assets                              # Recursos para el proyecto
│   ├── datacritica
│   ├── imgs
│   ├── imgs_processed
│   ├── mosaics
│   ├── targets
│   └── targets_processed
├── data                                # Datos categorizados 
│   ├── processed                       # Datos limpios
│   │   ├── escritoras_wiki.csv
│   │   └── escritores_destacados.csv
│   └── raw                             # Datos sin procesar
│       └── escritoras.csv
├── Dockerfile                          # Comandos para crear una imagen en docker
├── docs                                # Material explicativo
│   ├── data-dictionary.md              # Información sobre los datos
│   └── references                      # Documentos, manuales, artículos, etc.
├── escritoras_latinas                  # Módulo de Python
│   ├── data                            # Funciones para manipular datos
│   │   ├── analyze.py                  # Módulo de análisis de datos
│   │   ├── export.py                   # Módulo para guardar exportaciones
│   │   ├── load.py                     # Módulo para cargar datos y rutas
│   │   └── process.py                  # Módulo para procesar datos
│   └── utils                           # Funciones para realizar patrones comunes
│       └── paths.py                    # Módulo para generar rutas relativas
├── LICENSE                             # Licencia del proyecto
├── notebooks                           # Cuadernos de Jupyter
│   ├── 0.0-scrapping-text.ipynb
│   ├── 0.1-scrapping-text.ipynb
│   ├── 0.2-scrapping-images.ipynb
│   ├── 1.0-annotate-data.ipynb
│   ├── 1.1-process-images.ipynb
│   ├── 2.0-visualize-network.ipynb
│   ├── 2.1-visualize-network.ipynb
│   └── 2.2-visualize-donut-chart.ipynb
├── outputs                             # Exportaciones generadas por los cuadernos
│   ├── figures                         # Gráficos, mapas, etc.
│   │   └── index.html
|   ├── networks                        # Red de nodos
│   │   └── index.html
│   └── tables                          # Tablas dinámicas
│   ├── LICENSE
│   ├── photomosaics
│   │   ├── photomosaics.py
│   │   ├── run.py
│   │   └── scrape.py
│   ├── README.md
│   └── requirements.txt
├── Pipfile                             # Dependencias del proyecto
├── Pipfile.lock                        # Versiones específicas de paquetes en Pipfile
├── README.md                           # README principal del proyecto
├── README-ES.md                        # README en español
├── requirements.txt                    # Dependencias del proyecto
├── setup.py                            # Importar el proyecto como un módulo de Python
└── style.css                           # Estilos para la aplicación de streamlit
```
---

## Licencia

Este proyecto está liberado bajo [Licencia MIT](/LICENSE).

---

Este repositorio fue generado con [cookiecutter](https://github.com/cookiecutter/cookiecutter) utilizando la plantilla [data-journalism](https://github.com/DataCritica/cookiecutter-data-journalism) para python.