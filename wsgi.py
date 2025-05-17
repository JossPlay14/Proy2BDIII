import sys
from os.path import abspath, dirname

# Añade el directorio backend al path
sys.path.append(abspath(dirname(__file__)))

from src.app import create_app  # Ajusta según tu estructura real

app = create_app()

if __name__ == "__main__":
    app.run()
