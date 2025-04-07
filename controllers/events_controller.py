from flask import jsonify, request
from services.scheduler import Scheduler
from utils.validators import validate_event_data

scheduler = Scheduler()

def get_events():
    return jsonify(scheduler.get_all_events()), 200

def get_event(event_id):
    event = scheduler.get_event(event_id)
    if event:
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404

def create_event():
    data = request.json
    is_valid, error = validate_event_data(data)
    if not is_valid:
        return jsonify({"error": error}), 400

    event = scheduler.create_event(
        name=data.get('name'),
        start_date=data.get('start_date'),
        start_time=data.get('start_time'),
        duration=data.get('duration'),
        repeat_days=data.get('repeat_days')
    )

    if event is None:
        return jsonify({"error": "Conflict with existing event"}), 409
    return jsonify(event), 201

def update_event(event_id):
    data = request.json
    is_valid, error = validate_event_data(data)
    if not is_valid:
      return jsonify({"error": error}), 400

    updated = scheduler.update_event(event_id, **data)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "Event not found"}), 404
