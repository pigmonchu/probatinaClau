from tareas import app

@app.route("/")
def index():
    return "Flask rulando desde __init__"