# Void-Bot-PPF-Discord
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

## Pasos para correr el script:
1. Instalar Python
2. Instalar dependencias copiando el siguiente comando
```pip install dhooks websocket-client```
3. Correr el script del void con main.py
```python3 main.py```

## Considerar lo siguiente
- Introducir datos en `data.json`
 - `URL: (Obligatorio) Link de webhook, ej: https://discord.com/api/webhooks/`
 - `role: ID de rol cuando void gana, ej: <@&9298219>`
 - `alert: Es opcional, notifica cuando el void empieza`
 - `logger: Webhook para log de chat es (Opcional, se puede dejar vacio)`
 - Asi tiene que quedar:
![data](/media/data.png)

## Ejecutando en distintos entornos
- En entornos linux solo es necesario seguir los pasos de arriba.
- Es recomendable correr en un entorno Linux, ideal un servidor dedicado o sitio web que permita hostear el servidor
- Termux (Android) es muy recomendable, corre de fondo donde quiera que vayas, sin necesidad de mantener la PC encendida ni la app abierta

En Windows se necesitaría lo siguiente:
1. Instalar **Terminal** de Windows en Microsoft Store
2. Instalar Python.exe, en Google
3. Instalar main.py y data.json de este repositorio, y asignarlo en una carpeta dedicada.
![directorio](https://raw.githubusercontent.com/ripiner/Void-bot-PPF-discord/main/media/directorio.png)
4. Click derecho y "Abrir en terminal"
![Click](/media/click.png)
5. Seguir los pasos de arriba para correr el script ↖️
