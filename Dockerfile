FROM --platform=linux/arm64 ollama/ollama:latest

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

EXPOSE 11434

# Add startup script
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

# Use shell to run the startup script
ENTRYPOINT ["/bin/bash"]
CMD ["/startup.sh"] 