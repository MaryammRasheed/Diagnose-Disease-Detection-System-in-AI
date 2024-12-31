import subprocess
import os

def query_meditron(prompt: str, file_path: str = None):
    command = ["ollama", "run", "meditron", prompt]
    if file_path and os.path.exists(file_path):
        command.extend(["--image", file_path])
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr.strip())
    
    return result.stdout.strip()
