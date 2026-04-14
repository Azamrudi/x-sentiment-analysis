📊 Sentiment Analysis of MBG Policy on X (Twitter)
🧠 Overview

This project aims to analyze public sentiment toward the Makan Bergizi Gratis (MBG) policy using data from X (Twitter). By leveraging Natural Language Processing (NLP) and machine learning, this project classifies tweets into positive, negative, and neutral sentiments.

This project demonstrates how social media data can be used to understand public opinion on government policies.

🎯 Objectives
Analyze public opinion on MBG policy
Classify tweets into sentiment categories
Evaluate model performance
Visualize sentiment distribution
🗂️ Dataset
Source: Scraped from X (Twitter)
Total data: 199 tweets
Features:
tweet → raw tweet text
sentiment → label
0 = Negative
1 = Positive
2 = Neutral
⚙️ Methodology
🔹 1. Data Preprocessing
Lowercasing
Remove URL, mentions, hashtags
Remove symbols & numbers
Stopword removal (Indonesian - NLTK)
Stemming (Sastrawi)
🔹 2. Feature Extraction
TF-IDF (Term Frequency – Inverse Document Frequency)
🔹 3. Model
Multinomial Naive Bayes
🔹 4. Evaluation
Train-test split (80:20)
Metrics:
Accuracy
Precision
Recall
F1-score
📈 Results
Metric	Value
Accuracy	77.5%
📊 Classification Summary
Model performs well on negative sentiment
Model fails to detect neutral sentiment
Caused by imbalanced dataset
📊 Visualization
WordCloud (Positive Sentiment)
WordCloud (Negative Sentiment)
Sentiment Distribution Chart
🧠 Key Insights
Public sentiment toward MBG is mostly negative
Dataset imbalance significantly affects performance
Small dataset limits model generalization
🚀 Future Improvements
Add more data (≥ 500 tweets)
Balance dataset (SMOTE / undersampling)
Try advanced models:
Logistic Regression
SVM
IndoBERT (recommended)
Hyperparameter tuning
Add confusion matrix
🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
NLTK
Sastrawi
Matplotlib
WordCloud
📁 Project Structure
mbg-sentiment-analysis/
│
├── data/
│   ├── mbg_labeled.csv
│   ├── mbg_cleaned.csv
│   └── mbg_preprocessed.csv
│
├── notebook/
│   └── sentiment_analysis.ipynb
│
├── results/
│   ├── wordcloud_positive.png
│   ├── wordcloud_negative.png
│   └── sentiment_distribution.png
│
└── README.md
▶️ How to Run
1. Clone Repository
git clone https://github.com/username/mbg-sentiment-analysis.git
cd mbg-sentiment-analysis
2. Install Dependencies
pip install pandas numpy scikit-learn nltk sastrawi matplotlib wordcloud
3. Run Notebook / Script
jupyter notebook
📌 Conclusion

This project shows that sentiment analysis can be used to understand public opinion on social media. Although the model achieved 77.5% accuracy, improvements in data quality and model selection are needed for better performance.

👤 Author

Akmal Azamrudi

⭐ Support

If you like this project, don't forget to give it a ⭐ on GitHub!
