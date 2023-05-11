import pytest
from test_code import game_start, signpost

def test_game_start_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "blabla")
    result = game_start()
    assert result == "Invalid Choice"

def test_game_start_play(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "play")
    result = game_start()
    assert result == "Playing Game"

def test_game_start_quit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "quit")
    result = game_start()
    assert result == "System Exit"

def test_signpost_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "blabla")
    result = signpost()
    assert result == "Invalid Choice"

def test_signpost_church(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "church")
    result = signpost()
    assert result == "Church Selected"

def test_signpost_manor(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "manor")
    result = signpost()
    assert result == "Manor Selected"

def test_signpost_dorms(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "dorms")
    result = signpost()
    assert result == "Dorms Selected"

def test_signpost_mess_hall(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "mess hall")
    result = signpost()
    assert result == "Mess Hall Selected"