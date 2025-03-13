import streamlit as st

# Custom Styling
st.markdown("""
    <style>
        .main { background-color: #f4f4f4; }
        .stButton>button { background-color: #007BFF; color: white; border-radius: 10px; padding: 10px; }
        .stTextInput>div>div>input { border-radius: 10px; }
        .stDataFrame { border-radius: 10px; overflow: hidden; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("📚 Personal Library Manager")

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Add Book", "View Library", "Favorites", "Search Book", "Edit/Delete Books", "Reading Stats", "Reading Planner", "Backup & Restore"])

# Data Storage (Simulated for now)
if "library" not in st.session_state:
    st.session_state.library = []
    st.session_state.favorites = []

# Add Book Section
if menu == "Add Book":
    st.subheader("📖 Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1900, max_value=2100, step=1)
    genre = st.text_input("Genre")
    
    if st.button("➕ Add Book"):
        if title and author:
            book = {"Title": title, "Author": author, "Year": year, "Genre": genre}
            st.session_state.library.append(book)
            st.success(f'Book "{title}" added successfully!')
        else:
            st.warning("Please fill in all required fields.")

# View Library Section
elif menu == "View Library":
    st.subheader("📚 My Library")
    if st.session_state.library:
        for book in st.session_state.library:
            st.write(f"**{book['Title']}** by {book['Author']} ({book['Year']}) - *{book['Genre']}*")
            if st.button(f"🌟 Add to Favorites - {book['Title']}"):
                if book not in st.session_state.favorites:
                    st.session_state.favorites.append(book)
                    st.success(f"Added {book['Title']} to Favorites!")
    else:
        st.info("No books in the library. Add some!")

# Favorites Section
elif menu == "Favorites":
    st.subheader("🌟 Favorite Books")
    if st.session_state.favorites:
        for book in st.session_state.favorites:
            st.write(f"**{book['Title']}** by {book['Author']} ({book['Year']}) - *{book['Genre']}*")
    else:
        st.info("No favorite books yet. Add some!")

# Search Book Section
elif menu == "Search Book":
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("Enter book title or author")
    if search_query:
        results = [book for book in st.session_state.library if search_query.lower() in book["Title"].lower() or search_query.lower() in book["Author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No matching books found.")

# Edit/Delete Books Section
elif menu == "Edit/Delete Books":
    st.subheader("📝 Edit or Delete Books")
    book_titles = [book["Title"] for book in st.session_state.library]
    selected_book = st.selectbox("Select a book to edit/delete", book_titles if book_titles else ["No books available"])
    
    if selected_book and selected_book != "No books available":
        for book in st.session_state.library:
            if book["Title"] == selected_book:
                new_title = st.text_input("New Title", book["Title"])
                new_author = st.text_input("New Author", book["Author"])
                new_year = st.number_input("New Publication Year", min_value=1900, max_value=2100, step=1, value=book["Year"])
                new_genre = st.text_input("New Genre", book["Genre"])
                
                if st.button("✅ Update Book"):
                    book.update({"Title": new_title, "Author": new_author, "Year": new_year, "Genre": new_genre})
                    st.success("Book updated successfully!")
                
                if st.button("❌ Delete Book"):
                    st.session_state.library.remove(book)
                    st.success("Book deleted successfully!")
                break

# Reading Stats Section
elif menu == "Reading Stats":
    st.subheader("📊 Reading Statistics")
    total_books = len(st.session_state.library)
    favorite_books = len(st.session_state.favorites)
    st.write(f"Total Books: **{total_books}**")
    st.write(f"Favorite Books: **{favorite_books}**")

# Reading Planner Section
elif menu == "Reading Planner":
    st.subheader("📅 Reading Planner")
    planner_book = st.text_input("Enter book you plan to read")
    if st.button("📌 Add to Planner"):
        st.session_state.library.append({"Title": planner_book, "Author": "Planned", "Year": "-", "Genre": "-"})
        st.success("Book added to planner!")

# Backup & Restore Section
elif menu == "Backup & Restore":
    st.subheader("☁️ Backup & Restore")
    if st.button("💾 Backup Library"):
        st.download_button(label="Download Backup", data=str(st.session_state.library), file_name="library_backup.txt")
    if st.button("🔄 Restore Library"):
        uploaded_file = st.file_uploader("Upload Backup File", type="txt")
        if uploaded_file:
            st.session_state.library = eval(uploaded_file.getvalue().decode())
            st.success("Library restored successfully!")

# Home Section
else:
    st.write("Welcome to your **Personal Library Manager**! Use the sidebar to navigate.")






    