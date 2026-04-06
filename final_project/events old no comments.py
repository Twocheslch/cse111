import json
import uuid

EVENTS_FILE = "final_project/events.json"


def load_events(path=EVENTS_FILE):
    """
    Load events from a JSON file and return a list of dictionaries.

    Behavior:
      • Opens the file in text mode and uses json.load().
      • On invalid/malformed JSON, exits the program with SystemExit("Cannot read JSON file - bad format.").
      • On missing file, exits the program with SystemExit(f"Cannot find file {path}").
    """
    try:
        with open(path, "rt") as file:
            events_list = json.load(file)
            return events_list
    except FileNotFoundError:
        raise SystemExit(f"Cannot find file {path}")
    except json.JSONDecodeError:
        raise SystemExit("Cannot read JSON file - bad format.")



def save_events(events, path=EVENTS_FILE):
    """
    Save events to a JSON file using json.dump().

    Returns True on success and False on IOError.
    """
    try:
        with open(path, "wt") as file:
            json.dump(events, file, indent=2)
        return True
    except IOError:
        return False



def add_event(events, name, sport, day, start_time, location, notes=""):
    """Create a new event, append it to events, and return it."""
    if day == 7:
        raise ValueError("Sunday is not allowed.")

    new_event = {
        "id": str(uuid.uuid4()),
        "event_name": name,
        "sport": sport,
        "day": day,
        "start_time": start_time,
        "location": location,
        "notes": notes,
    }

    events.append(new_event)
    return new_event



def view_by_day(events, day):
    """Return matching events for a day sorted by start_time."""
    matching_events = filter(lambda event: event["day"] == day, events)
    sorted_events = sorted(matching_events, key=lambda event: event["start_time"])
    return sorted_events



def update_event_name(events, event_id, event_name):
    """Find an event by id and update its event_name in place."""
    matchers = list(filter(lambda event: event["id"] == event_id, events))

    if len(matchers) == 0:
        return False

    matchers[0]["event_name"] = event_name
    return True



def delete_event(events, event_id):
    """Delete an event by id and return True if removed."""
    matchers = list(filter(lambda event: event["id"] == event_id, events))

    if len(matchers) == 0:
        return False

    events.remove(matchers[0])
    return True
