from transformers import pipeline

def generate_questions(text, num_questions=5):
    """
    دالة لتوليد الأسئلة من النصوص باستخدام نموذج توليد النصوص.
    """
    # التحقق من صحة النص المدخل
    if not text.strip():
        return ["النص المدخل فارغ. يرجى توفير نص مناسب."]
    
    try:
        # تحميل النموذج مع التأكد من أنه يدعم PyTorch
        question_generator = pipeline("text2text-generation", model="valhalla/t5-small-qg-prepend", framework="pt", from_pt=True)
        input_text = f"generate questions: {text}"
        
        # توليد الأسئلة
        questions = question_generator(input_text, max_length=512, num_return_sequences=num_questions)
        return [q['generated_text'] for q in questions]
    except Exception as e:
        # معالجة الأخطاء وإرجاع رسالة مناسبة
        return [f"حدث خطأ أثناء توليد الأسئلة: {str(e)}"]

def summarize_text(text, max_length=150):
    """
    دالة لتلخيص النصوص باستخدام نموذج تلخيص النصوص.
    """
    # التحقق من صحة النص المدخل
    if not text.strip():
        return "النص المدخل فارغ. يرجى توفير نص مناسب."
    
    try:
        # تحميل نموذج التلخيص
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
        # تلخيص النصوص
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        # معالجة الأخطاء وإرجاع رسالة مناسبة
        return f"حدث خطأ أثناء تلخيص النص: {str(e)}"
