from flask import Blueprint
from controllers import events_controller

events_bp = Blueprint('events', __name__)

events_bp.route('/events', methods=['GET'])(events_controller.get_events)
events_bp.route('/events/<int:event_id>', methods=['GET'])(events_controller.get_event)
events_bp.route('/events', methods=['POST'])(events_controller.create_event)
events_bp.route('/events/<int:event_id>', methods=['PUT'])(events_controller.update_event)
