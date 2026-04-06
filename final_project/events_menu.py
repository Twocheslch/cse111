"""
events_menu.py — Optional interactive driver for manual testing

This file is NOT graded. It imports `events.py` and lets you try your functions.
"""
import events  # your implementation module


DAY_NAME = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
SPORTS = ["Basketball", "Volleyball", "Futsal"]
TIMES = ["17:00", "18:00", "19:00", "20:00", "21:00"]
LOCATIONS = ["Court 1", "Court 2", "Court 3", "Court 4"]
VALID_DAYS = [1, 2, 3, 4, 5, 6]  # Mon-Sat (7=Sunday not allowed)

def print_menu():
    print(
        "\nI-Center Sports Event Manager (manual test)\n"
        "1. Load events\n"
        "2. Save events\n"
        "3. Add event\n"
        "4. View events by day\n"
        "5. Update event\n"
        "6. Delete event\n"
        "7. Exit\n"
    )


def main():
    events_list = []
    while True:
        print_menu()
        choice = input("Select an option: ")
        if choice == "1":
            path = input(
                "Path to events.json [events.json]: ") or "events.json"
            try:
                events_list = events.load_events(path)
                print(f"Loaded {len(events_list)} events.")
            except SystemExit:
                print("Failed to load file.")
        elif choice == "2":
            path = input("Save to path [events.json]: ") or "events.json"
            success = events.save_events(events_list, path)
            print("Saved." if success else "Not saved!")
        elif choice == "3":
            name = input("Event name: ")
            sport = input(f"Sport {SPORTS}: ")
            day = int(input("Day (1=Mon..7=Sun): "))
            start_time = input(f"Start time {TIMES}: ")
            location = input(f"Location {LOCATIONS}: ")
            notes = input("Notes (optional): ")
            try:
                e = events.add_event(events_list, name=name, sport=sport, day=day,
                                     start_time=start_time, location=location, notes=notes)
                print(f"Created: {e['id']}")
            except ValueError:
                print("Add failed due to invalid input.")
        elif choice == "4":
            day = int(input("Day to view (1-6): "))
            res = events.view_by_day(events_list, day)
            if not res:
                print("No events.")
            else:
                for e in res:
                    print(
                        f"{e['id']}: {DAY_NAME.get(e['day'], e['day'])} {e['start_time']} - {e['event_name']} ({e['location']})")
        elif choice == "5":
            event_id = input("Event ID: ")
            name = input("New name: ")
            ok = events.update_event_name(events_list, event_id, name)
            print("Updated." if ok else "Not found or invalid.")
        elif choice == "6":
            event_id = input("Event ID to delete: ")
            ok = events.delete_event(events_list, event_id)
            print("Deleted." if ok else "Not found.")
        elif choice == "7":
            print("See ya!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
