import smtplib
import tkinter as tk
def tkinput(text) -> str:
   
    root = tk.Tk()
    question = tk.StringVar()
    tk.Label(root, text=text).pack()
    e = tk.Entry(root, textvariable=question)
    e.pack()
    e.focus()
    e.bind("<Return>", lambda event: root.destroy())
    root.mainloop()
    return question.get()

if __name__ == '__main__':
    host = "smtp.gmail.com"
    mmail = tkinput("De: ")
    hmail = tkinput("Para: ")
    subject = tkinput("Asunto: ")
    text = tkinput("Texto: ")
    server = smtplib.SMTP(host, 587)
    server.ehlo()
    server.starttls()
    password = tkinput("APP Password:")
    server.login(mmail, password)
    server.sendmail(mmail, hmail, text)
    print("Email enviado" +hmail)
    server.quit()
