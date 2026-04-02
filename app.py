import streamlit as st
import google.generativeai as gemi

st.title('first web🥇')

Q_A, quizzes, planner = st.tabs(['Q&A','quizzes', 'planner' ])

with Q_A:
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox('choose subject:', options=['math', 'programing', 'english'])
        
        teacher = st.selectbox('choose teacher:', options=['alaa', 'mohamed', 'youssif'])
    with col2:
        place = st.selectbox('choose the place:', options=['obour', 'zamalek', 'Giza'])
        
        number_of_lines = st.selectbox('number of lines:', options=['5', '10', '20 ','30' ])
        what_you_want = st.text_input('enter if you want any thing')
    
    st.divider()
    
    questions = st.chat_input('Enter your question:')
    
    
    if questions:
        with st.chat_message('human', avatar='😁'):
            st.write(questions)
            
        gemini = 'gemini-3.1-flash-lite-preview'
        
        
        gemi.configure(api_key=st.secrets('api'))
        model = gemi.GenerativeModel(model_name=gemini)
        
        with st.chat_message('assistant', avatar='😒'):
            prompt = f'''
            you are an ai assistant who will answer me this questions 
            {questions}
            customize your answer using this info:
            iam talking about {subject} iam in {place}
            you are my teacher who`s name is {teacher}
            i want numbers of lines be equal {number_of_lines}
            and i want you to take this in mind when you write answer {what_you_want}
            '''
            with st.spinner('Generating...🧠'):
                answer = model.generate_content(prompt)
            st.write(answer.text)
            
       
        