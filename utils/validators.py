from datetime import datetime

VALID_WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

def validate_event_data(data):
    required_fields = ['name', 'start_date', 'start_time', 'duration']
    missing = [field for field in required_fields if not data.get(field)]

    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    try:
        datetime.strptime(data['start_date'], '%Y-%m-%d')
    except ValueError:
        return False, "Invalid start_date format. Expected YYYY-MM-DD."

    try:
        datetime.strptime(data['start_time'], '%H:%M')
    except ValueError:
        return False, "Invalid start_time format. Expected HH:MM (24-hour)."

    if not isinstance(data['duration'], (int, float)) or data['duration'] <= 0:
        return False, "Duration must be a positive number."

    repeat_days = data.get('repeat_days')
    if repeat_days:
        if not isinstance(repeat_days, list) or not all(day in VALID_WEEKDAYS for day in repeat_days):
            return False, f"repeat_days must be a list containing valid weekdays: {', '.join(VALID_WEEKDAYS)}"

    return True, None
