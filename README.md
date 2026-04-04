AutoEIT – Automated Scoring System for Elicited Imitation Task Responses
Overview

AutoEIT is an automated scoring system for the Spanish Elicited Imitation Task (EIT). It replaces manual human evaluation with a deterministic, reproducible, and scalable solution for scoring learner responses.

Abstract

The Spanish Elicited Imitation Task evaluates learners’ implicit grammatical knowledge through sentence reproduction. Traditional scoring depends on human raters, making it time-consuming and inconsistent.

AutoEIT automates this process using rule-based NLP techniques, ensuring transparency, reproducibility, and efficient large-scale processing.

Features
Automated sentence-level scoring
Deterministic and explainable logic
Handles annotations like [pause] and [gibberish]
Batch processing using CSV files
Structured output with score and reason
Exportable results (CSV)
Streamlit-based interface
Installation
1. Clone the repository
git clone https://github.com/your-username/autoeit-prototype.git
cd autoeit-prototype
2. Install dependencies
pip install -r requirements.txt
3. Install spaCy Spanish model (Required)
python -m spacy download es_core_news_lg

Note: The project will not run without installing the spaCy model.

Usage
Run the application
streamlit run app.py
Steps
Upload CSV file
Click submit
View scored output
Download results
Input Format

CSV file must contain:

Stimulus
Transcription Rater 1
Example
Stimulus,Transcription Rater 1
Quiero cortarme el pelo,Quiero cortarme mi pelo
El libro está en la mesa,El libro [pause] está en la mesa
El carro lo tiene Pedro,E-[gibberish] perro
Output Format

The system generates structured output:

ID	Stimulus	Response	Score	Reason
Example Output
1  Quiero cortarme el pelo          Quiero cortarme mi pelo        3  Minor variation (lexical/morphological)
2  El libro está en la mesa         El libro está en la mesa       4  Exact Match
3  El carro lo tiene Pedro          E perro                        1  Major errors / Unintelligible
4  El se ducha cada mañana          El se lucha cada mañana        3  Minor variation (lexical/morphological)
5  ¿Qué dice usted que va a hacer hoy?  ¿Qué que vas estoy?        1  Major errors / Unintelligible
Scoring Logic
4 – Exact Match
3 – Minor variation (lexical/morphological)
2 – Partial response / Significant errors
1 – Major errors / Unintelligible
0 – Non-attempt
Special Handling
[pause] is ignored
[gibberish] is penalized
Project Structure
autoeit-prototype/
│
├── app.py
├── main.py
│
├── content/
│   ├── test.csv
│   └── scored_results.csv
│
├── notebooks/
│   └── prototype.ipynb
│
├── src/
│   ├── engine.py
│   ├── utils.py
│   └── __pycache__/
│
├── scored_output.csv
├── requirements.txt
└── README.md
Tech Stack
Python
Pandas, NumPy
spaCy
python-Levenshtein
Streamlit
Matplotlib, Seaborn
scikit-learn
Future Improvements
Advanced syntactic analysis using dependency parsing
ML-based fallback scoring for ambiguous cases
Support for multiple languages
Performance optimization for large datasets
Author

Second-year undergraduate student in Information Technology with a focus on AI, NLP, and data-driven systems.

License

This project is open-source and available under the MIT License.
