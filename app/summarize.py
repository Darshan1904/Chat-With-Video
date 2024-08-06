import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary nltk data files
# nltk.download('punkt')
# nltk.download('stopwords')

def summarize_text(text, num_sentences=5):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    # Create a frequency table to keep the score of each word
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    # Create a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentence_value = dict()
    
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    # Calculate the average score of a sentence
    sum_values = sum(sentence_value.values())
    average = int(sum_values / len(sentence_value))

    # Store the summary sentences
    summary = ''
    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] > (1.2 * average):
            summary += " " + sentence

    # Optionally limit the number of sentences in the summary
    summary_sentences = sent_tokenize(summary)
    if len(summary_sentences) > num_sentences:
        summary = ' '.join(summary_sentences[:num_sentences])

    return summary
