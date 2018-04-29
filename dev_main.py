from server.server import app

if __name__ == '__main__':
    # Debug mode means the server auto updates
    # when code changes occur.
    app.run(port=5678, debug=True)
