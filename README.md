# Local LLaMa3 Enterprise Chat Interface

## Description

This project provides a secure, on-premise AI solution designed for enterprise environments, leveraging the capabilities of LLaMa3 through a user-friendly Streamlit interface. It enables organizations to implement powerful AI capabilities while maintaining complete control over their data and infrastructure.

### Key Features
- **On-Premise Deployment**: Full control over data security and privacy
- **Enterprise-Ready**: Designed for integration with existing corporate infrastructure
- **Department-Specific Customization**: Adaptable for various business units including:
  - Technical Support
  - Sales Operations
  - Customer Service
  - Research & Development
  - Documentation Management
  - Human Resources
- **Scalable Architecture**: Built on Docker for consistent deployment and scaling
- **Data Security**: Keeps sensitive information within your organization's boundaries

### Business Applications
- **Technical Support**: Enhance support capabilities with AI-powered response generation
- **Sales Operations**: Assist with product information and customer inquiries
- **Documentation**: Automated analysis and summarization of corporate documents
- **Training**: Support for employee onboarding and continuous learning
- **Customer Service**: Improve response times and service quality
- **Internal Knowledge Base**: Quick access to organizational knowledge

## Prerequisites

- Docker and Docker Compose
- Git
- 8GB+ RAM (16GB+ recommended for production)
- The LLaMa3 model file (`meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf`)
- Corporate firewall configurations (if applicable)

## Project Structure
```
project/
├── docker-compose.yml
├── Dockerfile
├── Modelfile
├── models/
│   └── [Add your model here]
├── startup.sh
├── check_model.sh
└── streamlit_app.py
```

## Enterprise Deployment

1. Clone the repository:
   ```bash
   git clone https://github.com/mart-planB/ai-on-docker
   cd https://github.com/mart-planB/ai-on-docker
   ```

2. Place the LLaMa3 model file in the `models` directory:
   ```bash
   cp path/to/[models]] ./models/
   ```

3. Configure environment settings (optional):
   ```bash
   # Edit docker-compose.yml for custom configurations
   # Adjust memory allocation and network settings as needed
   ```

4. Deploy the application:
   ```bash
   docker-compose up -d
   ```

5. Access the interface:
   - Internal network: `http://localhost:8501`
   - Configure reverse proxy settings for corporate network access

## Security Considerations

- Deployed within corporate network boundaries
- No external API calls or data transmission
- Configurable access controls
- Compatible with corporate VPN and firewall settings

## System Requirements

### Minimum Requirements
- CPU: 4 cores
- RAM: 8GB
- Storage: 20GB available space

### Recommended Specifications
- CPU: 8+ cores
- RAM: 16GB+
- Storage: 50GB+ SSD
- Network: 1Gbps

## Usage Guidelines

1. Access the chat interface through your corporate browser
2. Authenticate using corporate credentials (if configured)
3. Input queries or upload documents for analysis
4. Receive AI-generated responses based on your input

## Maintenance

To stop the application:
```bash
docker-compose down
```

For updates and maintenance:
```bash
git pull
docker-compose build --no-cache
docker-compose up -d
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/EnhancementName`)
3. Commit your changes (`git commit -m 'Add some EnhancementName'`)
4. Push to the branch (`git push origin feature/EnhancementName`)
5. Open a Pull Request

## Support

For enterprise support and customization:
- Create an issue in the repository
- Contact your system administrator
- Refer to internal documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- LLaMa3 model developers
- Streamlit framework
- Docker platform
- Enterprise deployment contributors
