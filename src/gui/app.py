from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel)
from PySide6.QtCore import Qt
from src.models.solver import Solver
import sys


class ProblemSolverApp:
    def __init__(self, sys_argv=None):
        self.app = QApplication(sys_argv or [])
        self.window = QWidget()
        self.window.setWindowTitle("AI Problem Solver")
        self.layout = QVBoxLayout()

        self.input_label = QLabel("Describe your problem:")
        self.input_text = QTextEdit()
        self.solve_button = QPushButton("Solve")
        self.solve_button.clicked.connect(self.on_solve)

        self.output_label = QLabel("Solution:")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.solve_button)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_text)

        self.window.setLayout(self.layout)

        # Solver instance (loads model if available)
        self.solver = Solver()

    def on_solve(self):
        problem = self.input_text.toPlainText().strip()
        if not problem:
            self.output_text.setPlainText("Please enter a problem description.")
            return
        result = self.solver.solve(problem)
        self.output_text.setPlainText(result)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
