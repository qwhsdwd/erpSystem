import tkinter as tk
import tkinter
from tkinter import  messagebox
from main import run

root = tk.Tk()


def message():
    result = run(numberE.get())
    if result:
        messagebox.showinfo("正确提示", "通关号正确")
    else:
        messagebox.showerror("错误提示", "通关号错误")


def center_window():
    w = 350
    h = 100
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window()
numberL = tk.Label(root, text="通关号： ")
numberL.place(x=10, y=20)
numberE = tk.Entry(root)
numberE.place(x=67, y=20)
numberL1 = tk.Label(root, text="剩余查询次数:")
numberL1.place(x=220, y=20)
number = 0
numberL2 = tk.Label(root, text=number)
numberL2.place(x=310, y=20)
buttun = tk.Button(root, text="查询", padx=20, command=message)
buttun.place(x=140, y=65)

root.mainloop()
