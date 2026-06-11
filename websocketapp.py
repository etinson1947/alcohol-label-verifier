from services.socket_service import socketio


socketio.init_app(app)


@app.route("/progress/<job_id>")
def progress(job_id):

    return {"status": "tracking"}