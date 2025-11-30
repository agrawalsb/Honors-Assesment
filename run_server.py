import subprocess
import sys
import os

def install_deps():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn"])
        print("Dependencies installed successfully!")
    except:
        print("Failed to install dependencies. Please install manually: pip install fastapi uvicorn")

def run_server():
    try:
        print("Starting server on http://localhost:8000")
        print("API endpoints:")
        print("- GET http://localhost:8000/api/products")
        print("- POST http://localhost:8000/api/order")
        subprocess.run([sys.executable, "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"])
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error running server: {e}")
        print("Try running manually: python -m uvicorn server:app --host 0.0.0.0 --port 8000")

if __name__ == "__main__":
    install_deps()
    run_server()