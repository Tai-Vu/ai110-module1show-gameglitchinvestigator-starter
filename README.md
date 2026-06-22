# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is a Streamlit-based number guessing challenge where the player guesses a secret number and receives higher/lower hints until they win or run out of attempts.
- I found that the hint text was reversed for too-high and too-low guesses, which made the game misleading even when the logic worked otherwise.
- I fixed the hint direction in `logic_utils.py` and refactored the shared guess logic into a helper function imported by `app.py`. I also added a regression test in `tests/test_game_logic.py` to verify the corrected hint behavior.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user selects a difficulty level and sees the range and attempt limit for the game.
2. The user enters a guess, such as `40`, and submits it.
3. The game responds with `Too Low` and a hint to go higher if the guess is below the secret number.
4. The user enters another guess, such as `70`, and the game responds with `Too High` and a hint to go lower if the guess is above the secret number.
5. The score updates after each guess based on the outcome and attempt count.
6. The user continues guessing until the correct number is entered, and the game displays a win message with the final score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
