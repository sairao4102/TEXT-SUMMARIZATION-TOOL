from transformers import pipeline

# Creating a summarization pipeline using transformers (PyTorch framework)
summarizer_pipeline = pipeline("summarization", framework="pt")

# Function to generate summary from the input text
def abstractive_summary(text):
    
    input_count = len(text.split())  # length input text
    
    # Setting summary length to about 50% of input length
    max_length = max(input_count, int(input_count * 0.5))  # Maximum length of summary(50% of input length)

    min_length = max(15, int(input_count * 0.25))          # Minimum length of summary(25% of input length)
    # If the input text is too short, return it as is

    # Generating the summary using the pipeline
    summary = summarizer_pipeline(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False  
    )
    
    return summary[0]['summary_text']  # Return only the summary text
