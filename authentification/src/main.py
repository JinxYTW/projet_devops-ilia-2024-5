import os

from dotenv import load_dotenv

from config import app
<<<<<<< HEAD

=======
from routes import route
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
load_dotenv()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
<<<<<<< HEAD
    app.run(debug=debug_mode, port=5000)
=======
    app.register_blueprint(route)
    app.run(host="0.0.0.0", debug=debug_mode, port=5000)

>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
