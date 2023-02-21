# Enron-Email-Classification
Aim: To model an algorithm which can classify emails into six categories based on the content it contains.

Data Preprocessing:
1) The data given is in form of .txt file and its corresponding class in form of .cats file in 8 folders. A loop is run to copy all the content present in the .txt file and its corresponding class to list of lists.
2) A DataFrame is made using the list of lists, some of emails belong to multiple categories as well. Hence such emails are filtered and duplicate data has been added to the dataset.
3) Unwanted data has been removed from the dataframe and only file name, Email body and its Label were retained.
4) Email body must be filtered so that predictions can be better, hence initially, all text data is converted to .lower() format and stopwords, numerics, https, email accounts are removed from the data.
5) Labels which are in float formats are converted to int formats. Any spacing before or after texts are removed.
6) To reduce text complexity, all the words are cut to their base stems using PorterStemmer and final dataset is prepared which contains only file name, from, subject, email body and label.
