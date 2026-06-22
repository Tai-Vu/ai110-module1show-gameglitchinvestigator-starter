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

- I used GitHub Copilot in the VS Code editor and the assistant to inspect `app.py`, pinpoint the broken logic, and propose concrete code fixes.
- One correct AI suggestion was identifying that the `New Game` button reset only `attempts` and `secret`, while leaving `status`, `score`, and `history` stale. I verified this by reading the updated `app.py` logic and confirming the game now starts fresh when the button is pressed.
- One misleading AI-related suggestion was the emphasis on Streamlit import warnings during `app.py` module loading; those warnings were useful to note but did not indicate a real failure. I verified the result by running the code and seeing that the app imported successfully and the relevant tests still passed.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed when the app no longer stayed stuck in the old game state and a new game could be started successfully with the `New Game` button.
- I ran `python -m pytest` and confirmed `4 passed`, and I also ran the new regression test specifically with `python -m pytest tests/test_game_logic.py -q -k new_game_button_resets_full_state` to make sure the new fix behaved as intended.
- AI helped me design the regression test by suggesting a simulated button press and assertions for full state reset, which made the verification more targeted and reliable.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
