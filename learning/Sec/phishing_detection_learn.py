# E-posta metnini spam/phishing olasılığına göre değerlendirme
is_phishing = isPhishing.predict(nb_model, email_text)
# E-posta metnini Spacy dokümanına dönüştürme ve vektörize etme
    nlp = spacy.load("en_core_web_sm")
    email_doc = nlp(email_text)
    email_vector = vectorizer.transform([email_doc])
 # Naive Bayes modelini eğitme
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model
