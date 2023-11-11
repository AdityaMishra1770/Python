import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = None
        self.imgs = []
        for i in range(5):
            img = Image.open(r"C:\Users\Aditya Mishra\OneDrive\Documents\pngtree-banana-yellow-fruit-banana-skewers-png-image_5944324.png")
            img = img.resize((300, 300))
            self.imgs.append(ImageTk.PhotoImage(img))
        
        self.current_index = -1
        self.timer = None
    
    def start(self):
        self.create_ui()
        self.update_image()
        self.start_timer()
        self.root.mainloop()
    
    def create_ui(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

    def update_image(self):
        if self.current_index < len(self.imgs)-1:
            self.current_index += 1
        else:
            self.current_index = 0
        
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, anchor='nw', image=self.imgs[self.current_index])
        self.root.after(2000, self.update_image)

    def start_timer(self):
        self.timer = self.root.after(2000, self.update_image)

if __name__ == '__main__':
    app = App()
    app.start()