import tkinter,tkinter.messagebox
import pygame
import random
  
#warna yang mungkin keluar
warna = ['Merah','Biru','Hijau','Pink','Hitam','Kuning'
         ,'Oren','Putih','Ungu','Coklat','Abu-abu']

#skornya dimulai dari 0
skor = 0

#untuk highscore
highscore=[0]

#waktu permainan
sisa_waktu = 0
  
#fungsi ketika enter
def startGame(Event):
    #definisi nextColour
    warna_berikutnya()
 
def baru():
    global sisa_waktu
    global skor
    skor=0
    sisa_waktu=0
    if sisa_waktu==0:
        sisa_waktu += 31
        waktu_mundur()
    warna_berikutnya()
    bermain() 
    tombol2['state']='normal'
    tombol1['state']='disabled'
    e['state']='normal'

def berhenti():
    global sisa_waktu
    global skor
    global highscore
    sisa_waktu=-1
    Waktu.config(text="Waktu Habis")
    label.config(text="SETOP")
    instruksi.config(text="SKOR KAMU = " + str(skor))
    stop()
    Waktu.after(1000,aktif1)
    tombol2['state']='disabled'
    pygame.mixer.music.pause()
    e.delete(0,tkinter.END)
    e['state']='disabled'
    highscore.append(skor)
    high.config(text="Skor tertinggi = " + str(max(highscore)))

def aktif1():
    tombol1['state']='normal'
  
#fungsi warna berikutnya
def warna_berikutnya():
    #global skor dan sisa_waktu
    global skor
    global sisa_waktu
    
    #Jika sisa_waktu>0
    if sisa_waktu>0:
        
        instruksi.config(text="SEMANGAT! :)",font="Arial 11 bold")#ubah instruksi
        
        if 0<sisa_waktu<30:
            #Jika warna sesuai dengan warna yang ada pada teks
            if e.get().lower() == warna[1].lower(): 
                skor += 1
                instruksi.config(text="BENAR")
                main_lagi()
            else :
                skor -=1
                instruksi.config(text="SALAH")
                salah()
        
        #hapus teks pada boxnya 
        e.delete(0, tkinter.END) 
          
        random.shuffle(warna) 
        
        trans=warna[1]
        if trans=='Hijau':
            trans='Green'
        elif trans=='Biru':
            trans='Blue'
        elif trans=='Merah':
            trans='Red'
        elif trans=='Hitam':
            trans='Black'
        elif trans=='Putih':
            trans='White'
        elif trans=='Pink':
            trans='Pink'
        elif trans=='Kuning':
            trans='Yellow'
        elif trans=='Coklat':
            trans='Brown'
        elif trans=='Oren':
            trans='Orange'
        elif trans=='Ungu':
            trans='Purple'
        elif trans=='Abu-abu':
            trans='Grey'

        label.config(fg = trans, text = warna[0]) #warna dan teksnya
          
        #update skornya 
        skorLabel.config(text = "skor: " + str(skor))
        
        
#fungsi hitung mundurnya
def waktu_mundur(): 
    global sisa_waktu
    global highscore

    #Jika permainan dalam keadaan bermain
    if sisa_waktu > 0: 
  
        #waktu dikurangi -1 
        sisa_waktu -= 1
          
        #update sisa waktunya
        Waktu.config(text = "Sisa Waktu: " + str(sisa_waktu)) 
                                 
        #menjalankan fungsinya lagi jika sudah 1 detik
        Waktu.after(1000, waktu_mundur)
        
    elif sisa_waktu==0:
        Waktu.config(text="Waktu Habis")
        label.config(text="SETOP")
        instruksi.config(text="SKOR KAMU = " + str(skor))
        e.delete(0, tkinter.END) 
        stop()
        Waktu.after(1000,aktif1)
        tombol2['state']='disabled'
        pygame.mixer.music.pause()
        e['state']='disabled'
        highscore.append(skor)
        high.config(text="Skor tertinggi = " + str(max(highscore)))
        
    
def buatMenu():
    menubar = tkinter.Menu(root)
    menusize = tkinter.Menu(root, tearoff=False)
    menusize.add_command(label="Info", command= info)
    menusize.add_separator()
    menusize.add_command(label="Help", command= bantuan)
    menubar.add_cascade(label="Menu", menu=menusize)
    menubar.add_command(label="Keluar", command= keluar)
    root.config(menu=menubar)
 
def bantuan():
    tkinter.messagebox.showinfo("TEST WARNA",'''  KETIK WARNA YANG SESUAI PADA TULISANNYA!\n  \
BUKAN KETIK TULISANNYA. \n 'Merah','Biru','Hijau','Pink','Hitam',\n \
'Kuning','Oren','Putih','Ungu','Coklat','Abu-abu' ''')
    
