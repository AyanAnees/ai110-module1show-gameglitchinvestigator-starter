# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game had a good front end view with clear instructions but the game was not working as intended. The game was certainly showing errors that were required to be corrected. 

- List at least two concrete bugs you noticed at the start  
  The very first bug I observed was that the hint was not correctly giving the right instruction for example, if the number that system guessed is 48, and if I type 47 (the hint would show Go Lower) whereas if I type 49(the hint would show Go Higher). The instructions should've been reversed. Secondly, the range of numbers was not just restricted from 1 to 100 (as the instruction said), instead they included numbers beyond 100 and even negative numbers. Third, as soon as the game ends, the "New Game" button was not resetting the game for which I had to manually refresh the game. Lastly, I observed that the Hint button would count as an attempt. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior                                          | Actual Behavior                                                     | Console Output / Error |
|-------|------------------------------------------------------------|---------------------------------------------------------------------|------------------------|
| | | | |"New Game" button should reset the game                     | The game would not reset                                            | None
| | | | |Numbers go beyond the range instructed (1-100)              | The number should be between (1-100)                                | None
| | | | |Selecting/Unselcting Hint should have no change on attempt  |The attempt was reducing by 1                                        | None
| | | | |Hint should correctly guide.                                |Misleading (Go Higher where it should say Go Lower) and vice - versa | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project, I used Claude. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The only time Claude's suggestion was incorrect was when adding a `key="show_hint"` parameter to fix the hint
checkbox costing an attempt. The actual fix was by moving the checkbox out of the columns layout and separating it from
the submit button logic. I verified by testing that toggling the hint
no longer reduced the attempt counter.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?



---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns are like refreshing a webpage every time you interact with anything. For Example, a button click, a checkbox toggle, even typing in a box. Every time this happens, Python runs your entire app.py file from the top again.

Session state is like a small notebook that Streamlit keeps between these reruns. Without it, every rerun would forget everything like your score, your attempts, your secret number. So st.session_state lets you save values that survive across reruns. 

This is why the hint checkbox was costing an attempt toggling it triggered a rerun, and the attempt counter was incrementing on every rerun instead of only when the Submit button was actually clicked.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit I want to reuse is writing tests that specifically reproduce the bug I just fixed. Instead of generic tests, I wrote test_inverted_hint_bug_fixed() using the exact values from my bug log (guess=72, secret=71). This makes sure the same bug can never keep coming back.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time I work with AI on a coding task, I would read the AI's suggested fix line by line before applying it, instead of accepting it all at once. The AI suggested adding a key parameter to fix the checkbox bug, which was partially wrong — the real fix required restructuring the layout.

- In one or two sentences, describe how this project changed the way you think about AI generated code
This project changed how I think about AI-generated code because it showed me that AI code can look completely reasonable and still have subtle logic bugs that only appear during real use. AI is a strong first draft tool, but human review and testing are what makes the actual difference.
