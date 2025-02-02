# Shelfside 

Based off of the YouTube Channel: https://www.youtube.com/@Shelfside
Website: https://www.shelfside.co/

Take the Shelfside 10 Board Game Personality quiz: https://shelfside-10-personalities.streamlit.app/

Personality Quiz organization:
```
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── personality-quiz/
│   ├── question_pages*.py
├── data/
│   ├── questions*.txt
├── utils/
│   └── utils.py
```
## Contributing

We welcome contributions that help improve the quiz, whether it's adding new questions, refining the scoring logic, or improving the UI. 

### Getting Started

1. **Fork the Repository**: Click the "Fork" button on the repository's GitHub page.
2. **Clone Your Fork**:  
   ```
   bash
   git clone https://github.com/json-to-string/shelfside-quiz.git
   ```
3. **Create a branch**:
   ```
   git checkout -b feature-name
   ```
4. **Install Dependencies:**
   ```
   python -m venv .venv
   pip install -r requirements.txt
   ```

### Making Changes
- Modifying Questions: Update the question files in data/ or the corresponding logic in personality-quiz/question_pages*.py.
- Adding Utilities: Place helper functions in utils/utils.py.

### Testing
This project uses streamlit, so to view your changes and edits you'll need to run your build locally:
```
streamlit run main.py
```
