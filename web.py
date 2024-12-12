import streamlit as st
from streamlit import session_state
from functions import get_todos,write_todos


todos = get_todos()
def add_todo():
    todo = st.session_state['new_todo']+'\n'
    todos.append(todo)
    write_todos(todos)
st.title("Salam Ali GAAAAAve")
st.subheader("This is my to-do app!")
st.write("This app is to improve your productivity!")
for index,todo in enumerate(todos):
   checkbox = st.checkbox(todo,key=todo)
   if checkbox:
       todos.pop(index)
       write_todos(todos)
       del st.session_state[todo]
       st.rerun()
st.text_input(label="",placeholder="Add a new todo...",on_change=add_todo,key='new_todo')
