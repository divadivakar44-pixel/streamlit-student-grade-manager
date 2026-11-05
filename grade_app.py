import streamlit as st

def get_grade(mark):          # paste your Day 2 version here unchanged
    if mark >= 90: return "A"
    elif mark >= 80: return "B"
    elif mark >= 70: return "C"
    elif mark >= 60: return "D"
    else: return "F"

st.title("Student Grade Manager")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add", clear_on_submit=True):
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1)
    if st.form_submit_button("Add"):
        if name.strip():
            st.session_state.students.append(
                {"Name": name.strip(), "Mark": int(mark), "Grade": get_grade(mark)}
            )
            st.success(f"Added {name}")
        else:
            st.error("Please enter a name.")

if st.session_state.students:
    st.table(st.session_state.students)
    marks = [s["Mark"] for s in st.session_state.students]
    average, highest, lowest = sum(marks) / len(marks), max(marks), min(marks)

    st.subheader("Class Performance")
    col1, col2, col3 = st.columns(3)
    col1.metric("Class Average", f"{average:.1f}")
    col2.metric("Highest Mark", highest)
    col3.metric("Lowest Mark", lowest)
else:
    st.info("No students added yet. Add your first student above!")