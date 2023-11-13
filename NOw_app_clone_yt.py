import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
import json
import time
import threading
import subprocess


# ################### resizing image ############
def resize(a):
    from PIL import Image

    # Open an image file
    img = Image.open(a)
    # Specify the new size
    new_size = (26, 22)
    # Resize the image
    img_resized = img.resize(new_size)
    # Save the resized image
    img_resized.save(a)
resize(r"C:\Users\Aditya Mishra\OneDrive\Documents\left-align.png")
resize(r"C:\Users\Aditya Mishra\OneDrive\Documents\align-center.png")
resize(r"C:\Users\Aditya Mishra\OneDrive\Documents\right-align.png")
# --------------------------   endl --------------


main_app = tk.Tk()
main_app.geometry('1240x850')
main_app.title("App_clone_Yt_Harshit-vashisth")


################################## main menu ###############################
main_menu = tk.Menu()
# file icons

new_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\new.png")
open_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\open.png")
save_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\save.png")
save_as_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\save-as.png")
exit_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\exit.png")


# declaring file
file = tk.Menu(main_menu, tearoff=False)




# -----------------endl----------------------
# Edit icons

copy_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\copy.png")
cut_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\cut.png")
paste_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\paste.png")
clear_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\clear.png")
find_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\find.png")



edit = tk.Menu(main_menu, tearoff=False)
#-------------------edit end------------

#===============started view======================
#view icons
toolbar_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\toolbar.png")
status_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\status.png")

view = tk.Menu(main_menu, tearoff=False)
# ------------end------------------

#Color Theme
white_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\white.png")
black_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\black.png")
red_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\red.png")
blue_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\blue.png")


color_theme = tk.Menu(main_menu, tearoff=False)


theme_choice = tk.StringVar()
color_icons = (white_icon, black_icon, red_icon, blue_icon)
color_dict = {
    'White' : ('#000000','#FFFFFF'),
    'Black':('#FFFFFF','#000000'),
    'Red':('#ffffff','#FF7273'),
    'Blue':('#FFFF00','#0000FF')
}


#=========================end --------------------------------





#cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)




# ------------------------------End-----------------------------



################################## toolbar ###############################

tool_bar = ttk.Label(main_app)
tool_bar.pack(side=tk.TOP, fill=tk.X)


######### font box------------------
font_t = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable=font_family, state='readonly')
font_box['values'] = font_t
font_box.current(font_t.index('Calibri'))
font_box.grid(row=0,column=0,padx=5)


############ size box-----
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=14,textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8,800,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

############    Button
#Bold
bold_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\bold.png")
bold_btn=ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#italic
italic_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\italic.png")
italic_btn = ttk.Button(tool_bar,image = italic_icon)
italic_btn.grid(row=0,column=3,padx=2)

#underline
underline_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\underline.png")
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=2)

#font Color btn
font_color_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\font_icon.png")
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=2)

## alignment -left -centre -right
align_left_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\left-align.png")
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=2)

align_center_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\align-center.png")
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=2)


align_right_icon = tk.PhotoImage(file=r"C:\Users\Aditya Mishra\OneDrive\Documents\right-align.png")
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=2)



# ------------------------------End-----------------------------




################################## text editor ###############################

text_editor = tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


#font family and size functionality
current_font_family = 'Calibri'
current_font_size = 12

def change_font(main_app):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(main_app):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))


font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_fontsize)    




# --------------------------button functionakity----

text_property =tk.font.Font(font=text_editor['font'])


#bold button functionality
def change_bold():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == "normal":
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    elif text_property.actual()['weight'] == "bold":
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=change_bold)

# italic button functionality
def change_italic():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == "roman":
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    else:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

italic_btn.configure(command=change_italic)
# underline button functionality
def change_underline():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    else:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)


# ------------font color functionality----------
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
    
    
font_color_btn.configure(command=change_font_color)

# ---------align functionality------------
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_left_btn.configure(command=align_left)
align_center_btn.configure(command=align_center)
align_right_btn.configure(command=align_right)





text_editor.config(font=('Calibri',12))

# ------------------------------End-----------------------------


##################################  main status bar ###############################




status_bar = ttk.Label(main_app,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)
    
      
text_editor.bind("<<Modified>>",changed)

