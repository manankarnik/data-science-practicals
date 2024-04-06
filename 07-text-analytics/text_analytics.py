import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models
from nltk.stem import WordNetLemmatizer

# Install necessary packages
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

# Set the working directory
os.chdir("british-fiction-corpus")

# List all text files in the directory
filenames = [file for file in os.listdir() if file.endswith(".txt")]

# Read the contents of each file into a list
filetext = [open(file, "r", encoding="utf-8").read() for file in filenames]

# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(text) if token.isalpha() and token.lower() not in stop_words]

# Apply preprocessing to each document
preprocessed_text = [preprocess_text(text) for text in filetext]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(preprocessed_text)
corpus = [dictionary.doc2bow(text) for text in preprocessed_text]

# Specify the number of topics (k)
k = 3

# Fit Latent Dirichlet Allocation (LDA) model
lda_model = models.LdaModel(corpus, num_topics=k, id2word=dictionary, passes=15)

# Display the topics
print(lda_model.print_topics(num_topics=k, num_words=10))

