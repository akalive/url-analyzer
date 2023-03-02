from tkinter import Tk, Label, Entry, Button, messagebox, Frame, BOTH, LEFT
import random
import requests
import validators


def fetch():
    try:
        url = (ent.get())
        if not validators.url(url):
            print('Invalid URL. Please enter a valid URL.')
            messagebox.showerror(title='Invalid URL!', message='Invalid URL. Please enter a valid URL.')
    except Exception as e:
        print(e)
        messagebox.showerror(title='Error', message='Error occurred')
        root.destroy()
    else:
        try:
            print(url+" is the url.")
            resp = requests.head(url)

            message = resp.headers
            # print("Content type: " + resp.headers['content-type'])

            label = Label(root, text=message, padx=20, pady=20)
            label.pack()
            # messagebox.showinfo(title='Results', message=message)
        except Exception as e:
            print(e)
            messagebox.showerror(title='Error', message='Error occurred')
            root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('akalive/url-analyzer')
    root.geometry('400x200')
    frame1 = Frame(master=root, width=200, height=100)
    frame1.pack(fill=BOTH, side=LEFT, expand=True)

    label_for_entry = Label(frame1, text='Enter URL', padx=2, pady=2)
    label_for_entry.pack()

    ent = Entry(master=frame1, width=60)
    ent.pack(padx=5, pady=5)

    widget = Button(frame1, text='Analyze!', command=fetch)
    widget.pack()

    root.mainloop()
