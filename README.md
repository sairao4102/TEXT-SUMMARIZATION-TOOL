# Text Summarization Tool

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: KIRANSAI AREPELLI

**INTERN ID**: C0DF51

**DOMAIN**: Artificial Intelligence Markup Language

**DURATION**: 4 WEEKS

**MENTOR**: NEELA SANTOSH KUMAR

## Description
A web-based tool to summarize large text inputs using abstractive summarization and extract key points.  It leverages advanced Natural Language Processing (NLP) techniques to make long texts more digestible and easily understandable.

## Technologies Used:
- **Flask**: Web framework to create the backend of the application.
- **Python**: Programming language for development.
- **Transformers**: Library for working with pre-trained models, used for abstractive summarization.
- **spaCy**: NLP library used for extracting key points.
- **HTML/CSS**: For frontend UI.
- **JavaScript**: For interactive frontend features.

## Features:
- **Abstractive Summarization**: Generate a concise summary of a given text.
- **Key Point Extraction**: Extract meaningful key points from the summary.
- **File Upload**: Upload a text file to extract the summary and key points.
- **Text Input**: Directly input text for summarization.

## How It Works:
- **User Input**:
Users can either upload a .txt or .pdf file or directly paste large blocks of text into the input field on the website.
- **Text Processing**:
The input text is processed by the backend. If it's a long document, it is split into manageable chunks to ensure the summarization model handles it efficiently.
- **Abstractive Summarization**:
Each chunk of text is passed through a pre-trained transformer model (e.g., T5, BART) using the Hugging Face transformers library. The model generates a concise, human-like summary.
- **Key Point Extraction**:
Using spaCy, the summarized text is further analyzed to extract essential key points. Only meaningful and informative phrases are selected — not just individual words or short noun chunks.
- **Output Display**:
The summarized content and key points are displayed on the webpage for the user to review.
- **Optional Image Generation**:
If enabled, the app can generate an image related to the content using online APIs, based on detected keywords (like places, people, or topics).

##  How to Use

### 1. **Clone the repository**

```bash
git clone [https://github.com/sairao4102/TEXT-SUMMARIZATION-TOOL.git]
cd GPT-TEXT-GENERATOR-TOOL
```

### 2.  Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```
### 3. **Run the application**

```bash
python app.py
```

Access the Application:
Web Interface: Open [http://127.0.0.1:5000] in your browser

# OUTPUT

![Image](https://github.com/user-attachments/assets/90fe170d-8967-41ac-8ced-37c0edc9ccd8)

![Image](https://github.com/user-attachments/assets/fa6a395b-cd0e-4398-a117-94c9b71e85f1)


This project was developed as part of my internship at ** CODTECH IT Solutions** (Task 1). 
