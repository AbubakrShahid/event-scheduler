import json
import os
from models.event import Event

class Scheduler:
    def __init__(self, file_path="events.json"):
        self.file_path = file_path
        self.event_id_counter = 1
        self.events = self.load_events()

    def load_events(self):
        """Load events from the file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                events_data = json.load(file)
                self.events = [Event(**event) for event in events_data]
                self.event_id_counter = max([event.id for event in self.events], default=0) + 1
        else:
            self.events = []
        return self.events

    def save_events(self):
        """Save events to the file."""
        with open(self.file_path, 'w') as file:
            json.dump([event.to_dict() for event in self.events], file, indent=4)

    def get_all_events(self):
        return [event.to_dict() for event in self.events]

    def get_event(self, event_id):
        for event in self.events:
            if event.id == event_id:
                return event.to_dict()
        return None

    def is_conflict(self, new_event):
        for event in self.events:
            if event.start_date == new_event.start_date and \
               event.start_time == new_event.start_time and \
               set(event.repeat_days).intersection(set(new_event.repeat_days)):
                return True
            if not event.repeat_days and not new_event.repeat_days:
                if event.start_date == new_event.start_date and event.start_time == new_event.start_time:
                    return True
        return False

    def create_event(self, name, start_date, start_time, duration, repeat_days=None):
        new_event = Event(
            id=self.event_id_counter,
            name=name,
            start_date=start_date,
            start_time=start_time,
            duration=duration,
            repeat_days=repeat_days
        )

        if self.is_conflict(new_event):
            return None

        self.events.append(new_event)
        self.event_id_counter += 1
        self.save_events()
        return new_event.to_dict()

    def update_event(self, event_id, **kwargs):
        for event in self.events:
            if event.id == event_id:
                for key, value in kwargs.items():
                    setattr(event, key, value)
                self.save_events()
                return event.to_dict()
        return None
