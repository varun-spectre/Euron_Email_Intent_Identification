# assignment
Spride AI assignment

1st step after preprocessing the text is decide on which vectorizer to use
Here, I used 3 vectorizers
1. TFIDF
2. Infersent
3. Google sentence encoder

Have tried various classifiers in the code above, out of all those SVM and XGBoost gave better results
Max Accuracy obtained is 80.5% with XGBoost classifier

Code with TFIDF- Assignment.ipynb

Code with Infersent- Classification_using_Infersent.ipynb

Code with Google sentece encoder- UniversalSentenceEncoder.ipynb

Confusion matrix and Accuracy score are printed below every classifier


Bonus code- extractor.py
It extracts subject, username and body from .eml files


