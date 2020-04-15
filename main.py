import api.flask_server as flask_server
import api.backend as backend
import threading

flask_server_thread = threading.Thread(target=flask_server.start)
flask_server_thread.start()
backend.start()
