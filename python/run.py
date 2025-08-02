"""
This module is used to call the flask code.
"""

from src.main import app

# Flask has the built-in Werkzeug server.
# Only run the dev server if this file is executed directly

# host='0.0.0.0' -> Exposes the app to all network interfaces, not just localhost.
# port=8080	-> Binds the app to port 8080.
# debug=True -> Enables debug mode, which provides automatic reload + debugger.
# threaded=True	-> Enables multi-threading, so one process can handle multiple requests concurrently

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "any random string"
    app.run(host="0.0.0.0", port=4999)
