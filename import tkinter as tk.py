import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("เครื่องคิดเลขและแปลงสกุลเงิน")
        master.configure(bg='Gray')

        self.result_var = tk.StringVar()

        # Entry สำหรับแสดงผลลัพธ์
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=('Helvetica', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=1, column=0, columnspan=4)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('C', 4, 0),
            ('THB to USD', 5, 0),
            ('USD to THB', 5, 1)
        ]

        for (text, row, col) in buttons:
            if text in ['+', '-', '*', '/', '=', 'THB to USD', 'USD to THB', 'C']:
                # ปรับขนาดปุ่มเครื่องหมายให้ใหญ่ขึ้น
                button = tk.Button(button_frame, text=text, padx=30, pady=30, font=('Helvetica', 12), bg='white', fg='black', command=lambda t=text: self.handle_button_click(t))
            else:
                # ปรับขนาดปุ่มตัวเลขให้เล็กลง
                button = tk.Button(button_frame, text=text, padx=20, pady=20, font=('Helvetica', 10), bg='white', fg='black', command=lambda t=text: self.handle_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def handle_button_click(self, value):
        if value == '=':
            self.calculate()
        elif value == 'C':
            self.clear()
        elif value == 'THB to USD':
            self.convert_thb_to_usd()
        elif value == 'USD to THB':
            self.convert_usd_to_thb()
        else:
            self.append_to_expression(value)

    def append_to_expression(self, value):
        current_expression = self.result_var.get()
        new_expression = current_expression + str(value)
        self.result_var.set(new_expression)

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("ข้อผิดพลาด")

    def convert_thb_to_usd(self):
        try:
            amount = float(self.result_var.get())
            exchange_rate = 0.0292  # อัตราแลกเปลี่ยน 1 THB = 0.0292 USD
            result = amount * exchange_rate  # แปลงเงินบาทเป็นดอลลาร์
            self.result_var.set(f"{result:.2f} USD")  # แสดงผลลัพธ์ในรูปแบบดอลลาร์
        except ValueError:
            self.result_var.set("ข้อผิดพลาด")

    def convert_usd_to_thb(self):
        try:
            amount = float(self.result_var.get())
            exchange_rate = 34.5593  # อัตราแลกเปลี่ยน 1 USD = 34.5593 THB
            result = amount * exchange_rate  # แปลงดอลลาร์เป็นเงินบาท
            self.result_var.set(f"{result:.2f} THB")  # แสดงผลลัพธ์ในรูปแบบเงินบาท
        except ValueError:
            self.result_var.set("ข้อผิดพลาด")

    def clear(self):
        self.result_var.set("") # ล้างค่าที่แสดงใน Entry

# สร้างหน้าต่างหลักและเรียกใช้งาน
root = tk.Tk()
calc = Calculator(root)
root.mainloop()