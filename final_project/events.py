"""
I-Center Sports Event Manager — Outline

This module provides function outlines and docstrings for students to implement.
Functions avoid user input and are designed for unit testing with pytest.

Data constraints:
- Days: 1..6 (Mon..Sat). Sunday (7) is not allowed.
"""

import json
import uuid

EVENTS_FILE = "final_project/events.json"



def load_events(path=EVENTS_FILE):
    """
    Load events from a JSON file and return a list of dictionaries.

    Behavior:
      • Opens the file in text mode and uses json.load(). See https://docs.python.org/3/library/json.html
      • On invalid/malformed JSON, exits the program with SystemExit("Cannot read JSON file - bad format.").
      • On missing file, exits the program with SystemExit(f"Cannot find file {path}").

    Parameters:
        path: Path to the JSON file (default: "events.json").

    Returns:
        list[dict]: The parsed JSON array of event dictionaries.

    Raises:
        SystemExit: If the file is missing or the JSON is malformed.
    """
    try:
        with open(path, "rt") as file:
            event_list = json.load(file)
            return event_list
    except FileNotFoundError:
        raise SystemExit(f"Cannot find file {path}")
    except json.JSONDecodeError:
        raise SystemExit("Cannot read JSON file - bad format.")


# return_value = load_events()
# You're gonna get the list of events

def save_events(events, path=EVENTS_FILE):
    """
    Save events to a JSON file using json.dump(). See https://docs.python.org/3/library/json.html

    Behavior:
      • Opens the file in text mode and dumps the given list as JSON.
      • Returns True on success; returns False if an IOError occurs.

    Parameters:
        events: A list of event dictionaries to write.
        path: Destination path for the JSON file (default: "events.json").

    Returns:
        bool: True if save succeeded; False if an IOError occurred.
    """
    try:
        with open(path, "wt") as file:
            json.dump(events, file, indent=2)
        return True
    except IOError:
        return False


# save = save_events(return_value)
# this should just write your stuff to the JSON file

def add_event(events, name, sport, day, start_time, location, notes=""):
    """
    Create a new event, append it to 'events', and return the newly created event.

    Behavior:
      • Generates a new UUID4 string for the "id" field.
      • Rejects day == 7 (Sunday) by raising ValueError.

    Parameters:
        events: The in-memory list of event dictionaries.
        name: Event display name.
        sport: Sport string (e.g., "Basketball", "Volleyball", "Futsal").
        day: Integer day of week (1=Mon .. 6=Sat). Sunday (7) is not allowed.
        start_time: Start time string (e.g., "19:00").
        location: Location string (e.g., "Court 1").
        notes: Optional notes string (default: "").

    Returns:
        dict: The newly created event dictionary that was appended.

    Raises:
        ValueError: If day == 7 (Sunday).
    """
    if day == 7:
        raise ValueError("Sunday is not allowed")

    new_event = {
        "id": str(uuid.uuid4()),
        "event_name": name,
        "sport": sport,
        "day": day,
        "start_time": start_time,
        "location": location,
        "notes": notes
    }

    events.append(new_event)
    return new_event



def view_by_day(events, day):
    """
    Return events for a specific day, sorted by 'start_time'.

    Behavior:
      • Uses filter() (no explicit loops) to select events where e["day"] == day.
      • Returns a NEW list sorted by "start_time" ascending.
      • Returns an empty list if there are no matches.

    Parameters:
        events: List of event dictionaries.
        day: Integer day of week to match.

    Returns:
        list[dict]: A list of dictionaries including only matching events sorted by start_time.
    """
    one_day = filter(lambda event: event["day"] == day, events)
    sorted_day = sorted(one_day, key=lambda event: event["start_time"])
    return sorted_day



def update_event_name(events, event_id, event_name):
    """
    Find an event by ID and update its 'event_name' in place.

    Behavior:
      • Locates the target via filter(...)
      • If found, sets event["event_name"] = event_name and returns True.
      • If not found, returns False.

    Parameters:
        events: List of event dictionaries (mutated if update succeeds).
        event_id: UUID string of the event to update.
        event_name: New string value for the 'event_name' field.

    Returns:
        bool: True if the event was found and updated; False otherwise.
    """
    matching_event = list(filter(lambda event: event["id"] == event_id, events))

    if len(matching_event) == 0:
        return False

    matching_event[0]["event_name"] = event_name
    return True



def delete_event(events, event_id):
    """Delete an event by ID and report whether removal occurred.

    Behavior:
      • Use filter(...) to retrieve the matching event object, then remove it.
      • Returns True if an event was removed; returns False if no event matched.

    Parameters:
        events: List of event dictionaries (mutated if removal succeeds).
        event_id: UUID string of the event to remove.

    Returns:
        bool: True if an event was removed; False if no matching ID was found
    """
    matching_event = list(filter(lambda event: event["id"] == event_id, events))

    if len(matching_event) == 0:
        return False

    events.remove(matching_event[0])
    return True
