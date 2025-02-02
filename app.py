import streamlit as st

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'landing'
        st.session_state.progress = 0
        st.session_state.tasks_completed = 0
        st.session_state.task_status = {f"task_{i}": False for i in range(1, 16)}

    if st.session_state.page == 'landing':
        show_landing_page()
    elif st.session_state.page == 'login':
        show_login_page()
    elif st.session_state.page == 'job_selection':
        show_job_selection_page()
    elif st.session_state.page == 'task_overview':
        show_task_overview_page()
    elif st.session_state.page == 'dashboard':
        show_dashboard_page()

# Function to navigate back
def go_back():
    if st.session_state.page == 'login':
        st.session_state.page = 'landing'
    elif st.session_state.page == 'job_selection':
        st.session_state.page = 'login'
    elif st.session_state.page == 'task_overview':
        st.session_state.page = 'job_selection'
    elif st.session_state.page == 'dashboard':
        st.session_state.page = 'task_overview'

# 1️⃣ Landing Page
def show_landing_page():
    st.markdown("""
        <style>
            .stApp {background: linear-gradient(to right, #ff9a9e, #fad0c4);}
            .stTitle {color: white; text-align: center; font-size: 45px; font-weight: bold;}
            .stButton>button {background-color: #28a745; color: white; border-radius: 25px; font-size: 22px; padding: 15px 35px;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='stTitle'>Candidate Hiring Portal</h1>", unsafe_allow_html=True)

    if st.button("Start", key='start', help='Click to Proceed', use_container_width=True):
        st.session_state.page = 'login'

# 2️⃣ Login Page (with dynamic name display while typing)
def show_login_page():
    st.markdown("""
        <style>
            .stTextInput>div>div>input {background-color: white; border-radius: 8px;}
            .stButton>button {background-color: #ff6363; color: white; border-radius: 12px;}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Candidate Login")
    
    # Name fields
    name = st.text_input("Name", key="name_input")
    unique_id = st.text_input("Unique ID")
    password = st.text_input("Password", type="password")
    
    # Displaying text while entering the credentials
    if name:
        st.write(f"Hello {name}, please complete your login.")
    else:
        st.write("Please enter your name to proceed.")
    
    if st.button("Login"):
        if name and unique_id and password:
            st.session_state.page = 'job_selection'
            st.session_state.name = name  # Storing name in session state
            st.session_state.unique_id = unique_id  # Storing unique_id

    # Move back button to top-left
    if st.button("Back", on_click=go_back):  # Add back button
        go_back()

# 3️⃣ Job Selection Page
def show_job_selection_page():
    st.markdown("""
        <style>
            .stSelectbox>div>div>select {background-color: #ffb703; border-radius: 8px;}
            .stButton>button {background-color: #023047; color: white; border-radius: 12px;}
        </style>
    """, unsafe_allow_html=True)

    st.title("Select Your Job Role")
    job_roles = ["Sales", "Account", "Finance", "Operation", "Logistics", "Marketing", "Human Resource"]
    selected_role = st.selectbox("Choose a role", job_roles)

    if st.button("Proceed"):
        st.session_state.page = 'task_overview'

    if st.button("Back", on_click=go_back):  # Add back button
        go_back()

# 4️⃣ Task Overview Page (with structural changes and candidate info)
def show_task_overview_page():
    st.markdown("""
        <style>
            .stButton>button {background-color: #8ecae6; color: black; border-radius: 10px;}
        </style>
    """, unsafe_allow_html=True)

    st.title("Daily Challenges")
    
    # Frame for candidate information
    candidate_info = f"Name: {st.session_state.name} | Unique ID: {st.session_state.unique_id}"
    
    # Current Day Box
    st.sidebar.markdown("### Candidate Info:\n" + candidate_info)
    current_day = st.date_input("Select Today's Date")
    
    # Progress Bar
    st.write("### Progress")
    st.progress(st.session_state.progress)
    
    # Task Challenges Boxes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Day 1 - Day 6")
        for i in range(1, 7):
            if st.button(f"Day {i}"):
                st.session_state.page = 'dashboard'

    with col2:
        st.header("Day 7 - Day 9")
        for i in range(7, 10):
            if st.button(f"Day {i}"):
                st.session_state.page = 'dashboard'

    with col3:
        st.header("Day 10")
        if st.button("Day 10"):
            st.session_state.page = 'dashboard'

    # Move back button to top-left
    if st.button("Back", on_click=go_back):  # Add back button
        go_back()

# 5️⃣ Dashboard Page (with only 3 tasks)
def show_dashboard_page():
    st.markdown("""
        <style>
            .stProgress>div>div>div {background-color: #ffb703;}
            .stCheckbox>div>div>input {accent-color: #219ebc;}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Dashboard - Task Progress")

    # Calculate progress safely
    completed_tasks = sum(st.session_state.task_status.values())
    st.session_state.progress = min(completed_tasks / 3, 1.0)  # Adjusted to 3 tasks
    st.progress(st.session_state.progress)

    st.write("### Tasks To-Do")

    # Creating task boxes for 3 tasks
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Task 1")
    with col2:
        checked = st.checkbox(f"Done 1", key="task_1")
        if checked and not st.session_state.task_status[f"task_1"]:
            st.session_state.task_status[f"task_1"] = True

    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Task 2")
    with col2:
        checked = st.checkbox(f"Done 2", key="task_2")
        if checked and not st.session_state.task_status[f"task_2"]:
            st.session_state.task_status[f"task_2"] = True

    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Task 3")
    with col2:
        checked = st.checkbox(f"Done 3", key="task_3")
        if checked and not st.session_state.task_status[f"task_3"]:
            st.session_state.task_status[f"task_3"] = True

    # Move back button to top-left
    if st.button("Back", on_click=go_back):  # Add back button
        go_back()

if __name__ == "__main__":
    main()
#done
