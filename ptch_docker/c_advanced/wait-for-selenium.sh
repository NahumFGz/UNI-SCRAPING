#!/bin/bash

# URL del Selenium Server
SELENIUM_URL="http://localhost:4444/wd/hub/status"

echo "🚀 Iniciando Selenium..."
/opt/bin/entry_point.sh &  # Inicia Selenium en segundo plano

echo "⌛ Esperando a que Selenium esté disponible..."

# Esperar hasta que Selenium responda correctamente
while true; do
    RESPONSE=$(curl -s $SELENIUM_URL)
    
    READY=$(echo $RESPONSE | jq -r '.value.ready')
    NODE_STATUS=$(echo $RESPONSE | jq -r '.value.nodes[0].availability')

    if [[ "$READY" == "true" && "$NODE_STATUS" == "UP" ]]; then
        echo "✅ Selenium está listo y el nodo está disponible."
        break
    else
        echo "❌ Selenium aún no está listo, esperando..."
        sleep 2
    fi
done

echo "🚀 Ejecutando demo.py..."
/home/seluser/venv/bin/python demo.py
