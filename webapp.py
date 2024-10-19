import streamlit as st 
import Functions

todos = Functions.Get_TODO("todo.txt")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    
    Functions.Set_TODO("todo.txt",todos)





st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key= todo)
    
    if checkbox:
        todos.pop(checkbox)
        Functions.Set_TODO("todo.txt",todos)
        del st.session_state[todo]
        st.rerun()
    
    
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

