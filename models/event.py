from datetime import datetime
from typing import List

class Event:
    def __init__(self, id, name, start_date, start_time, duration, repeat_days=None):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration
        self.repeat_days = repeat_days or []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "duration": self.duration,
            "repeat_days": self.repeat_days
        }
