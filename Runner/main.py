import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
import subprocess
import shutil
import platform
import threading

# COLORES DEL FORMATO:
BACKGROUND = "#0d1117"
PANEL = "#161b22"
BORDER = "#30363d"
TEXT = "#c9d1d9"
MUTED = "#8b949e"
BLUE = "#58a6ff"
GREEN = "#3fb950"
RED = "#f85149"
YELLOW = "#d29922"

# RUTA DE LAS CARPETAS
ROOT_DIR = Path(__file__).resolve().parent.parent  # CARPETA PRINCIPAL
LEETCODE_DIR = ROOT_DIR / "LeetCode"
HACKERRANK_DIR = ROOT_DIR / "HackerRank"
BUILD_DIR = ROOT_DIR / "runner" / ".build"


class ProblemRunner:
    def __init__(self, root):
        self.root = root

        self.root.title("Problemas de Leetcode y Hackerrank")  # TITULO DE LA VENTANA
        self.root.geometry("950x700")  # Width x Height, TAMAÑO DE LA VENTANA
        self.root.minsize(850, 650)

        # ESTADOS DEL SISTEMA
        self.selected_platform = None
        self.selected_difficulty = None
        self.selected_problem = None
        self.selected_language = None
        self.problems = []

        # CONFIGURACION DE LA INTERFAZ
        self.create_interface()

    # CREACION DEL ENTORNO UI
    def create_interface(self):
        # ENCABEZADO: titulo a la izquierda y boton de ejecutar arriba a la derecha
        header_frame = tk.Frame(self.root)
        header_frame.pack(fill="x", padx=25, pady=(20, 5))

        title_box = tk.Frame(header_frame)
        title_box.pack(side="left")

        title = tk.Label(title_box, text="Busca y ejecuta el problema que necesites", fg=BLUE, font=("Times new roman", 14, "bold"))
        title.pack(anchor="w")

        subititle = tk.Label(title_box, text="Ejecutor de problemas de HackerRank y Leetcode", fg=MUTED, font=("Times new roman", 14))
        subititle.pack(anchor="w")

        self.run_button = tk.Button(header_frame, text="EJECUTAR", command=self.run_selected, bg=GREEN,
        activebackground=GREEN, activeforeground=BACKGROUND, font=("Times new roman", 12, "bold"), relief="flat", padx=25, pady=8, cursor="hand2")
        self.run_button.pack(side="right", anchor="ne")

        # ZONA CON SCROLL PARA TODA LA VENTANA
        canvas = tk.Canvas(self.root, borderwidth=0, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True, padx=(25, 0))

        scrollbar_root = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar_root.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar_root.set)

        main_frame = tk.Frame(canvas)
        canvas_window = canvas.create_window((0, 0), window=main_frame, anchor="nw")

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_canvas_configure(event):
            canvas.itemconfig(canvas_window, width=event.width)

        main_frame.bind("<Configure>", on_frame_configure)
        canvas.bind("<Configure>", on_canvas_configure)

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)

        main_frame.pack_propagate(True)

        # SELECCION DE LA PLATAFORMA
        self.create_section_title(main_frame, "PLATFORMA")
        platform_frame = tk.Frame(main_frame)
        platform_frame.pack(fill="x", pady=(5, 15))

        self.leetButton = self.create_button(platform_frame, "LeetCode", self.select_leetcode)
        self.leetButton.pack(side="left", padx=(0, 10))

        self.hacker_button = self.create_button(platform_frame, "HackerRank", self.select_hackerrank)
        self.hacker_button.pack(side="left")

        # SELECCION DE LA DIFICULTAD
        self.create_section_title(main_frame, "DIFICULTAD")
        difficulty_frame = tk.Frame(main_frame)
        difficulty_frame.pack(fill="x", pady=(5, 15))

        self.difficulty_button = {}
        for difficulty in ["Easy", "Medium", "Hard"]:
            button = self.create_button(difficulty_frame, difficulty, lambda d=difficulty: self.select_difficulty(d))
            button.pack(side="left", padx=(0, 10))
            self.difficulty_button[difficulty] = button
            button.config(state="disabled")

        # SELECCION DEL PROBLEMA
        self.create_section_title(main_frame, "PROBLEMAS")
        problem_frame = tk.Frame(main_frame, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
        problem_frame.pack(fill="both", expand=True, pady=(5, 15))
        scrollbar = tk.Scrollbar(problem_frame)
        scrollbar.pack(side="right", fill="y")
        self.problem_list = tk.Listbox(problem_frame, bg=PANEL, fg=TEXT, selectbackground=BLUE, selectforeground=BACKGROUND,
        font=("Times new Roman", 11), borderwidth=0, highlightthickness=0, yscrollcommand=scrollbar.set)
        self.problem_list.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.config(command=self.problem_list.yview)
        self.problem_list.bind("<<ListboxSelect>>", self.problem_selected)

        # SELECCION DEL LENGUAJE
        self.create_section_title(main_frame, "LENGUAJE")
        language_frame = tk.Frame(main_frame)
        language_frame.pack(fill="x", pady=(5, 15))
        self.language_buttons = {}
        for langue in ["C++", "Python", "Java"]:
            button = self.create_button(language_frame, langue, lambda l=langue: self.select_language(l))
            button.pack(side="left", padx=(0, 10))
            self.language_buttons[langue] = button
            button.config(state="disabled")

        # SALIDA
        self.create_section_title(main_frame, "SALIDA")
        output_frame = tk.Frame(main_frame, bg="#010409", highlightbackground=BORDER, highlightthickness=1)
        output_frame.pack(fill="both", expand=True, pady=(5, 15))
        self.output = tk.Text(output_frame, bg="#010409", fg=GREEN, insertbackground=TEXT, font=("Times new Roman", 10), borderwidth=0, highlightthickness=0, wrap="word")
        self.output.pack(fill="both", expand=True, padx=10, pady=10)
        self.output.config(state="disabled")

    ## FUNCIONES DE AYUDA
    def create_section_title(self, parent, text):
        label = tk.Label(parent, text=text, fg=MUTED, font=("Times new roman", 10, "bold"), anchor="w")
        label.pack(fill="x")

    def create_button(self, parent, text, command):
        return tk.Button(parent, text=text, command=command, bd=5, relief="ridge", highlightthickness=3, highlightbackground=PANEL,
        activebackground=BLUE, font=("Times new roman", 10, "bold"), padx=25, pady=7, cursor="hand2")

    def select_leetcode(self):
        self.selected_platform = "LeetCode"
        self.selected_difficulty = None
        self.selected_problem = None
        self.selected_language = None

        for button in self.difficulty_button.values():
            button.config(state="normal")

        self.clear_problem_list()
        self.clear_language_selection()
        self.clear_output()
        self.write_output("> Plataforma seleccionada: LeetCode\n\n")

    def select_hackerrank(self):
        self.selected_platform = "HackerRank"
        self.selected_difficulty = None
        self.selected_problem = None
        self.selected_language = None

        for button in self.difficulty_button.values():
            button.config(state="disabled")

        self.clear_problem_list()
        self.clear_language_selection()
        self.clear_output()
        self.write_output("> Plataforma seleccionada: HackerRank\n\n")

        self.load_hackerrank_problems()

    def select_difficulty(self, difficulty):
        if self.selected_platform != "LeetCode":
            return
        self.selected_difficulty = difficulty
        self.selected_problem = None
        self.selected_language = None
        path = (LEETCODE_DIR / difficulty)
        self.load_problems(path)
        self.clear_language_selection()
        self.clear_output()
        self.write_output(f"> Platform: LeetCode\n"
                          f"> Difficulty: {difficulty}\n\n")

    def load_problems(self, directory):
        self.clear_problem_list()
        self.problems = []
        if not directory.exists():
            self.write_output("> Directory not found:\n"
                             f"> {directory}\n")
            return
        for folder in directory.iterdir():
            if not folder.is_dir():
                continue
            parts = folder.name.split(" ", 1)
            if len(parts) != 2:
                continue
            number = parts[0]
            name = parts[1]
            if not number.isdigit():
                continue
            problem = {
                "number": int(number),
                "name": name,
                "path": folder
            }
            self.problems.append(problem)

        self.problems.sort(key=lambda problem: problem["number"])
        for problem in self.problems:
            text = (f"{problem['number']:<6}"
                    f"{problem['name']}")
            self.problem_list.insert(tk.END, text)

    def load_hackerrank_problems(self):
        self.clear_problem_list()
        self.problems = []
        if not HACKERRANK_DIR.exists():
            self.write_output("> HackerRank directory not found:\n"
                             f"> {HACKERRANK_DIR}\n")
            return
        for folder in HACKERRANK_DIR.rglob("*"):
            if not folder.is_dir():
                continue
            source_files = [file for file in folder.iterdir() if file.suffix in (".cpp", ".py", ".java")]
            if not source_files:
                continue
            problem = {
                "number": len(self.problems) + 1,
                "name": folder.name,
                "path": folder
            }
            self.problems.append(problem)

        for problem in self.problems:
            text = (f"{problem['number']:<6}"
                    f"{problem['name']}")
            self.problem_list.insert(tk.END, text)

    def clear_problem_list(self):
        self.problem_list.delete(0, tk.END)
        self.problems = []

    def clear_language_selection(self):
        self.selected_language = None
        for button in (self.language_buttons.values()):
            button.config(state="disabled")

    def clear_output(self):
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.config(state="disabled")

    def write_output(self, text):
        def update():
            self.output.config(state="normal")
            self.output.insert(tk.END, text)
            self.output.see(tk.END)
            self.output.config(state="disabled")
        self.root.after(0, update)

    def problem_selected(self, event):
        selection = (self.problem_list.curselection())
        if not selection:
            return
        index = selection[0]
        if index >= len(self.problems):
            return
        self.selected_problem = (self.problems[index])
        self.selected_language = None
        self.detect_languages()
        self.clear_output()
        self.write_output("> Problema seleccionado:\n"
                          f"> #{self.selected_problem['number']} "
                          f"{self.selected_problem['name']}\n\n")

    def detect_languages(self):
        for button in (self.language_buttons.values()):
            button.config(state="disabled")
        if not self.selected_problem:
            return
        folder = (self.selected_problem["path"])
        for file in folder.iterdir():
            if file.suffix == ".cpp":
                self.language_buttons["C++"].config(state="normal")
            elif file.suffix == ".java":
                self.language_buttons["Java"].config(state="normal")
            elif file.suffix == ".py":
                self.language_buttons["Python"].config(state="normal")

    def select_language(self, language):
        if not self.selected_problem:
            return
        file = self.find_solution_file(self.selected_problem["path"], language)
        if not file:
            messagebox.showerror("Archivo no encontrado", f"No se encontro una solucion en {language}.")
            return
        self.selected_language = language
        self.clear_output()
        self.write_output(f"> Problema:\n"
                          f"> #{self.selected_problem['number']} "
                          f"{self.selected_problem['name']}\n"
                          f"> Lenguaje: {language}\n"
                          f"> Archivo: {file.name}\n\n")

    def run_selected(self):
        if not self.selected_problem:
            messagebox.showwarning("Problema", "Favor de seleccionar un problema primero")
            return
        if not self.selected_language:
            messagebox.showwarning("Lenguaje", "Favor de seleccionar un lenguaje primero")
            return
        problem = self.selected_problem
        language = self.selected_language
        file = self.find_solution_file(problem["path"], language)
        if not file:
            messagebox.showerror("Error", "No se encontro el archivo de la solucion.")
            return

        self.run_button.config(state="disabled")
        self.clear_output()
        self.write_output(f"> Problema: #{problem['number']} {problem['name']}\n"
                          f"> Lenguaje: {language}\n"
                          f"> Archivo: {file.name}\n\n")

        thread = threading.Thread(target=self.execute_solution, args=(file, language), daemon=True)
        thread.start()

    def execute_solution(self, file, language):
        try:
            if language == "Python":
                self.execute_python(file)
            elif language == "C++":
                self.execute_cpp(file)
            elif language == "Java":
                self.execute_java(file)
        except Exception as error:
            self.write_output("\n> ERROR:\n"
                             f"> {error}\n")
        finally:
            self.root.after(0, self.enable_run_button)

    def execute_python(self, file):
        python = shutil.which("python") or shutil.which("python3")
        if not python:
            self.write_output("> Python no fue encontrado.\n")
            return
        self.write_output("> Ejecutando Python...\n\n")
        process = subprocess.run([python, file.name], cwd=file.parent, capture_output=True, text=True)
        self.show_process_result(process)

    def execute_cpp(self, file):
        compiler = shutil.which("g++")
        if not compiler:
            self.write_output("> g++ no fue encontrado.\n")
            return

        BUILD_DIR.mkdir(parents=True, exist_ok=True)

        if platform.system() == "Windows":
            executable = BUILD_DIR / f"{file.stem}.exe"
        else:
            executable = BUILD_DIR / file.stem

        self.write_output("> Compilando C++...\n")
        compile_process = subprocess.run([compiler, file.name, "-std=c++17", "-o", str(executable)], cwd=file.parent, capture_output=True, text=True)

        if compile_process.returncode != 0:
            self.write_output("\n> La compilacion fallo.\n\n")
            if compile_process.stderr:
                self.write_output(compile_process.stderr)
            return

        self.write_output("> Compilacion exitosa.\n"
                          "> Ejecutando...\n\n")
        process = subprocess.run([str(executable)], cwd=file.parent, capture_output=True, text=True)
        self.show_process_result(process)

    def execute_java(self, file):
        javac = shutil.which("javac")
        java = shutil.which("java")

        if not javac:
            self.write_output("> javac no fue encontrado.\n")
            return
        if not java:
            self.write_output("> java no fue encontrado.\n")
            return

        java_build = BUILD_DIR / "java"
        java_build.mkdir(parents=True, exist_ok=True)

        self.write_output("> Compilando Java...\n")
        compile_process = subprocess.run([javac, "-d", str(java_build), file.name], cwd=file.parent, capture_output=True, text=True)

        if compile_process.returncode != 0:
            self.write_output("\n> La compilacion fallo.\n\n")
            if compile_process.stderr:
                self.write_output(compile_process.stderr)
            return

        class_name = file.stem

        self.write_output("> Compilacion exitosa.\n"
                          "> Ejecutando...\n\n")
        process = subprocess.run([java, "-cp", str(java_build), class_name], cwd=file.parent, capture_output=True, text=True)
        self.show_process_result(process)

    def show_process_result(self, process):
        if process.stdout:
            self.write_output(process.stdout)

        if process.stderr:
            self.write_output("\n[stderr]\n")
            self.write_output(process.stderr)

        self.write_output(f"\n> Proceso finalizado con codigo {process.returncode}\n")

    def enable_run_button(self):
        self.run_button.config(state="normal")

    def find_solution_file(self, folder, language):
        extensions = {"C++": ".cpp",
                      "Java": ".java",
                      "Python": ".py"}
        extension = extensions[language]
        for file in folder.iterdir():
            if file.suffix == extension:
                return file
        return None


def main():
    root = tk.Tk()
    ProblemRunner(root)
    root.mainloop()


if __name__ == "__main__":
    main()