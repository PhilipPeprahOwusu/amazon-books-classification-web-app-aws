
  <h1>Amazon Book Classification Project</h1>
  <p>This project involves classifying book genres based on their summaries. The code and steps below outline the process I followed to accomplish this task.</p>

  <h2>Importing Libraries</h2>
  <p>I imported the necessary libraries and dependencies, including pandas, numpy, seaborn, matplotlib.pyplot, re, nltk, and various classifiers from scikit-learn.</p>

  <h2>Data Preparation and Exploration</h2>
  <p>I read the book summary dataset and performed initial data exploration. I removed unnecessary columns, checked for null values, and visualized the distribution of genres using count plots.</p>

  <h2>Data Cleaning and Preprocessing</h2>
  <p>I applied various text cleaning techniques to the book summaries, including removing special characters, converting text to lowercase, removing stopwords, lemmatizing, and stemming.</p>

  <h2>Encoding Genres</h2>
  <p>I encoded the genres for unique reference using a mapping dictionary. Each genre was assigned a unique numeric label.</p>

  <h2>Model Building</h2>
  <p>I built classification models using both CountVectorizer and TfidfVectorizer to convert text into numerical representations and I trained it with classifiers such as Support Vector Machines (SVM), Multinomial Naive Bayes, and Random Forest.</p>

  <h2>Model Evaluation</h2>
  <p>I evaluated the trained models on the test dataset and calculated accuracy scores for each model.</p>

  <h2>Text Classification</h2>
  <p>I created a function to classify new book summaries using the trained Multinomial Naive Bayes model. This function applied the same cleaning and preprocessing steps to the input text and predicted the genre.</p>

  <h2>Saving the Models</h2>
  <p>I saved the trained Multinomial Naive Bayes model and the TfidfVectorizer model for future use.</p>

  <h2>Conclusion</h2>
  <p>This project demonstrates the process of classifying book genres based on their summaries. By using various text cleaning techniques and machine learning models, we were able to achieve reasonable accuracy in predicting the genres of new books.</p>
