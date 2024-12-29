from app import create_app

app = create_app()

@app.route('/')
def debug_index():
    return "Debug Route Working!"
