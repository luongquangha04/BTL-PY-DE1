import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Tính Đơn Giản")

        # Thiết lập layout với Grid
        # Ô nhập số thứ nhất
        tk.Label(root, text="Số thứ nhất:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry1 = tk.Entry(root, width=10, font=("Arial", 12))
        self.entry1.grid(row=0, column=1, padx=10, pady=5)

        # Ô nhập số thứ hai
        tk.Label(root, text="Số thứ hai:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry2 = tk.Entry(root, width=10, font=("Arial", 12))
        self.entry2.grid(row=1, column=1, padx=10, pady=5)

        # Nhóm Radio buttons cho phép toán
        self.operation = tk.StringVar(value="+")  # Mặc định là cộng
        operations = [("+", "Cộng"), ("-", "Trừ"), ("*", "Nhân"), ("/", "Chia")]
        tk.Label(root, text="Phép toán:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        for i, (op, label) in enumerate(operations):
            tk.Radiobutton(root, text=label, variable=self.operation, value=op, font=("Arial", 12)).grid(row=2, column=i+1, padx=5, pady=5)

        # Nút Tính
        tk.Button(root, text="Tính", command=self.calculate, font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=10)

        # Nút Reset
        tk.Button(root, text="Reset", command=self.reset, font=("Arial", 12)).grid(row=3, column=2, columnspan=2, pady=10)

        # Label hiển thị kết quả
        self.result_label = tk.Label(root, text="Kết quả: ", font=("Arial", 12))
        self.result_label.grid(row=4, column=0, columnspan=4, pady=10)

    def calculate(self):
        try:
            # Lấy giá trị từ ô nhập
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            op = self.operation.get()

            # Thực hiện phép toán
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Không thể chia cho 0")
                result = num1 / num2

            # Hiển thị kết quả
            self.result_label.config(text=f"Kết quả: {result:.2f}")

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
        except ZeroDivisionError as e:
            messagebox.showerror("Lỗi", str(e))

    def reset(self):
        # Xóa ô nhập và đặt lại nhãn kết quả
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.operation.set("+")  # Đặt lại phép toán mặc định
        self.result_label.config(text="Kết quả: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()