# 📊 Sentiment Analysis of MBG Policy on X (Twitter)

## 🧠 Overview
This project analyzes public sentiment toward the **Makan Bergizi Gratis (MBG)** policy using data collected from X (Twitter). By applying **Natural Language Processing (NLP)** and machine learning, tweets are classified into **positive, negative, and neutral** sentiments.

This project demonstrates how social media data can be utilized to understand public opinion on government policies.

---

## 🎯 Objectives
- Analyze public opinion on MBG policy  
- Classify tweets into sentiment categories  
- Evaluate machine learning model performance  
- Visualize sentiment distribution  

---

## 🗂️ Dataset
- Source: Scraped from X (Twitter)  
- Total data: **199 tweets**  

### Features:
- `tweet` → raw tweet text  
- `sentiment` → label  
  - 0 = Negative  
  - 1 = Positive  
  - 2 = Neutral  

---

## ⚙️ Methodology

### 🔹 Data Preprocessing
- Lowercasing  
- Remove URLs, mentions, hashtags  
- Remove symbols & numbers  
- Stopword removal (NLTK Indonesian)  
- Stemming using **Sastrawi**

### 🔹 Feature Extraction
- TF-IDF (Term Frequency – Inverse Document Frequency)

### 🔹 Model
- Multinomial Naive Bayes  

### 🔹 Evaluation
- Train-test split (80:20)  
- Metrics:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  

---

## 📈 Results

- **Accuracy: 77.5%**

### 📊 Key Findings
- Model performs well on **negative sentiment**
- Model struggles to detect **neutral sentiment**
- Issue caused by **imbalanced dataset**

---

## 📊 Visualization
- WordCloud (Positive Sentiment)  
- WordCloud (Negative Sentiment)  
- Sentiment Distribution Chart  

---

## 🧠 Insights
- Public sentiment toward MBG is **dominated by negative opinions**
- Dataset imbalance significantly impacts performance  
- Small dataset limits model generalization  

---

## 🚀 Future Improvements
- Increase dataset size (≥ 500 tweets)  
- Balance dataset (SMOTE / undersampling)  
- Try advanced models:
  - Logistic Regression  
  - SVM  
  - IndoBERT  
- Hyperparameter tuning  
- Add confusion matrix visualization  

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  
- Sastrawi  
- Matplotlib  
- WordCloud  



---

## ▶️ How to Run

### 1. Clone Repository
git clone https://github.com/username/mbg-sentiment-analysis.git
cd mbg-sentiment-analysis
### 2. Install Dependencies
pip install pandas numpy scikit-learn nltk sastrawi matplotlib wordcloud
### 3. Run Notebook
jupyter notebook

## 📌 Conclusion

This project shows that sentiment analysis can effectively extract public opinion from social media. While the model achieved 77.5% accuracy, improvements in dataset size and model selection are needed for better performance.

## 👤 Author

Akmal Azamrudi

## ⭐ Support

If you find this project useful, please give it a ⭐ on GitHub!
