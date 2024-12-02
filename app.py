import streamlit as st
from utils.text_processing import generate_questions, summarize_text
from utils.learning_model import evaluate_user, create_quiz
from utils.visualization import create_mind_map
from streamlit_chat import message

st.set_page_config(page_title="تطبيق المذاكرة الذكية", layout="wide")

# صفحة البداية
st.title("📘 تطبيق المذاكرة الذكية")
st.sidebar.title("⚙️ الإعدادات")

# تقسيم المنهج إلى مراحل
st.sidebar.subheader("مراحل المنهج")
levels = ["التفكير المنطقي", "المكعبات", "قسم التأسيس", "التناسب الطردي", "التناسب العكسي"]
current_level = st.sidebar.radio("اختر المرحلة", levels)

# تحديد المرحلة الحالية
st.header(f"🌟 أنت الآن في مرحلة: {current_level}")

# رفع الملفات للنصوص
uploaded_file = st.file_uploader("📂 ارفع ملف PDF", type=["pdf"])
if uploaded_file:
    # قراءة النص
    from PyPDF2 import PdfReader
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.success("تم رفع الملف بنجاح!")
    st.write(f"مقتطف من النص:\n{text[:500]}")

    # توليد أسئلة
    if st.button("❓ توليد أسئلة"):
        st.subheader("الأسئلة المولدة")
        questions = generate_questions(text)
        for i, q in enumerate(questions, 1):
            st.write(f"{i}. {q}")

    # تلخيص النصوص
    if st.button("📄 تلخيص النص"):
        st.subheader("الملخص")
        summary = summarize_text(text)
        st.write(summary)

    # الخرائط الذهنية
    if st.button("🧠 إنشاء خريطة ذهنية"):
        st.subheader("الخريطة الذهنية")
        create_mind_map(text)

# إضافة الاختبارات
st.header("📝 اختبار المرحلة الحالية")
if st.button("ابدأ الاختبار"):
    quiz_questions = create_quiz(current_level)
    user_score = evaluate_user(quiz_questions)
    st.write(f"📊 نتيجتك: {user_score} / {len(quiz_questions)}")
    if user_score >= 8:
        st.success("🎉 تهانينا! يمكنك الانتقال إلى المرحلة التالية.")

# واجهة المحادثة
st.sidebar.subheader("💬 تحدث معنا")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    message(msg["text"], is_user=msg["is_user"])

user_input = st.text_input("اكتب رسالتك هنا:")
if user_input:
    st.session_state.messages.append({"text": user_input, "is_user": True})
    st.session_state.messages.append({"text": f"🤖 رد من التطبيق: {user_input}", "is_user": False})
