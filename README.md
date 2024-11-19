# Scripts de Control para Proyecto Flask

Este repositorio contiene tres scripts shell para gestionar el ciclo de vida de la pagina web ELEGANZA en Flask con una base de datos en MySQL80.

## Descripción de los Scripts

### 1. `ini_cero.sh`
Este script realiza la configuración inicial completa del proyecto:

```bash 
python -m venv venv # Crea un nuevo entorno virtual
pip install -r requirements.txt # Instala todas las dependencias
source venv/Scripts/activate # Activa el entorno virtual
net start MySQL80 # Inicia el servidor MySQL
python run.py # Ejecuta la aplicación Flask
```

### 2. `ini_flask.sh`
Este script inicia el servidor Flask:   
```bash
source venv/Scripts/activate
net start MySQL80
python run.py
```

### 3. `stop_flask.sh`
Este script detiene el servidor Flask:

```bash
net stop MySQL80
deactivate
```

## Notas: 
> [!IMPORTANT]
> - Asegúrate de que el archivo `requirements.txt` existe y contiene todas las dependencias necesarias
> - Los scripts deben tener permisos de ejecución
> - El servicio MySQL debe llamarse "MySQL80" en tu sistema
> - El entorno virtual se creará en una carpeta llamada "venv"

> [!WARNING]
> - Este repositorio está configurado para ejecutarse en un entorno Windows. Si estás utilizando un entorno Linux, es posible que necesites ajustar los comandos de activación del entorno virtual y la gestión del servidor MySQL. 
  
__autor__: <span style="color:purple">@Curcolor</span>