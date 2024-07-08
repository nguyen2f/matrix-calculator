# Name: Nguyễn Phúc Nguyên
# Student ID: 20227138
# Class:  150328
# Project: 01 - Thư viện/Tiện ích ma trận
# Date: 10 - 06 - 2024
import tkinter as tk
from tkinter import filedialog, messagebox
import matrixcalculator as mc

class MatrixCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matrix Calculator")
        self.geometry("1000x400")
        self.resizable(0, 0)
        self.canvas = tk.Canvas(self, width=1000, height=400)  
        self.canvas.pack(fill="both", expand=True)
        self.frame = tk.Frame(self.canvas, bg='white', bd=5)
        self.canvas.create_window(500, 200, window=self.frame)
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.frame, text="Matrix Calculator",
                              font=("Times New Roman", 20), bg="white")
        self.label.grid(row=0, columnspan=3, pady=10)
        
        self.input_matrix1_label = tk.Label(self.frame, text="Ma trận 1:",
                                            bg="white")
        self.input_matrix1_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.input_matrix1_text = tk.Text(self.frame, height=10, width=30)
        self.input_matrix1_text.grid(row=2, column=0, padx=5)

        self.input_matrix1_import_button = tk.Button(self.frame, text="File ma trận 1",
                                                     bg="blue", fg="white",
                                                     command=lambda: self.import_matrix(self.input_matrix1_text))
        self.input_matrix1_import_button.grid(row=3, column=0, pady=5)

        self.input_matrix2_label = tk.Label(self.frame, text="Ma trận 2 (nếu thực hiện phép cộng,nhân):",
                                            bg="white")
        self.input_matrix2_label.grid(row=1, column=1, padx=5, pady=5)
        
        self.input_matrix2_text = tk.Text(self.frame, height=10, width=30)
        self.input_matrix2_text.grid(row=2, column=1, padx=5)

        self.input_matrix2_import_button = tk.Button(self.frame, text="File ma trận 2",
                                                     bg="blue", fg="white",
                                                     command=lambda: self.import_matrix(self.input_matrix2_text))
        self.input_matrix2_import_button.grid(row=3, column=1, pady=5)

        self.result_label = tk.Label(self.frame, text="Kết quả:",
                                     bg="white")
        self.result_label.grid(row=1, column=2, padx=5, pady=5)
        
        self.result_text = tk.Text(self.frame, height=10, width=30)
        self.result_text.grid(row=2, column=2, padx=5)

        self.save_button = tk.Button(self.frame, text="Lưu kết quả",
                                     bg="green", fg="white",
                                     command=self.save_result)
        self.save_button.grid(row=3, column=2, pady=5)

        self.operation_frame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window(500, 350, window=self.operation_frame)

        self.add_button = tk.Button(self.operation_frame, text="Cộng 2 ma trận",
                                    bg="orange", fg="black",
                                    command=self.add_matrices)
        self.add_button.grid(row=0, column=0, padx=10)
        
        self.add_button = tk.Button(self.operation_frame, text="Trừ 2 ma trận",
                                    bg="orange", fg="black",
                                    command=self.subtract_matrices)
        self.add_button.grid(row=0, column=1, padx=10)

        self.multiply_button = tk.Button(self.operation_frame, text="Nhân 2 ma trận",
                                         bg="orange", fg="black",
                                         command=self.multiply_matrices)
        self.multiply_button.grid(row=0, column=2, padx=10)

        self.transpose_button = tk.Button(self.operation_frame, text="Ma trận chuyển vị(của ma trận 1)",
                                          bg="orange", fg="black",
                                          command=self.transpose_matrix)
        self.transpose_button.grid(row=0, column=3, padx=10)

        self.inverse_button = tk.Button(self.operation_frame, text="Ma trận nghịch đảo(của ma trận 1)",
                                        bg="orange", fg="black",
                                        command=self.inverse_matrix)
        self.inverse_button.grid(row=0, column=4, padx=10)
    def import_matrix(self, text_widget):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    matrix = []
                    for line in file:
                        row = [float(x) for x in line.split()]
                        matrix.append(row)
                
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, self.matrix_to_string(matrix))
            except Exception as e:
                messagebox.showerror("Đã xảy ra lỗi", f" không thể tải được ma trận: {e}")
    def add_matrices(self):
        matrix1 = self.get_matrix_from_text(self.input_matrix1_text)
        matrix2 = self.get_matrix_from_text(self.input_matrix2_text)
        if matrix1 is None or matrix2 is None:
            return
        try:
            result = mc.add_matrices(matrix1, matrix2)  # Sử dụng hàm tính tổng 2 ma trận trong matrixcalculator.py
            self.display_result(matrix1, matrix2, result)
        except ValueError as e:
            messagebox.showerror("Đã xảy ra lỗi", str(e))
    def subtract_matrices(self):
        matrix1 = self.get_matrix_from_text(self.input_matrix1_text)
        matrix2 = self.get_matrix_from_text(self.input_matrix2_text)
        if matrix1 is None or matrix2 is None:
            return
        try:
            result = mc.subtract_matrices(matrix1, matrix2)  # Use function from matrixcalculator.py
            self.display_result(matrix1, matrix2, result)
        except ValueError as e:
            messagebox.showerror("Đã xảy ra lỗi", str(e))
            
    def multiply_matrices(self):
        matrix1 = self.get_matrix_from_text(self.input_matrix1_text)
        matrix2 = self.get_matrix_from_text(self.input_matrix2_text)
        if matrix1 is None or matrix2 is None:
            return
        try:
            result = mc.multiply_matrices(matrix1, matrix2)  # Use function from matrixcalculator.py
            self.display_result(matrix1, matrix2, result)
        except ValueError as e:
            messagebox.showerror("Đã xảy ra lỗi", str(e))

    def transpose_matrix(self):
        matrix = self.get_matrix_from_text(self.input_matrix1_text)
        if matrix is None:
            return
        try:
            result = mc.transpose_matrix(matrix)  # Use function from matrixcalculator.py
            self.display_result(matrix, None, result)
        except ValueError as e:
            messagebox.showerror("Đã xảy ra lỗi", str(e))

    def inverse_matrix(self):
        matrix = self.get_matrix_from_text(self.input_matrix1_text)
        if matrix is None:
            return
        try:
            result = mc.inverse_matrix(matrix)  # Use function from matrixcalculator.py
            self.display_result(matrix, None, result)
        except ValueError as e:
            messagebox.showerror("Đã xảy ra lỗi", str(e))

    def get_matrix_from_text(self, text_widget):
        text = text_widget.get("1.0", tk.END).strip()
        if not text:
            return None
        try:
            matrix = [[float(num) for num in row.split()] for row in text.split('\n') if row]
            return matrix
        except ValueError:
            messagebox.showerror("Đã xảy ra lỗi", "Ma trận không phù hợp")
            return None

    def display_result(self, matrix1, matrix2, result):
        self.input_matrix1_text.delete("1.0", tk.END)
        self.input_matrix1_text.insert(tk.END, self.matrix_to_string(matrix1))
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, self.matrix_to_string(result))
        if matrix2 is not None:
            self.input_matrix2_text.delete("1.0", tk.END)
            self.input_matrix2_text.insert(tk.END, self.matrix_to_string(matrix2))
        else:
            self.input_matrix2_text.delete("1.0", tk.END)

    def matrix_to_string(self, matrix):
        formatted_matrix = []
        for row in matrix:
            formatted_row = [f"{num:.4f}" for num in row]  #Định dạng float sau dấu chữ 4 chữ số
            formatted_matrix.append(' '.join(formatted_row))
        return '\n'.join(formatted_matrix)

    def save_result(self):
        result_text = self.result_text.get("1.0", tk.END).strip()
        if not result_text:
            messagebox.showerror("Đã xảy ra lỗi", "không thể lưu file kết quả")
            return
        result = [[float(num) for num in row.split()] for row in result_text.split('\n') if row]
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                for row in result:
                    file.write(' '.join(f"{num:.4f}" for num in row) + '\n')
            messagebox.showinfo("Đã lưu", "Kết quả đã được lưu")
            
if __name__ == "__main__":
    app = MatrixCalculatorApp()
    app.mainloop()