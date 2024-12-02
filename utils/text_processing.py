def generate_questions(text, num_questions=5):
    """
    دالة لتوليد الأسئلة باستخدام نموذج خفيف.
    """
    if not text.strip():
        return ["النص المدخل فارغ. يرجى توفير نص مناسب."]
    
    try:
        question_generator = pipeline("text2text-generation", model="t5-small", framework="pt", from_pt=True)
        input_text = f"generate questions: {text}"
        questions = question_generator(input_text, max_length=128, num_return_sequences=num_questions)
        return [q['generated_text'] for q in questions]
    except Exception as e:
        return [f"حدث خطأ أثناء توليد الأسئلة: {str(e)}"]

def summarize_text(text, max_length=150):
    """
    دالة لتلخيص النصوص باستخدام نموذج خفيف.
    """
    if not text.strip():
        return "النص المدخل فارغ. يرجى توفير نص مناسب."
    
    try:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"حدث خطأ أثناء تلخيص النص: {str(e)}"
