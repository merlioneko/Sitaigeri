import tkinter as tk
from tkinter import scrolledtext, ttk


def display_novel_gui(plan: str, novel: str):
    """小説のストーリープランと本文をGUIに表示する。"""
    window = tk.Tk()
    window.title("小説生成結果")
    window.geometry("900x700")

    main_frame = ttk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    notebook = ttk.Notebook(main_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

    plan_frame = ttk.Frame(notebook)
    notebook.add(plan_frame, text="ストーリープラン")
    plan_text = scrolledtext.ScrolledText(plan_frame, wrap=tk.WORD, font=("Arial", 11), bg="white")
    plan_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    plan_text.insert(tk.END, plan)
    plan_text.config(state=tk.DISABLED)

    novel_frame = ttk.Frame(notebook)
    notebook.add(novel_frame, text="小説本文")
    novel_text = scrolledtext.ScrolledText(novel_frame, wrap=tk.WORD, font=("Arial", 11), bg="white")
    novel_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    novel_text.insert(tk.END, novel)
    novel_text.config(state=tk.DISABLED)

    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=10)

    close_btn = ttk.Button(button_frame, text="閉じる", command=window.quit)
    close_btn.pack(side=tk.RIGHT, padx=5)

    window.mainloop()
