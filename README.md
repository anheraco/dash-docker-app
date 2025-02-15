# Dashboard de Segmentación de Comercios 🚀

Este proyecto es un **dashboard interactivo** construido con **Dash** y desplegado con **Docker**. Utiliza **K-Means** para segmentar comercios según su actividad de transacciones y ventas.

## 📌 Características
- Carga y procesamiento de datos desde un archivo Excel.
- Segmentación de comercios con **K-Means**.
- Visualización interactiva con **Plotly y Dash**.
- Desplegable para filtrar segmentos de comercios.
- Puede ejecutarse en **Docker** y desplegarse en **Render o Railway**.

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/)
- [VS Code](https://code.visualstudio.com/)

## 📂 Estructura del Proyecto

```
dash-docker-app/
│── data/                       # Carpeta para archivos de datos
│   └── DataTransacciones_PruebasIngreso.xlsx  # Archivo de datos
│── app.py                      # Código del dashboard con Dash
│── Dockerfile                   # Archivo para construir la imagen Docker
│── requirements.txt              # Lista de dependencias de Python
│── .gitignore                   # Ignorar archivos innecesarios en Git
│── README.md                    # Documentación del proyecto
│── venv/                        # Entorno virtual de Python (opcional)
```

## 💻 Instalación y Ejecución Local

1. **Clonar el repositorio**:
   ```sh
   git clone https://github.com/TU-USUARIO/dash-docker-app.git
   cd dash-docker-app
   ```

2. **Crear y activar un entorno virtual** (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/Scripts/activate  # En Windows
   ```

3. **Instalar dependencias**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```sh
   python app.py
   ```
   Luego abre `http://127.0.0.1:8050/` en tu navegador.

## 🐳 Ejecución con Docker

1. **Construir la imagen Docker**:
   ```sh
   docker build -t dash-app .
   ```

2. **Ejecutar el contenedor**:
   ```sh
   docker run -p 8050:8050 dash-app
   ```

## 🌍 Despliegue en Render o Railway

### **Render**
1. Crea una cuenta en [Render](https://render.com/).
2. Conéctalo con GitHub y selecciona el repositorio.
3. En **Environment**, elige **Docker**.
4. Render construirá y desplegará la app.

### **Railway**
1. Crea una cuenta en [Railway](https://railway.app/).
2. Importa el repositorio desde GitHub.
3. Configura Railway para usar **Docker**.
4. Railway usará el `Dockerfile` y desplegará la app.

## 🛠 Contribuciones
Si quieres mejorar el proyecto:
1. Haz un **fork** del repositorio.
2. Crea una **rama** nueva: `git checkout -b mi-mejora`.
3. Haz tus cambios y confirma: `git commit -m "Mejora"`.
4. Sube tu código: `git push origin mi-mejora`.
5. Abre un **pull request** en GitHub.

## 📄 Licencia
Este proyecto es de uso libre bajo la licencia MIT.

---

🎉 **¡Listo! Ahora puedes visualizar y segmentar comercios de manera interactiva!** 🚀

