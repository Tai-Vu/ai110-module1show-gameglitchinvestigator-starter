# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. Input hints are missaligned. Input 1, says to go lower. Input 100, says to go higher. 
  2. The difficulty ranges do not align with what they are supposed to accomplish. Easy - 1 
  3. The new game button does not work. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 1     | Go Higher!        | Go Lower!       | Input hints are missaligned |
| Normal | Range 1 to 50    | Range 1 to 100  | The range given is incorrect |
| New Game|New Game Created | Nothing Happens | No New Game is Being Created|

---

## 2. How did you use AI as a teammate?

- I used GitHub Copilot in the VS Code editor and the assistant to inspect `app.py`, pinpoint broken logic, and propose concrete code fixes.
- I also used the assistant to help inspect the tests and craft a regression test that would catch the difficulty-switch bug.
- One correct AI suggestion was identifying that the `New Game` button reset only `attempts` and `secret`, while leaving `status`, `score`, and `history` stale. I verified this by reading the updated `app.py` logic and confirming the game now starts fresh when the button is pressed.
- Another correct AI suggestion was that the difficulty range and attempt-limit values in `app.py` should be adjusted to make the levels more sensible. I verified this by reviewing `get_range_for_difficulty()` and `attempt_limit_map` in `app.py`, then confirming the selected difficulty now maps to the expected range and attempts.
- One incorrect/misleading AI-related suggestion was initially focusing on the `logic_utils.py` helper ranges as the only source of the bug. That was misleading because the real issue was in `app.py` state initialization and range text display. I verified the true fix by checking the code path in `app.py` and running tests to confirm the difficulty switch behavior.

---

## 3. Debugging and testing your fixes

- I decided the difficulty bug was fixed when changing difficulty immediately updated the secret range and attempt limit, and the app displayed the correct range text for the selected level.
- I verified my repairs by running `python -m pytest -q` and confirming all tests passed, including the new regression test for difficulty switching and range/attempt updates.
- I also checked the code directly in `app.py` to ensure the `difficulty` session state reset logic, `secret` regeneration, and sidebar captions matched the intended behavior.

---

## 4. What did you learn about Streamlit and state?

- Streamlit reruns the script from top to bottom every time a user interacts with the app, so any values not stored in `st.session_state` are recomputed or reset.
- Session state is the way to preserve important game data across reruns, such as the secret number, the current score, and whether the game is still playing.
- I learned that button clicks and input changes are not like ordinary function calls in a normal app; they cause a fresh execution of the entire script, so state initialization must be guarded carefully.
- That means the correct pattern is to only set default values when a key is missing, and update state explicitly on events like new game or submit.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is writing a regression test for each bug I fix, especially when the bug is subtle, so I can prevent it from coming back later.
- Next time I work with AI on code, I will start by asking it to explain the current behavior and code path before applying fixes, instead of immediately changing the first thing that looks wrong.
- This project taught me that AI-generated code can be a strong starting point, but it still needs careful validation and testing because the AI can introduce logical inconsistencies or hidden bugs.
