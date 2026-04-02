#UUID4 = university unique identifier version 4 
#That's 36 bytes long
#Make a project to ask for a UUID

import uuid

new_id = uuid.uuid4()
print(new_id)
print(type(new_id))

id_string = str(new_id)
print(id_string)

def create_event(name, date):
    event = {
        "id": str(uuid.uuid4()),
        "name": name,
        "date": date
    }
    return event

event = create_event("python_meetup", "2026/5/12")
print(event)