def keluar():
    answer=tkinter.messagebox.askquestion("Keluar","Apakah anda ingin keluar beneran?",icon='question')
    if answer=='yes':
        root.destroy()
        pygame.mixer.music.pause()
    else :
        tkinter.messagebox.showinfo("NOTIF","Selamat datang kembali",icon='info')
         
def info():
    tkinter.messagebox.showinfo("Creator","Steven,Tassya,Yudha",icon='warning')         
         
#LAGUNYA
def bermain():
    pygame.mixer.music.load('main.wav')
    pygame.mixer.music.play(2)
    
def main_lagi():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('lompat.wav'))

def salah():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('false.wav'))
    
def stop():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('dead.wav'))


#membuat GUI di root (membuka sebuah GUI)
#code ini digunakan untuk memanggil “Tk” dari tkinter yang kemudian di simpan ke dalam variabel “root”
root = tkinter.Tk() 
root.iconbitmap("icon.ico")
root.configure(background="lightblue",relief="raised",bd='25')

#Judul
#myframe = tkinter.Frame(root)
#myframe.master.title("PERMAINAN TEBAK WARNA")
#myframe.pack()
root.title("PERMAINAN TEBAK WARNA") 
  
#UKURAN TAMPILAN
root.geometry("1000x700") 
  
#Batas = tkinter.Frame(root)
#batas.pack()
#batas_atas = tkinter.Label(Frame, bg='blue',width=1000)
#batas_atas.pack(side=tkinter.TOP,fill=tkinter.BOTH)
#ATAU
batas_atas=tkinter.Frame(root,bg='red',width=1000,height=20)
batas_atas.pack(side=tkinter.TOP,fill=tkinter.BOTH)

batas_bawah=tkinter.Frame(root,bg='red',width=1000,height=20)
batas_bawah.pack(side=tkinter.BOTTOM,fill=tkinter.BOTH)

batas_kanan=tkinter.Frame(root,bg='darkred',width=20,height=1000)
batas_kanan.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)

batas_kiri=tkinter.Frame(root,bg='darkred',width=20,height=1000)
batas_kiri.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
  
tkinter.Label(root,text="\n",font="arial 1",bg="lightblue").pack() #JEDA

#label instruksi
instruksi = tkinter.Label(root, text = "Masukan warna yang ada pada tulisan, bukan tulisannya!",
                             font = ('Helvetica', 12, 'bold'),bg="white",relief="sunken",bd='10',width='50',height='2') 
instruksi.pack()  

tkinter.Label(root,text="\n",font="arial 1",bg="lightblue").pack() #JEDA

#highcore
high = tkinter.Label(root, text = "Skor tertinggi = 0",
                          font = (12),bg="white",relief="sunken",bd='8')
high.pack()

tkinter.Label(root,text="\n",font="arial 1",bg="lightblue").pack() #JEDA

#label skor
skorLabel = tkinter.Label(root, text = "Klik Mulai baru untuk bermain!",
                          font = ('Helvetica', 12),bg="white",relief="sunken",bd='8') 
skorLabel.pack()

  
#label sisa waktu
Waktu = tkinter.Label(root, text = "Sisa Waktu: " + str(sisa_waktu),
                          font = ('Helvetica', 12),bg="white",relief="sunken",bd='8')            
Waktu.pack() 
  
tkinter.Label(root,text="\n",font="arial 4",bg="lightblue").pack() #JEDA 
  
#Menampilkan tulisan label warna
label = tkinter.Label(root, text="HALO",font = ('Helvetica', 100),
                      bg="lightgray",relief="ridge",bd='6',height=1,width=10) 
label.pack() #penempatan tulisan label warna

tkinter.Label(root,text="\n",bg="lightblue",).pack() #JEDA

#kotak untuk menulis 
e = tkinter.Entry(root,bg="lightgray") 

e['state']='disabled'

#menjalankan fungsi startgame ketika tombol enter di tekan
root.bind('<Return>', startGame)

e.focus_set()
e.pack() 

tombol1 = tkinter.Button(root, text="Mulai Baru",font="times 14 bold",
                         bg="white",width=10,bd=7,command=baru)
tombol2 = tkinter.Button(root, font="arial 14 bold", text="Stop",
                         bg="white", width=10,state='disabled',bd=7,command=berhenti)
tombol1.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.X)
tombol2.pack(side=tkinter.RIGHT,expand=tkinter.YES,fill=tkinter.X)


pygame.mixer.init(88200)


buatMenu() #membuat menu


#memulai GUI (melooping pada gui tersebut)
root.mainloop()
#code ini digunakan agar windownya tidak langsung close ketika kita jalankan programnya





