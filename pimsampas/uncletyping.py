from tkinter import *
from tkinter import ttk, messagebox
import random
#import wikipedia
import time
import csv
import os
import subprocess


def OpenCSVFolder(event=None):
	dir_path = os.path.dirname(os.path.realpath(__file__))
	path = os.path.realpath(dir_path)
	subprocess.Popen(f'explorer {os.path.realpath(path)}')


sample = ['หมา','กา','ไก่','แมว','ลิง','สิงโต','เป็ด','จิงโจ้']

def writecsv():
	with open('data.csv','w',newline='',encoding='utf-8') as f:
		fw = csv.writer(f)
		for s in sample:
			fw.writerow([s])

allfile = os.listdir()
if 'data.csv' not in allfile:
	writecsv()

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)

	vocab = [d[0] for d in data]
	return vocab

#alltext = wikipedia.summary('python programming')
#alltext = alltext.split()
#alltext = ['หมา','กา','ไก่','แมว','ลิง','สิงโต','เป็ด','จิงโจ้']

alltext = readcsv()

print('Vocab: ',alltext)
print('กด F10 อ่านวิธีเล่นก่อน')

GUI = Tk()
GUI.title('Pimsampas by Uncle Engineer')

#GUI.geometry('700x500')
w = 700
h = 500

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height
#print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y+200:.0f}')
GUI.resizable(0, 0)
label = Label(GUI, font=("Courier", 30, 'bold'), fg='black', bd =30)
label.place(x=20,y=20)
count = 0
alltime = 60
first = True
waiting = True
newgame = False
reset = True
def digitalclock():
	global first
	global count
	global waiting
	global count
	global newgame
	global score
	global reset

	if newgame == False and first == False: 
		count += 1

	if first == False and waiting == True:
		global current
		global corrected
		select = random.choice(alltext)
		v_vocab.set(select)
		corrected = False
		current = select
		waiting = False

	text_input = count
	label.config(text=str(text_input))
	if first == True:
		#print('5 second')
		label.after(5000, digitalclock)
		first = False
	elif newgame == True:
		count = 0
		score = 0
		#print('10 second')
		newgame = False
		label.after(10000, digitalclock)
		#RandomVocab()
	else:
		if reset == True:
			E1.configure(state='enabled')
			E1.focus()
			reset = False
			v_text.set('')
			RandomVocab()

		#print('1 second')
		newgame == False
		label.after(1000, digitalclock)
		if count == alltime:
			count = 0
			if score > 40:
				extratext = 'อะไรจะเทพเบอร์นี้'
			elif score > 20:
				extratext = 'ก็พอได้นะจ๊ะ ขอคะแนนมากกว่านี้อีก'
			else:
				extratext = 'พิมพ์ช้ามากกกกก กลับไปฝึกใหม่ด่วน! 555'
			v_vocab.set('จบเกมนะจ๊ะ\nรอ 10 วินาทีเพื่อเล่นใหม่\nคุณได้ทั้งหมด {} คะแนน!\n{}'.format(score,extratext))
			score = 0
			v_score.set(score)
			newgame = True
			E1.configure(state='disabled')
			reset = True
	

FONT1 = ('Angsana New',30)

L1 = Label(GUI,text='ข้อความ',font=FONT1).pack()

v_vocab = StringVar()
v_vocab.set('เริ่มเกมภายใน 5 วินาที')
L2 = Label(GUI,textvariable=v_vocab,font=FONT1,foreground='green').pack()

v_score = StringVar()
v_score.set(0)
L3 = Label(GUI,textvariable=v_score,font=FONT1).place(x=600,y=10)

v_text = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_text,font=FONT1,width=40)
E1.pack(pady=40)

E1.configure(state='disabled')
global current
current = ''
global corrected
global score
score = 0

def RandomVocab():
	global current
	global corrected
	select = random.choice(alltext)
	v_vocab.set(select)
	corrected = False
	current = select

def CheckTyping(sv):

	global current
	global corrected
	global score
	#print('corrected? ',corrected)
	text = v_text.get()
	#print(text)
	if corrected == True:
		select = random.choice(alltext)
		v_vocab.set(select)
		corrected = False
		current = select

	if corrected == False:
		if text == current:
			corrected = True
			score += 1
			print('You Got 1, All Score: ',score)
			RandomVocab()
			v_text.set('')
			v_score.set(score)

v_text.trace("w", lambda name, index, mode, sv=v_text: CheckTyping(sv))

