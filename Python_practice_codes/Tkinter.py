import tkinter as tk

window = tk.Tk()                                          
window.title("Tkinter GUI Designing page ~ by pratik farate") 
window.geometry("600x300")             

label=tk.Label(window,text="eneter a text here", font=("Arial",14))        
label.pack(pady=10)

entry=tk.Entry(width=25)
entry.pack(pady=10)
def Show():
 Text_= entry.get()
 result_label.config(text="your entered text is:"+Text_)

button= tk.Button(window,text="click me",command=Show)
button.pack(pady=10)


result_label=tk.Label(window,text="",font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()