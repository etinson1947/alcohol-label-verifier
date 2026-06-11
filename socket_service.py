from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")


def emit_progress(job_id, progress):

    socketio.emit(
        "progress_update",
        {
            "job_id": job_id,
            "progress": progress
        }
    )