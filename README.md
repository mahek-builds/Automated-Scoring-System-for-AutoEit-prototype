AutoEIT – Automated Scoring System for Elicited Imitation Task Responses
Overview

AutoEIT is an automated scoring system for the Spanish Elicited Imitation Task (EIT), designed to replace manual human evaluation with a deterministic, reproducible, and scalable solution.

The system processes transcription data and generates structured scores with explanations, enabling efficient large-scale SLA research.

Abstract

The Spanish EIT evaluates learners’ implicit grammatical knowledge through sentence reproduction tasks. Traditional scoring relies on human raters, making the process time-consuming and inconsistent.

AutoEIT automates this process using rule-based NLP techniques, ensuring transparency and reproducibility while maintaining high agreement with human scoring.

Features
Automated sentence-level scoring
Deterministic and explainable logic
Handles annotations such as [pause] and [gibberish]
Batch processing via CSV upload
Structured output with score and reason
Export results as CSV
Streamlit-based user interface
Input Format

Upload a CSV file with the following columns:

Stimulus
Transcription Rater 1
Example Input
Stimulus,Transcription Rater 1
Quiero cortarme el pelo,Quiero cortarme mi pelo
El libro está en la mesa,El libro [pause] está en la mesa
El carro lo tiene Pedro,E-[gibberish] perro
Output Format

The system generates a structured dataset with the following columns:

ID	Stimulus	Response	Score	Reason
Example Output
1  Quiero cortarme el pelo          Quiero cortarme mi pelo        3  Minor variation (lexical/morphological)
2  El libro está en la mesa         El libro está en la mesa       4  Exact Match
3  El carro lo tiene Pedro          E perro                        1  Major errors / Unintelligible
4  El se ducha cada mañana          El se lucha cada mañana        3  Minor variation (lexical/morphological)
5  ¿Qué dice usted que va a hacer hoy?  ¿Qué que vas estoy?        1  Major errors / Unintelligible
Scoring Logic

The scoring system is based on normalized text comparison and edit-distance metrics:

4 – Exact Match: Response matches stimulus after normalization
3 – Minor variation: Small lexical or morphological differences
2 – Partial response: Significant but incomplete match
1 – Major errors: Unintelligible or heavily distorted response
0 – Non-attempt: No valid response
Special Handling
[pause] → ignored
[gibberish] → automatically penalized
Project Structure
autoeit-prototype/
│
├── app.py                     # Streamlit application
├── main.py                    # Entry script (if used)
│
├── content/                   # Input datasets
│   ├── test.csv
│   └── scored_results.csv
│
├── notebooks/
│   └── prototype.ipynb        # Experimentation and testing
│
├── src/
│   ├── engine.py              # Core scoring logic
│   ├── utils.py               # Helper functions
│   └── __pycache__/
│
├── scored_output.csv          # Generated output file
├── requirements.txt           # Dependencies
└── README.md
Installation
git clone https://github.com/your-username/autoeit-prototype.git
cd autoeit-prototype

pip install -r requirements.txt
python -m spacy download es_core_news_lg
Usage
Run the application
streamlit run app.py
Steps
Upload CSV file
Click submit
View scored output
Download results
Output File

After processing, a file is generated:

scored_output.csv

This file contains all scored responses in structured format.

Tech Stack
Python
Pandas, NumPy
spaCy (Spanish NLP)
Levenshtein distance
Streamlit
scikit-learn (optional validation)
Future Improvements
Syntactic structure matching using dependency parsing
ML-based fallback scoring for ambiguous cases
Support for multiple languages
Advanced analytics dashboard
