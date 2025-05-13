import spacy

# Loading the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Function to extract important key points from the text
def extract_keypoints(text, num_points=5):
    doc = nlp(text)
    sentence_scores = []  # List to store sentence and its score

    # Loop through each sentence in the text
    for sent in doc.sents:
        sent_text = sent.text.strip() 
        if len(sent_text) > 40:  
            score = 0
            # Loop through each word in the sentence
            for token in sent:
                # If the word is a noun, proper noun, or verb increase the score
                if token.pos_ in ["NOUN", "PROPN", "VERB"]:
                    score += 1
            # Save the sentence and its score
            sentence_scores.append((sent_text, score))
    
    # Sort the sentences based on their score in descending order
    sorted_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)

    # Take the top scored sentences as key points
    keypoints = [sent[0] for sent in sorted_sentences[:num_points]]

    return keypoints  # Return the final list of key points
