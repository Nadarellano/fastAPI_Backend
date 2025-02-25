# fastAPI_Backend
Creación de API con FastAPI un framework web de Python que permite crear APIs de manera rápida y eficiente.
Una de sus ventajas es que FastAPI proporciona documentación automática para que los desarrolladores no tengan que escribir documentación extensa. 

Comando para crear un entorno virtual llamado env
```shell
python -m venv env
```

Comando para activar entorno virtual en Windows
```shell
. env/Scripts/activate
```

Crear archivo requirements.txt (Dependencias)
```shell
pip freeze > requirements.txt
```

Instalar dependencias a partir del archivo requirments.txt.
```shell
pip install -r requirements.txt
```

Comando para ejecutar aplicación
```shell
uvicorn main:app --port 5000 --reload
```

Comando para desactivar el entorno virtual
```shell
deactivate
```