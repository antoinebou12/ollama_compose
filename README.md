# 🚀 Ollama Model Management and Docker Setup

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This repository simplifies the management of **Ollama models** and the deployment of a robust environment using **Docker Compose**. It provides a Python script for automating model pulls and a ready-to-use Docker Compose file for running services like OpenWebUI, SearXNG, Redis, Tika, and Pipelines.

---

## 🛠️ Features

- **Automated Ollama Model Pulling**:
  - Use `pull.py` to fetch multiple models effortlessly.
  - Supports both `.txt` file and default model lists.

- **Pre-configured Docker Compose**:
  - Deploy services such as OpenWebUI, Redis, SearXNG, Tika, and Pipelines.
  - GPU acceleration support included.

- **Customizable Setup**:
  - Easily modify configurations to meet your needs.

---

## 📦 Installation

### Prerequisites
- Python 3.8 or later
- Docker and Docker Compose
- Ollama CLI installed and configured

### Clone the Repository
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

---

## 🔧 Usage

### 🐳 Docker Compose

#### **Start Services**
1. Navigate to the directory containing the `docker-compose.yml` file:
   ```bash
   cd your-repo-name
   ```
2. Start the services:
   ```bash
   docker-compose up -d
   ```

#### **Access Services**
- **OpenWebUI**: [http://localhost:3000](http://localhost:3000)
- **SearXNG**: [http://localhost:8080](http://localhost:8080)
- **Pipelines**: [http://localhost:9099](http://localhost:9099)
- **Tika**: [http://localhost:9998](http://localhost:9998)

#### **Stop Services**
```bash
docker-compose down
```

---

### 🐍 `pull.py` Script

#### **Default Models**
By default, `pull.py` includes:
- `deepseek-r1`
- `llama3.3`
- `llama3.2-vision:11b`
- `command-r7b`
- `qwen2.5:32b`
- `qwen2.5:7b`
- `granite-embedding`
- `nomic-embed-text`
- `llava:34b`

#### **Using Custom Models**
1. Create a `models.txt` file in the same directory as `pull.py`.
2. Add one model name per line, for example:
   ```
   model-name-1
   model-name-2
   model-name-3
   ```

#### **Run the Script**
```bash
python pull.py
```

#### **Script Workflow**
1. Reads models from `models.txt` (if available) or defaults to the predefined list.
2. Pulls models using `ollama pull`.
3. Displays success or failure for each model.

---

## 🛠️ Configuration

### Docker Compose Customization
- **Services**:
  - Modify `docker-compose.yml` to add or remove services.
- **GPU Support**:
  - Ensure NVIDIA drivers and `nvidia-container-toolkit` are installed for GPU acceleration.
- **Networks**:
  - Adjust the `networks` section to fit your environment.

### Python Script
- **Default Models**:
  - Update the `default_models` list in `pull.py` to add or remove models.
- **Custom Models**:
  - Use a `models.txt` file for dynamic model loading.

---

## 📚 Tutorials

### 1. **How to Use the `pull.py` Script**
   - Create or edit the `models.txt` file.
   - Run `python pull.py` to fetch models.

### 2. **Deploy Docker Services**
   - Start Docker Compose with `docker-compose up -d`.
   - Access services via their respective URLs.

### 3. **Integrating a New Service**
   - Add the service configuration in `docker-compose.yml`.
   - Restart Docker Compose.

---

## 🛡️ License

This project is licensed under the MIT License.

---
