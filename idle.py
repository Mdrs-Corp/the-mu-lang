import tkinter as tk
from tkinter.filedialog import asksaveasfile,askopenfilename

from shell import shell
pusher={}
KEYWORDS=["yield","make","set","do","?"]
def bougerfen(event):
        f.geometry(f'+{int(event.x_root/2)}+{int(event.y_root/2)}')
def grandirfen(event):
	f.geometry(f'{int(event.x_root)}x{int(event.y_root)}')

def savefile():
    print('save file')
    try:
        file = asksaveasfile(initialfile = 'PROGRAMME_POG.µ',defaultextension=".µ",filetypes=[("All Files","*.*")])
        file.write(T.get('1.0',"end-1c"))
        file.close()
        f.title(file.name)
    except FileNotFoundError:
        pass

        
def openfile():
    print('open file')
    try:
        file = askopenfilename(filetypes=[("All Files","*.*")])
        T.insert('1.0', open(file).read())
        f.title(file)
    except FileNotFoundError:
        pass
   
        
def bas(touche):
    global pusher
    pusher[touche.keysym]=True
    if pusher.get('Control_R') or pusher.get('Control_L'): # Control + ...
        if pusher.get('s'):
            savefile()
        elif pusher.get('o'):
            openfile()
        pusher.clear()
    elif pusher.get('F5'):
        savefile()
        shell(T.get("1.0","end-1c"))
        
        
			
def haut(touche):
    global pusher
    pusher[touche.keysym]=False
    if touche.keysym=='Escape':
        f.destroy()
    text=T.get("1.0","end-1c")
    lignes=text.split("\n")
    for ind,ligne in enumerate(lignes,1):
        mots=ligne.split(" ")
        for mot in mots:
            if mot in KEYWORDS:
                T.tag_add("keywords", f"{ind}.{ligne.find(mot)}", f"{ind}.{ligne.find(mot)+len(mot)}")
    
    
		
pusher={}

f=tk.Tk()
f.config(bg='black')
f.title('Nouveau document sans titre tabernak')
f.geometry('500x500')

T=tk.Text(f,font='Consolas 25',bg='black',fg='white',cursor='pirate',insertbackground='purple',relief='flat',insertwidth=4,insertofftime=600)
T.tag_config("keywords",foreground="red")	
T.pack()

tk.Label(f,text='CTRL+S:Sauvegarder CTRL+O:Ouvrir ESC:Fermer',fg='white',bg='black').pack()
f.bind('<B2-Motion>',bougerfen)
f.bind("<KeyPress>",bas)
f.bind("<KeyRelease>",haut)
f.mainloop()
