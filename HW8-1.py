import tkinter as tk

def calculate_score():
    score = 0


    if q1_var.get() == "no": score += 1
    if q2_var.get() == "no": score += 1

    #  Q3, Q4
    if q3_var.get() == "yes": score += 1
    if q4_var.get() == "yes": score += 1

    #out
    result_text = f"您的總分為：{score}\n"
    if score >= 3:
        result_text += "健康狀況：健康狀況良好"
    else:
        result_text += "健康狀況：健康狀況不好"

    result_label.config(text=result_text)


root = tk.Tk()
root.title("生活健康狀況問卷")
root.geometry("420x420")

title_label = tk.Label(root, text="生活健康狀況問卷", font=("Arial", 18, "bold"))
title_label.pack(pady=15)

# Q1
frame1 = tk.Frame(root)
frame1.pack(anchor="w", padx=20, pady=5)
tk.Label(frame1, text="1. 是否有抽菸習慣？", font=("Arial", 12)).pack(side=tk.LEFT)

q1_var = tk.StringVar(value="yes")
tk.Radiobutton(frame1, text="是", variable=q1_var, value="yes").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame1, text="否", variable=q1_var, value="no").pack(side=tk.LEFT)

# Q 2 
frame2 = tk.Frame(root)
frame2.pack(anchor="w", padx=20, pady=5)
tk.Label(frame2, text="2. 是否有飲酒習慣？", font=("Arial", 12)).pack(side=tk.LEFT)

q2_var = tk.StringVar(value="yes")  
tk.Radiobutton(frame2, text="是", variable=q2_var, value="yes").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame2, text="否", variable=q2_var, value="no").pack(side=tk.LEFT)

# Q3
frame3 = tk.Frame(root)
frame3.pack(anchor="w", padx=20, pady=5)
tk.Label(frame3, text="3. 每天睡眠時間是否超過六小時？", font=("Arial", 12)).pack(side=tk.LEFT)

q3_var = tk.StringVar(value="yes")  
tk.Radiobutton(frame3, text="是", variable=q3_var, value="yes").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame3, text="否", variable=q3_var, value="no").pack(side=tk.LEFT)

# 4 
frame4 = tk.Frame(root)
frame4.pack(anchor="w", padx=20, pady=5)
tk.Label(frame4, text="4. 是否有均衡飲食？", font=("Arial", 12)).pack(side=tk.LEFT)

q4_var = tk.StringVar(value="yes") 
tk.Radiobutton(frame4, text="是", variable=q4_var, value="yes").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame4, text="否", variable=q4_var, value="no").pack(side=tk.LEFT)

btn = tk.Button(
    root,
    text="送出問卷並查看結果",
    command=calculate_score,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=5
)
btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()
