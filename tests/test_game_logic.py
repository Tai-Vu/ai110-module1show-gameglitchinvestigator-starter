import importlib
import sys

import streamlit as st

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_hint_messages_match_comparison_direction():
    # Results should give lower hints when guess is too high and higher hints when guess is too low
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert message_high == "📉 Go LOWER!"

    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert message_low == "📈 Go HIGHER!"


def test_new_game_button_resets_full_state(monkeypatch):
    st.session_state.clear()
    st.session_state.secret = 42
    st.session_state.attempts = 5
    st.session_state.score = 55
    st.session_state.status = "won"
    st.session_state.history = [10, 20]

    monkeypatch.setattr(st, "button", lambda label, *args, **kwargs: label == "New Game 🔁")
    monkeypatch.setattr(st, "rerun", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")
    monkeypatch.setattr(st, "columns", lambda n: [type("Column", (), {"__enter__": lambda self: self, "__exit__": lambda self, exc_type, exc, tb: None})() for _ in range(n)])
    monkeypatch.setattr(st.sidebar, "selectbox", lambda *args, **kwargs: "Normal")
    monkeypatch.setattr(st.sidebar, "header", lambda *args, **kwargs: None)
    monkeypatch.setattr(st.sidebar, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "selectbox", lambda *args, **kwargs: "Normal")

    if "app" in sys.modules:
        del sys.modules["app"]

    import app

    assert st.session_state.status == "playing"
    assert st.session_state.score == 0
    assert st.session_state.history == []
    assert st.session_state.attempts == 1
    assert 1 <= st.session_state.secret <= 100


def test_difficulty_switch_resets_game_state(monkeypatch):
    st.session_state.clear()
    st.session_state.difficulty = "Easy"
    st.session_state.secret = 5
    st.session_state.attempts = 4
    st.session_state.score = 30
    st.session_state.status = "lost"
    st.session_state.history = [2, 3, 5]

    monkeypatch.setattr(st.sidebar, "selectbox", lambda *args, **kwargs: "Normal")
    monkeypatch.setattr(st.sidebar, "header", lambda *args, **kwargs: None)
    monkeypatch.setattr(st.sidebar, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "button", lambda label, *args, **kwargs: False)
    monkeypatch.setattr(st, "rerun", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")
    monkeypatch.setattr(st, "columns", lambda n: [type("Column", (), {"__enter__": lambda self: self, "__exit__": lambda self, exc_type, exc, tb: None})() for _ in range(n)])

    if "app" in sys.modules:
        del sys.modules["app"]

    import app

    assert st.session_state.difficulty == "Normal"
    assert st.session_state.status == "playing"
    assert st.session_state.score == 0
    assert st.session_state.history == []
    assert st.session_state.attempts == 1
    assert 1 <= st.session_state.secret <= 50


def test_difficulty_switch_to_hard_updates_range_and_attempts(monkeypatch):
    st.session_state.clear()
    st.session_state.difficulty = "Easy"
    st.session_state.secret = 5
    st.session_state.attempts = 4
    st.session_state.score = 30
    st.session_state.status = "lost"
    st.session_state.history = [2, 3, 5]

    captions = []
    monkeypatch.setattr(st.sidebar, "selectbox", lambda *args, **kwargs: "Hard")
    monkeypatch.setattr(st.sidebar, "header", lambda *args, **kwargs: None)
    monkeypatch.setattr(st.sidebar, "caption", lambda *args, **kwargs: captions.append(args[0] if args else kwargs))
    monkeypatch.setattr(st, "button", lambda label, *args, **kwargs: False)
    monkeypatch.setattr(st, "rerun", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")
    monkeypatch.setattr(st, "columns", lambda n: [type("Column", (), {"__enter__": lambda self: self, "__exit__": lambda self, exc_type, exc, tb: None})() for _ in range(n)])

    if "app" in sys.modules:
        del sys.modules["app"]

    import app

    assert st.session_state.difficulty == "Hard"
    assert st.session_state.status == "playing"
    assert st.session_state.score == 0
    assert st.session_state.history == []
    assert st.session_state.attempts == 1
    assert 1 <= st.session_state.secret <= 100
    assert captions[0] == "Range: 1 to 100"
    assert captions[1] == "Attempts allowed: 5"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
