import pandas as pd
import numpy as np
import spacy
import Levenshtein
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import cohen_kappa_score, confusion_matrix
nlp = spacy.load("es_core_news_lg")

class EITScorer:
    def __init__(self):
        self.nlp = nlp

    def normalize(self, text):
        if not isinstance(text, str): return ""
        doc = self.nlp(text.lower())
        return " ".join([token.text for token in doc if not token.is_punct]).strip()

    def get_score(self, stimulus, response):
        target = self.normalize(stimulus)
        learner = self.normalize(response)

        if not learner:
            return 0, "No response"

        if target == learner:
            return 4, "Exact Match"

        t_doc = self.nlp(target)
        l_doc = self.nlp(learner)

        t_lemmas = [t.lemma_ for t in t_doc]
        l_lemmas = [l.lemma_ for l in l_doc]

        ratio = Levenshtein.ratio(target, learner)

        if t_lemmas == l_lemmas:
            return 3, "Morphological variation (Meaning preserved)"
        elif ratio > 0.85:
            return 3, "Minor phonological/spelling error"
        elif ratio > 0.60:
            return 2, "Partial response / Significant errors"
        elif ratio > 0.30:
            return 1, "Major errors / Unintelligible"
        else:
            return 0, "Non-attempt"
# file="C:\Users\bhati\Automated-Scoring-System-for-AutoEit-prototype\autoeit-prototype\content\test.csv"


def run_scoring(file):
   
    file.seek(0)

    try:
        df = pd.read_csv(file)
    except:
        file.seek(0)  
        df = pd.read_csv(file, encoding="latin1")

    stimulus_col = "Stimulus"
    response_col = "Transcription Rater 1"

    if df.empty:
        raise ValueError("CSV file is empty!")

    if stimulus_col not in df.columns or response_col not in df.columns:
        raise ValueError("CSV must contain 'Stimulus' and 'Transcription Rater 1' columns")

    scorer = EITScorer()

    df[["Score", "reason"]] = df.apply(
        lambda row: pd.Series(
            scorer.get_score(row[stimulus_col], row[response_col])
        ),
        axis=1
    )

    return df

# if __name__ == "__main__":
#     file = r"C:/Users/bhati/Automated-Scoring-System-for-AutoEit-prototype/autoeit-prototype/content/test.csv"
#     df=run_scoring(file)
#     print("\n--- Scoring Output ---")
#     print(df.head())

#     # Save file
#     output_file = "scored_output.csv"
#     df.to_csv(output_file, index=False)
#     print(f"\nSaved to {output_file}")

#     #  Plot
#     plt.figure()
#     sns.countplot(x="auto_score", data=df)
#     plt.title("Score Distribution")
#     plt.show()