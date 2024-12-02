import random
import streamlit as st

def create_quiz(level):
    sample_questions = {
        "التفكير المنطقي": ["ما هو المنطق؟", "كيف تحل مشكلة باستخدام التفكير المنطقي؟"],
        "المكعبات": ["كم عدد المكعبات في هذا الشكل؟", "ما الفرق بين مكعب ومستطيل؟"]
    }
    return random.sample(sample_questions.get(level, []), 2)

def evaluate_user(questions):
    score = 0
    for q in questions:
        user_answer = st.text_input(f"🔸 {q}")
        if user_answer.strip():  # اعتبر أي إجابة صحيحة
            score += 1
    return score
