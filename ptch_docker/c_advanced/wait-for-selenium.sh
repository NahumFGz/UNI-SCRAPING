#!/bin/bash

# URL del Selenium Server
SELENIUM_URL="http://localhost:4444/wd/hub/status"

echo "Esperando a que Selenium esté disponible..."

# Esperar hasta que Selenium responda correctamente
while ! curl -s $SELENIUM_URL | grep '"ready":true' > /dev/null; do
    echo "Selenium aún no está listo, esperando..."
    sleep 2
done

echo "Selenium está listo, ejecutando demo.py..."
/home/seluser/venv/bin/python demo.py
