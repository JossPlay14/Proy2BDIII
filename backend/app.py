from src import create_app
from .config import Config  # Usa punto para imports relativos
from .extensions import mongo

app = create_app()

if __name__ == "__main__":
    from src.config import Config

    app.run(port=Config.PORT, debug=Config.DEBUG)