#

L = Label(GUI,text='กดปุ่ม F10 เพื่อดูวิธีการเล่น').place(x=10,y=470)

v_language = StringVar()
v_language.set('eng')
L = Label(GUI,textvariable=v_language).place(x=650,y=470)



def EngKey(event=None):
	global checkkeyboard
	checkkeyboard = True

	ENG = Toplevel()
	ENG.title('KEYBOARD')
	#ENG.geometry('300x500')
	w = 1130
	h = 300

	ws = ENG.winfo_screenwidth() #screen width
	hs = ENG.winfo_screenheight() #screen height
	#print(ws,hs)

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	ENG.geometry(f'{w}x{h}+{x:.0f}+{y-280:.0f}')
	ENG.resizable(0, 0)

	canvas = Canvas(ENG,width=w,height=h)
	canvas.pack()

	def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

		points = [x1+radius, y1,
				  x1+radius, y1,
				  x2-radius, y1,
				  x2-radius, y1,
				  x2, y1,
				  x2, y1+radius,
				  x2, y1+radius,
				  x2, y2-radius,
				  x2, y2-radius,
				  x2, y2,
				  x2-radius, y2,
				  x2-radius, y2,
				  x1+radius, y2,
				  x1+radius, y2,
				  x1, y2,
				  x1, y2-radius,
				  x1, y2-radius,
				  x1, y1+radius,
				  x1, y1+radius,
				  x1, y1]

		return canvas.create_polygon(points, **kwargs, smooth=True)


	allkey1 ={'`':['`','~','%','_'],
			  '1':['1','!','/','+'],
			  '2':['2','@','ๅ','๑'],
			  '3':['3','#','-','๒'],
			  '4':['4','$','ภ','๓'],
			  '5':['5','%','ถ','๔'],
			  '6':['6','^','ุ','ู'],
			  '7':['7','&','ึ','฿'],
			  '8':['8','*','ค','๕'],
			  '9':['9','(','ต','๖'],
			  '0':['0',')','จ','๗'],
			  '-':['2','_','ข','๘'],
			  '=':['2','+','ช','๙'],
			  'back':[' ',' ',' ',' ']}
			  
	allkey2 ={'tab':[' ',' ',' ',' '],
			  'q':['Q',' ','ๆ','๐'],
			  'w':['W',' ','ไ','"'],
			  'e':['E',' ','ำ','ฎ'],
			  'r':['R',' ','พ','ฑ'],
			  't':['T',' ','ะ','ธ'],
			  'y':['Y',' ','ั','ํ'],
			  'u':['U',' ','ี','๊'],
			  'i':['i',' ','ร','ณ'],
			  'o':['O',' ','น','ฯ'],
			  'p':['P',' ','ย','ญ'],
			  '[':['[','{','บ','ฐ'],
			  ']':[']','}','ล',','],
			  '\\':['\\','|','ฃ','ฅ'],}


	allkey3 ={'Caplock':[' ',' ',' ',' '],
			  'a':['A',' ','ฟ','ฤ'],
			  's':['S',' ','ห','ฆ'],
			  'd':['D',' ','ก','ฏ'],
			  'f':['F',' ','ด','โ'],
			  'g':['G',' ','เ','ฌ'],
			  'h':['H',' ','้','็'],
			  'j':['J',' ','่','๋'],
			  'k':['K',' ','า','ษ'],
			  'l':['L',' ','ส','ศ'],
			  ';':[';',':','ว','ซ'],
			  "'":["'",'"','ง','.']}




	allkey4 ={'Shift':[' ',' ',' ',' '],
			'Shift':[' ',' ',' ',' '],
			  'z':['Z',' ','ผ','('],
			  'x':['X',' ','ป',')'],
			  'c':['C',' ','แ','ฉ'],
			  'v':['V',' ','อ','ฮ'],
			  'b':['B',' ','ิ','ฺ'],
			  'n':['N',' ','ื','์'],
			  'm':['M',' ','ท','?'],
			  ',':[',','<','ม','ฒ'],
			  '.':['.','>','ใ','ฬ'],
			  '/':['/','?','ฝ','ฦ']
			  }

	fg = 'white'
	bg = 'black'


	for i,(j,k,l,m) in enumerate(allkey1.values()):
		my_rectangle = round_rectangle(5 + (i*75), 5, 70 + (i*75), 70, radius=10, fill=bg)
		if v_language.get() == 'eng':
			L = ttk.Label(ENG,text=j,foreground=fg,background=bg,font=(None,15)).place(x=30 + (i*75),y=30)
			L = ttk.Label(ENG,text=k,foreground=fg,background=bg,font=(None,15)).place(x=10 + (i*75),y=10)
		else:
			L = ttk.Label(ENG,text=l,foreground=fg,background=bg,font=(None,15)).place(x=40 + (i*75),y=40)
			L = ttk.Label(ENG,text=m,foreground=fg,background=bg,font=(None,15)).place(x=40 + (i*75),y=10)

	# Backspace
	my_rectangle = round_rectangle(-20 + ((i+1)*75), 5, 75 + ((i+1)*75), 70 ,radius=10, fill=bg)
	L = ttk.Label(ENG,text='BACKSPACE',foreground=fg,background=bg,font=(None,15)).place(x=-65 + ((i+1)*75),y=20)

	# ------------------------------------------------
	for i,(j,k,l,m) in enumerate(allkey2.values()):
		my_rectangle = round_rectangle(40 + (i*75), 80, 105 + (i*75), 145, radius=10, fill=bg)
		if v_language.get() == 'eng':
			L = ttk.Label(ENG,text=j,foreground=fg,background=bg,font=(None,15)).place(x=65 + (i*75),y=105)
			L = ttk.Label(ENG,text=k,foreground=fg,background=bg,font=(None,15)).place(x=45 + (i*75),y=85)
		else:
			L = ttk.Label(ENG,text=l,foreground=fg,background=bg,font=(None,15)).place(x=75 + (i*75),y=115)
			L = ttk.Label(ENG,text=m,foreground=fg,background=bg,font=(None,15)).place(x=75 + (i*75),y=85)

	# Tab
	my_rectangle = round_rectangle( ((i+1)*75), 80, 75 + ((i+1)*75), 145 ,radius=10, fill=bg)
	my_rectangle = round_rectangle(5, 80, 70, 145, radius=10, fill=bg)
	L = ttk.Label(ENG,text='TAB',foreground=fg,background=bg,font=(None,15)).place(x=30,y=100)	

	
	# ------------------------------------------------
	for i,(j,k,l,m) in enumerate(allkey3.values()):
		my_rectangle = round_rectangle(75 + (i*75), 155, 140 + (i*75), 220, radius=10, fill=bg)
		if v_language.get() == 'eng':
			L = ttk.Label(ENG,text=j,foreground=fg,background=bg,font=(None,15)).place(x=100 + (i*75),y=180)
			L = ttk.Label(ENG,text=k,foreground=fg,background=bg,font=(None,15)).place(x=80 + (i*75),y=160)
		else:
			L = ttk.Label(ENG,text=l,foreground=fg,background=bg,font=(None,15)).place(x=110 + (i*75),y=190)
			L = ttk.Label(ENG,text=m,foreground=fg,background=bg,font=(None,15)).place(x=110 + (i*75),y=160)

	my_rectangle = round_rectangle(75 + ((i+1)*75), 155, 225 + ((i+1)*75), 220 ,radius=10, fill=bg)
	L = ttk.Label(ENG,text='ENTER',foreground=fg,background=bg,font=(None,15)).place(x=120 + ((i+1)*75),y=170)

	# Tab
	my_rectangle = round_rectangle(5, 155, 90, 220, radius=10, fill=bg)
	L = ttk.Label(ENG,text='CAPSLOCK',foreground=fg,background=bg,font=(None,15)).place(x=10,y=175)

	# ------------------------------------------------
	for i,(j,k,l,m) in enumerate(allkey4.values()):
		my_rectangle = round_rectangle(110 + (i*75), 230, 175 + (i*75), 295, radius=10, fill=bg)
		if v_language.get() == 'eng':
			L = ttk.Label(ENG,text=j,foreground=fg,background=bg,font=(None,15)).place(x=135 + (i*75),y=255)
			L = ttk.Label(ENG,text=k,foreground=fg,background=bg,font=(None,15)).place(x=115 + (i*75),y=235)
		else:
			L = ttk.Label(ENG,text=l,foreground=fg,background=bg,font=(None,15)).place(x=145 + (i*75),y=265)
			L = ttk.Label(ENG,text=m,foreground=fg,background=bg,font=(None,15)).place(x=145 + (i*75),y=235)

	# Tab
	my_rectangle = round_rectangle(185 + ((i)*75), 230, 375 + ((i)*75), 295 ,radius=10, fill=bg)
	L = ttk.Label(ENG,text='SHIFT',foreground=fg,background=bg,font=(None,15)).place(x=240 + (i*75),y=250)


	my_rectangle = round_rectangle(5, 230, 120, 295, radius=10, fill=bg)
	L = ttk.Label(ENG,text='SHIFT',foreground=fg,background=bg,font=(None,15)).place(x=45,y=250)

	ENG.mainloop()

