import streamlit as st


# App title and description
st.title("File Creation App")
st.write("This app allows you to create a text file with three sections.")

# Text field for file name
filename = st.text_input("Enter file name:")


original = st.text_area(label="the Original String", value="", height=100, key="original")

# Three horizontal sections with unique keys
sections = [
    {"title": "Draft 1", "text": ""},
    {"title": "Draft 2", "text": ""},
    {"title": "Draft 3", "text": ""},
]

for i, section in enumerate(sections):
    st.write(f"## {section['title']}\n")
    section["text"] = st.text_area("", height=200, key=f"section_text_{i}")  # Unique key added here

# Button to create file
if st.button("Create File"):
    with open(f"{filename}.md", "w", encoding="utf-8") as f:
        f.write(f"# Original\n")
        f.write(f"{original}\n".encode("utf-8").decode())
        for section in sections:
            f.write(f"## {section['title']} \n")
            f.write(f"{section['text']}\n".encode("utf-8").decode())
    st.success("File created successfully!")
    print(f"{sections}")



