import tkinter as tk
from tkinter import messagebox, ttk
import db

class BookTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Tracker")
        self.root.geometry("800x600")

        self.selected_book = None

        # Form Fields
        self.title_text = tk.StringVar()
        self.author_text = tk.StringVar()
        self.genre_text = tk.StringVar()
        self.pages_text = tk.StringVar()
        self.status_text = tk.StringVar()

        self.create_widgets()
        self.populate_list()

    def create_widgets():
         