global language
language = True # Eng = True , Thai = False
checkkeyboard = False

def ChangeLanguage(event=None):
	global language
	language = not language
	if language == True:
		v_language.set('eng')
	else:
		v_language.set('thai')

def KeyEng(event=None):
	global language
	language = False
	ChangeLanguage()
	EngKey()

def KeyThai(event=None):
	global language
	language = True
	ChangeLanguage()
	EngKey()


def ResetGame(event=None):
	global count
	global score
	global newgame
	global reset

	count = 0
	if score > 40:
		extratext = 'อะไรจะเทพเบอร์นี้'
	elif score > 20:
		extratext = 'ก็พอได้นะจ๊ะ ขอคะแนนมากกว่านี้อีก'
	else:
		extratext = 'ยังไม่ทันเล่นเลย หยุดซะแล้ว 555'
	v_vocab.set('จบเกมนะจ๊ะ\nรอ 10 วินาทีเพื่อเล่นใหม่\nคุณได้ทั้งหมด {} คะแนน!\n{}'.format(score,extratext))
	score = 0
	v_score.set(score)
	newgame = True
	E1.configure(state='disabled')
	reset = True

def HelpMenu(event=None):
	GUI2 = Toplevel()
	GUI2.title('วิธีเล่นเกมพิมพ์สัมผัสสไตล์ลุง')
	w = 600
	h = 700

	ws = GUI2.winfo_screenwidth() #screen width
	hs = GUI2.winfo_screenheight() #screen height
	#print(ws,hs)

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	GUI2.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
	#GUI2.resizable(0, 0)

	text = '''โปรแกรมฝึกพิมพ์ "Pimsampas" version 0.1

<<< วิธีเล่น>>>>
- หลังจากเปิดเตรียมตัวพิมพ์ภายใน 5 วินาที
- พิมพ์ตามคำศัพท์สีเขียว พิมพ์ผิดไม่ได้ ต้องพิมพ์ให้ถูกเท่านั้น (ยากไหม 55)
- โปรแกรมจะนับ 1-60 แล้วจะหยุดเกมทันที
- โปรแกรมรอให้ผู้เล่นหยุดหายใจอีก 10 วินาทีแล้วเริ่มใหม่ 555
- ถ้าอยากดูแป้นพิมพ์ภาษาอังกฤษให้กด F1 ภาษาไทยกด F2
- สามารถเพิ่มคำศัพท์ได้ในไฟล์ data.csv ให้กด F5 เพื่อเปิดโฟลเดอร์ที่เก็บไฟล์ CSV
- แก้ไขไฟล์ CSV โดยใช้ Notepad (คลิกขวา Edit) 

(รอลุงอัพเดต version ใหม่จะทำให้ง่ายกว่านี้ 555)

<<< ปุ่มลัดต่างๆ >>>
- กดปุ่ม F1 เพื่อดูคีย์บอร์ดภาษาอังกฤษ 
- กดปุ่ม F2 เพื่อดูคีย์บอร์ดภาษาภาษาไทย
- กดปุ่ม F5 เพื่อเปิดโฟลเดอร์เก็บไฟล์ csv
- กดปุ่ม F10 เพื่อดูวิธีการเล่น
- กดปุ่ม F12 เล่นใหม่

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer

ปล. ขออภัย version 0.1 ลุงใช้เวลาพัฒนาแค่คืนเดียว เลยไม่ได้สมบูรณ์จ้าาาา
'''

	L = ttk.Label(GUI2,text=text,font=('Angsana New',15))
	L.pack(padx=50,pady=50)

	GUI2.mainloop()


GUI.bind('<F1>',KeyEng)
GUI.bind('<F2>',KeyThai)
GUI.bind('<F5>',OpenCSVFolder)
GUI.bind('<F10>',HelpMenu)
GUI.bind('<F12>',ResetGame)
digitalclock()
#messagebox.showinfo('Vocab','คำศัพท์อยู่ในไฟล์ C:\\Python3x\\Lib\\site-packages\\pimsampas\\data.csv')

GUI.mainloop()