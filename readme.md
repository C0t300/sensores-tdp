# Taller de Progra

## Explicación

Este proyecto se basa en la simulación de un invernadero automático a base de sensores, actuadores y un controlador. El controlador se encarga de leer los datos de los sensores y en base a estos datos, activar o desactivar los actuadores.

## Forma de simular

- Se debe tener activemq funcionando
- Python 3.10 (Aunque debería funcionar con cualquier versión que tenga compatibilidad con [libreria de activemq](https://pypi.org/project/stomp.py/))
- Instalar lo indicado en el requirements.txt (idealmente con pyenv)
- Iniciar el listener.py
- Iniciar el errorAleatorioShutoff.py
- Iniciar el sendShutoff.py

Esto debería generar una simulación completa por segundos. Y crear archivos de log en la carpeta `logs/`, de forma de ver su funcionamiento (además de en la consola).

## Integrantes

- Elias Pizarro
- Manuel Valenzuela
- José Runín
- Javier Maturana
