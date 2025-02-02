#!/bin/bash

# Start Ollama service
/bin/ollama serve &

# Wait for Ollama to start
sleep 10

# Check if Ollama is responding
until curl --output /dev/null --silent --fail http://localhost:11434/api/tags; do
    echo "Waiting for Ollama to start..."
    sleep 5
done

# Create a temporary Modelfile
cat > /tmp/Modelfile << EOL
FROM /models/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.7
PARAMETER stop "User:"

SYSTEM You are a helpful AI assistant.
EOL

# Try to create the model using the Modelfile
/bin/ollama create local-llama3 -f /tmp/Modelfile

# Keep container running
tail -f /dev/null 