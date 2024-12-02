from transformers import pipeline

def generate_questions(text, num_questions=5):
    # تحقق من النص المدخل
    if not text.strip():
        return ["النص المدخل فارغ. يرجى توفير نص مناسب."]
    
    try:
        # استخدام نموذج مخصص لتوليد الأسئلة
        question_generator = pipeline("text2text-generation", model="valhalla/t5-small-qg-prepend")
        input_text = f"generate questions: {text}"
        questions = question_generator(input_text, max_length=512, num_return_sequences=num_questions)
        return [q['generated_text'] for q in questions]
    except Exception as e:
        return [f"حدث خطأ أثناء توليد الأسئلة: {str(e)}"]

def summarize_text(text, max_length=150):
    # تحقق من النص المدخل
    if not text.strip():
        return "النص المدخل فارغ. يرجى توفير نص مناسب."
    
    try:
        # استخدام ملخص النصوص
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"حدث خطأ أثناء تلخيص النص: {str(e)}"