# ------------------------------End-----------------------------




##################################  functionaliy ###############################


# variable url
url = ''

#-----------new file----
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)
    
#-----------open file----
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open (url , 'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))


#----------------- Save File--------------

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding="utf-8")as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
            
#---------------------- Save as functionality-----------------
def saveas_file(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return


def exit_file(event=None):
    global url, text_changed
    try:
        if text_changed:
            nbox = messagebox.askyesnocancel('Warning','Do you want to save the file?')
            if nbox == True :
                if url:
                    content= text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding="utf-8") as fw:
                        fw.write(content)
                        main_app.destroy()
                elif not url:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif nbox == False:
                main_app.destroy()
            else:
                pass
        else:
            main_app.destroy()
    except:
        return
                    
                    
                    
                    
                    
                    
# file commands 
file.add_command(label='New',image=new_icon, compound = tk.LEFT, accelerator = 'Ctrl+N', command=new_file)
file.add_command(label='Open',image=open_icon, compound = tk.LEFT, accelerator = 'Ctrl+O', command=open_file)
file.add_command(label='Save',image=save_icon, compound = tk.LEFT, accelerator = 'Ctrl+S',command=save_file)
file.add_command(label='Save as',image=save_as_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+S',command=saveas_file)
file.add_command(label='Exit',image=exit_icon, compound = tk.LEFT, accelerator = 'Alt+Q',command=exit_file)





#        edit && find functionality
def find_func(event=None):
    
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
                
                
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0, new_content)
    
    
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)
    
    
    ##frame
    find_frame = ttk.Label(find_dialogue)
    find_frame.pack(pady=20)
    
    # label
    find_replace = ttk.Label(find_frame,text='Find/Replace')
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace : ')
    
    # entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)
    
    # button
    find_button = ttk.Button(find_frame,text="Find", command = find)
    replace_button = ttk.Button(find_frame,text="Replace", command=replace)
    
    # label grid
    find_replace.grid(row=0,column=1,padx=8, pady=4)
    text_find_label.grid(row=1,column=0,padx=4, pady=4)
    text_replace_label.grid(row=2,column=0,padx=4, pady=4)

    # entry grid
    find_input.grid(row=1,column=1, padx=4, pady=4)
    replace_input.grid(row=2,column=1, padx=4, pady=4)
    
    # button grid
    find_button.grid(row=3,column=0, padx=8, pady=4)
    replace_button.grid(row=3,column=1, padx=8, pady=4)
    
    find_dialogue.mainloop()

# edit commands 
edit.add_command(label='Cut',image=cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X', command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Copy',image=copy_icon, compound = tk.LEFT, accelerator = 'Ctrl+C', command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste_icon, compound = tk.LEFT, accelerator = 'Ctrl+V', command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Find',image=find_icon, compound = tk.LEFT, accelerator = 'Ctrl+F',command=find_func)
edit.add_command(label='Clear',image=clear_icon, compound = tk.LEFT, accelerator = 'Alt+X',command= lambda:text_editor.delete(1.0,tk.END))



#view commands

show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)

def hide_toolbar(event=None):
    global show_tool_bar
    if show_tool_bar:
        tool_bar.forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar = True


def hide_statusbar(event=None):
    global show_status_bar
    if show_status_bar:
        status_bar.forget()
        show_status_bar = False
    else:
        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        show_status_bar = True

view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=show_tool_bar,image=toolbar_icon, compound=tk.LEFT, accelerator='Ctrl+T',command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_status_bar,image=status_icon, compound=tk.LEFT, accelerator='Ctrl+H',command=hide_statusbar)



#color command choice
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image = color_icons[count],variable=theme_choice, compound=tk.LEFT,command=change_theme)
    count +=1
# ------------------------------End-----------------------------


main_app.config(menu=main_menu)

#############  Binding short-cut keys---------
# file func--------
main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Alt-s>",saveas_file)
main_app.bind("<Alt-q>",exit_file)

#Edit command
def delto(event=None):
    text_editor.delete(1.0,tk.END)

main_app.bind("<Control-f>",find_func)
main_app.bind("<Alt-x>",delto)

#view command
main_app.bind("<Control-t>",hide_toolbar)
main_app.bind("<Control-h>",hide_statusbar)

main_app.mainloop()