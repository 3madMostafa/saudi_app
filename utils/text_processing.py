from transformers import pipeline

def generate_questions(text, num_questions=5):
    question_generator = pipeline("question-generation")
    questions = question_generator(text)
    return [q['question'] for q in questions[:num_questions]]

def summarize_text(text, max_length=150):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']
