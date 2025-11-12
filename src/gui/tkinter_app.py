"""Tkinter-based GUI (fallback when PySide6 unavailable)."""
import tkinter as tk
from tkinter import scrolledtext, messagebox
from src.models.solver import Solver


class SimpleSolverGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Problem Solver")
        self.window.geometry("600x500")
        self.solver = Solver()

        # Input section
        tk.Label(self.window, text="Describe your problem:", font=("Arial", 12, "bold")).pack(
            padx=10, pady=5, anchor="w"
        )
        self.input_text = scrolledtext.ScrolledText(self.window, height=6, width=70)
        self.input_text.pack(padx=10, pady=5, fill="both", expand=True)

        # Solve button
        tk.Button(
            self.window, text="Solve", command=self.on_solve, bg="#4CAF50", fg="white", font=("Arial", 11)
        ).pack(pady=5)

        # Output section
        tk.Label(self.window, text="Solution:", font=("Arial", 12, "bold")).pack(padx=10, pady=5, anchor="w")
        self.output_text = scrolledtext.ScrolledText(self.window, height=8, width=70, state="disabled")
        self.output_text.pack(padx=10, pady=5, fill="both", expand=True)

    def on_solve(self):
        problem = self.input_text.get("1.0", "end").strip()
        if not problem:
            messagebox.showwarning("Empty Input", "Please enter a problem description.")
            return
        result = self.solver.solve(problem)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)
        self.output_text.config(state="disabled")

    def run(self):
        self.window.mainloop()
