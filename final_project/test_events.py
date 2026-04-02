
import json
import os
import builtins
import uuid
import types
import pytest

import events


# -------------------------------
# load_events tests
# -------------------------------

def test_load_events_success(tmp_path):
    data = [{"id": "1", "event_name": "Open Gym"}]
    f = tmp_path / "ok.json"
    f.write_text(json.dumps(data))
    result = events.load_events(path=str(f))
    assert result == data


def test_load_events_bad_json(tmp_path):
    f = tmp_path / "bad.json"
    f.write_text("{not: valid json}")
    with pytest.raises(SystemExit) as exc:
        events.load_events(path=str(f))
    assert str(exc.value) == "Cannot read JSON file - bad format."


def test_load_events_missing_file(tmp_path):
    missing = tmp_path / "missing.json"
    with pytest.raises(SystemExit) as exc:
        events.load_events(path=str(missing))
    assert str(exc.value) == f"Cannot find file {missing}"


# -------------------------------
# save_events tests
# -------------------------------

def test_save_events_success(tmp_path):
    events_list = [{"id": "2", "event_name": "League Night"}]
    out = tmp_path / "events.json"
    ok = events.save_events(events_list, path=str(out))
    assert ok is True
    # Verify file content was written
    loaded = json.loads(out.read_text())
    assert loaded == events_list


def test_save_events_ioerror(monkeypatch):
    events_list = [{"id": "3", "event_name": "Training"}]

    def boom(*args, **kwargs):
        raise IOError("disk full")

    # Force builtins.open to raise for this call
    monkeypatch.setattr(builtins, "open", boom)
    ok = events.save_events(events_list, path="anywhere.json")
    assert ok is False


# -------------------------------
# add_event tests
# -------------------------------

def test_add_event_success_generates_uuid_and_appends():
    store = []
    new = events.add_event(
        store,
        name="Evening Run",
        sport="Basketball",
        day=3,
        start_time="19:00",
        location="Court 2",
    )
    # Returned dict is appended to list
    assert new in store
    # Contains an id that is a UUID4 string
    assert "id" in new and isinstance(new["id"], str)
    # Validate UUID v4
    uuid_obj = uuid.UUID(new["id"], version=4)
    assert str(uuid_obj) == new["id"]
    # Notes default to empty string
    assert new.get("notes", "") == ""


def test_add_event_rejects_sunday():
    with pytest.raises(ValueError):
        events.add_event([], "Sun Event", "Futsal", 7, "17:00", "Court 1")


# -------------------------------
# view_by_day tests
# -------------------------------

def test_view_by_day_sorted_by_time():
    items = [
        {"id": "a", "event_name": "Late", "day": 2, "start_time": "21:00"},
        {"id": "b", "event_name": "Early", "day": 2, "start_time": "17:00"},
        {"id": "c", "event_name": "OtherDay", "day": 4, "start_time": "18:00"},
        {"id": "d", "event_name": "Middle", "day": 2, "start_time": "19:00"},
    ]
    result = events.view_by_day(items, 2)
    assert [e["id"] for e in result] == ["b", "d", "a"]


def test_view_by_day_no_matches_returns_empty_list():
    items = [{"id": "x", "event_name": "Only", "day": 6, "start_time": "18:00"}]
    assert events.view_by_day(items, 1) == []


# -------------------------------
# update_event tests
# -------------------------------

def test_update_event_found_updates_in_place():
    items = [{"id": "abc", "event_name": "Old"}]
    ok = events.update_event_name(items, "abc", "New Name")
    assert ok is True
    assert items[0]["event_name"] == "New Name"


def test_update_event_not_found_returns_false():
    items = [{"id": "def", "event_name": "Keep"}]
    ok = events.update_event_name(items, "zzz", "New Name")
    assert ok is False
    assert items[0]["event_name"] == "Keep"


# -------------------------------
# delete_event tests
# -------------------------------

def test_delete_event_found_removes_from_list():
    items = [{"id": "abc", "event_name": "ToRemove"}, {"id": "keep", "event_name": "Stay"}]
    ok = events.delete_event(items, "abc")
    assert ok is True
    assert [e["id"] for e in items] == ["keep"]


def test_delete_event_not_found_returns_false_and_keeps_list_intact():
    original = [{"id": "abc"}, {"id": "def"}]
    items = list(original)
    ok = events.delete_event(items, "zzz")
    assert ok is False
    assert items == original

pytest.main([__file__])