#!/bin/bash

#huggingface-cli download mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF --include "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf" --local-dir ./
# Check if model file exists
if [ ! -f "/models/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf" ]; then
    echo "Error: Model file not found!"
    echo "Please ensure meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf exists in the models directory"
    exit 1
fi

# Check file permissions
if [ ! -r "/models/meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf" ]; then
    echo "Error: Cannot read model file!"
    echo "Please check file permissions"
    exit 1
fi

echo "Model file exists and is readable"
exit 0 