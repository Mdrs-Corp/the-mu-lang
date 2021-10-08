import tkinter as tk
from tkinter.filedialog import asksaveasfile,askopenfilename

pusher={}

def bougerfen(event):
        f.geometry(f'+{int(event.x_root/2)}+{int(event.y_root/2)}')
def grandirfen(event):
	f.geometry(f'{int(event.x_root)}x{int(event.y_root)}')


def bas(touche):
	global pusher
	pusher[touche.keysym]=True
	if (pusher.get('Control_R',0) or pusher.get('Control_L',0)): # Control + ...
		if pusher.get('s'):
			print('save file')
			try:
				file = asksaveasfile(initialfile = 'mmh.txt',
						     defaultextension=".text",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
				file.write(T.get('1.0',"end-1c"))
				file.close()
				f.title(file.name)
				pusher={}
			except FileNotFoundError:
				pusher={}
				pass
				
		elif pusher.get('o'):
			print('open file')
			try:
				file = askopenfilename(filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
				T.insert('1.0', open(file).read())
				f.title(file)
				pusher={}
			except FileNotFoundError:
				pusher={}
				pass
				
def haut(touche):
	global pusher
	pusher[touche.keysym]=False
	if touche.keysym=='Escape':
		f.destroy()
		
pusher={}
form=lambda tup:"#"+str(''.join([format(int(i),'02X') for i in tup]))#créer "#FFFFFF" à partir de (255,255,255)

f=tk.Tk()
f.config(bg='black')
f.title('Nouveau document sans titre tabernak')
f.iconbitmap('icon.ico')
f.geometry('500x500')

T=tk.Text(f,font='Consolas 25',bg='black',fg='#FF0000',cursor='pirate',insertbackground='green',relief='flat',insertwidth=4,insertofftime=600)
T.pack()

tk.Label(f,text='CTRL+S:Sauvegarder CTRL+O:Ouvrir ESC:Fermer',fg='white',bg='black').pack()
f.bind('<B2-Motion>',bougerfen)
f.bind("<KeyPress>",bas)
f.bind("<KeyRelease>",haut)
f.mainloop()
