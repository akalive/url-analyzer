from tkinter import Tk, Label, Entry, Button, messagebox
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

            # message = "Server: " + resp.headers['server'] + " Last modified: " + resp.headers['last-modified'] + "
            # Content type: " + resp.headers['content-type']
            message = resp.headers
            # print("Content type: " + resp.headers['content-type'])

            label = Label(root, text=message, padx=20, pady=20)
            label.pack()
            messagebox.showinfo(title='Results', message=message)
        except Exception as e:
            print(e)
            messagebox.showerror(title='Error', message='Error occurred')
            root.destroy()


if __name__ == '__main__':
    root = Tk()

    ent = Entry(root)
    ent.pack()

    widget = Button(root, text='Fetch!', command=fetch)
    widget.pack()

    root.mainloop()
