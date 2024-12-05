PASOS INICIALES
1. Crear la carpeta del proyecto
mkdir modafacil_app
2. ingresar a la carpeta
cd app_modafacil_python
3. Inicializar el repositorio en nuestro proyecto
 git init
observacion: si la rama esta por defecto en master cambiamos a main

git branch -m main
4. crear nuestro entorno virtual de python (al costado de venv ahi debe ir el nombre del entorno virtual).
(si le pongo un .venv al costado de venv puedo ocultar carpetas, y si quiero acceder cd ..)

python -m venv app_matricula_python
5. acceder y activar nuestro entrono virtual (Scripts siempre con mayuscula al inicio)
source app_matricula_python/Scripts/activate
6. para desactivar
deactivate

7. (es como el ´playstore de python) es una dependencia de python que me ayuda a instalar librerias de python
pip list
8. para instalar una libreria dentro de mi proyecto (se pone el nombre del pakete)
pip install