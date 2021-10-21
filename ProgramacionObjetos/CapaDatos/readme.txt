Realizar entorno virtuales en python

Crear el entorno virtual
    python -m venv env


Activar el entorno virtual
    env\Scripts\activate

Instalar libreria para la conexion a la base datos
    pip install psycopg2

Importar un libreria de logging para manejo de registros y eventos de la app
Se crea objetos de conexion y cursor

Realizamos un CRUD con el metodo DAO (DATA ACCES OBJECT), es un patron de diseño para comunicar con una base de datos. Tiene operaciones CRUD