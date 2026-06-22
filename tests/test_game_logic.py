import importlib
import sys

import streamlit as st

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


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

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
