import subprocess
import os

def pull_ollama_model(model_name):
    """
    Pull a specific Ollama model using the 'ollama pull' command.
    """
    try:
        print(f"Pulling model: {model_name}")
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"Successfully pulled: {model_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to pull {model_name}. Error: {e}")

def load_models_from_file(file_path):
    """
    Load a list of models from a .txt file.
    """
    if os.path.exists(file_path):
        print(f"Loading models from file: {file_path}")
        with open(file_path, "r") as file:
            models = [line.strip() for line in file if line.strip()]
        return models
    else:
        print(f"File {file_path} not found. Using default model list.")
        return None

def main():
    """
    Main function to pull models.
    """
    # Path to the .txt file containing model names
    model_file_path = "models.txt"

    # Default list of models
    default_models = [
        "deepseek-r1",
        "llama3.3",
        "llama3.2-vision:11b",
        "command-r7b",
        "qwen2.5:32b",
        "qwen2.5:7b",
        "granite-embedding",
        "nomic-embed-text",
        "llava:34b"
    ]

    # Load models from file or use default list
    models = load_models_from_file(model_file_path) or default_models

    # Pull all models
    for model in models:
        pull_ollama_model(model)

if __name__ == "__main__":
    main()
