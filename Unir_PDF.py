import socket
from tkinter import *
from tkinter import filedialog, ttk, messagebox, simpledialog
import os
from sys import exit
import PyPDF2 as pdf
import datetime as dt
from uuid import getnode as getmac
import getpass
import threading

MacAdd = getmac()
userID = getpass.getuser()
machineID = socket.gethostname()
print(userID)
print(machineID)


month = dt.datetime.now()

filename1 = ''
filename2 = ''
filename3 = ''
filename4 = ''
filename5 = ''

mes = month.month
year = month.year
mesEs = {
    0: 'Diciembre',
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}
serial = {'Vj6k9B52ue',
          'kITXm80yWw',
          'lFKdHw60sA',
          'yq39lqC47e',
          'ppzhwv3xR8',
          'u0fAYnp4aL',
          'EBkz9p3QzC',
          '1KDlH7BOts',
          'oqPHIlSDVA',
          'tbEHmiZQLY'}


fecha = mesEs[mes-1].upper() + ' DE ' + str(year)
folder = 'FACTURAS '+fecha

Xl1 = ''
Xl2 = ''
FACT_DIGITAL = ''
FACT_MUNDO = ''
jpg = ''



def browseFiles1():
    global filename1
    filename1 = filedialog.askdirectory()
    Buscar_Carpeta1.configure(text="Archivo Seleccionado: \n"+filename1)
    global Xl1
    Xl1 = [f for f in os.listdir(filename1) if os.path.isfile(
        os.path.join(filename1, f))]
    print(Xl1)


def browseFiles2():
    global filename2
    filename2 = filedialog.askdirectory()
    Buscar_Carpeta2.configure(text="Archivo Seleccionado: \n"+filename2)
    global Xl2
    Xl2 = [f for f in os.listdir(filename2) if os.path.isfile(
        os.path.join(filename2, f))]
    print(Xl2)


def browseFiles3():
    global filename3
    filename3 = filedialog.askdirectory()
    Buscar_Carpeta3.configure(text="Archivo Seleccionado: \n"+filename3)
    global FACT_DIGITAL
    FACT_DIGITAL = [f for f in os.listdir(filename3) if os.path.isfile(
        os.path.join(filename3, f))]
    print(FACT_DIGITAL)


def browseFiles4():
    global filename4
    filename4 = filedialog.askdirectory()
    Buscar_Carpeta4.configure(text="Archivo Seleccionado: \n"+filename4)
    global FACT_MUNDO
    FACT_MUNDO = [f for f in os.listdir(filename4) if os.path.isfile(
        os.path.join(filename4, f))]
    print(FACT_MUNDO)


def browseFiles5():
    global filename5
    filename5 = filedialog.askdirectory()
    Buscar_Carpeta5.configure(text="Archivo Seleccionado: \n"+filename5)
    global jpg
    jpg = [f for f in os.listdir(filename5) if os.path.isfile(
        os.path.join(filename5, f))]
    print(jpg)



def mezclar():
    
    file_list =[]
    nPdfs = len(jpg)
    nXl = len(Xl1)
    print(nPdfs)
    print(nXl)
    print(Xl1)
    print(Xl2)
    print(FACT_DIGITAL)
    print(FACT_MUNDO)
    print(jpg)
    if os.path.exists(folder):
        print('ya existe')
    else:
        os.mkdir(folder)
    for o in range(nXl):
            pdf_file = open(filename1+'/' + Xl1[o], 'rb')
            read_pdf = pdf.PdfReader(pdf_file)
            number_of_pages = len(read_pdf.pages)
            page = read_pdf.pages[0]
            page_content = page.extract_text()  
            pdf_file.close()
            file_list.append(page_content)
            print(file_list)
            Label_Estado.configure(text='Cargando '+str(o+1)+' de '+str(nPdfs)+' archivos')
    for i in range(nPdfs):
        merger = pdf.PdfMerger()
        abr = jpg[i]
        abr = abr.replace('.pdf', '')
        for j in range(nXl):
            # pdf_file = open(filename1+'/' + Xl1[j], 'rb')
            # read_pdf = pdf.PdfReader(pdf_file)
            # number_of_pages = len(read_pdf.pages)
            # page = read_pdf.pages[0]
            # page_content = page.extract_text()  
            # pdf_file.close()
            if abr in file_list[j]:
                print(abr+' esta en ' + Xl1[j])
                input1 = open(filename5+'/'+jpg[i], 'rb')
                input2 = open(filename1+'/'+Xl1[j], 'rb')
                for x in range(nXl):
                    if Xl1[j] == Xl2[x]:
                        print(Xl1[j]+' es igual a '+Xl2[x])
                        input3 = open(
                            filename2+'/'+Xl2[x], 'rb')
                for y in range(nXl):
                    if Xl1[j] == FACT_DIGITAL[y]:
                        print(Xl1[j]+' es igual a '+FACT_DIGITAL[y])
                        input4 = open(filename3+'/' +
                                      FACT_DIGITAL[y], 'rb')
                for z in range(nXl):
                    
                    if FACT_MUNDO[z].startswith("MR"):
                        if Xl1[j] == FACT_MUNDO[z]:
                            print(Xl1[j]+' es igual a '+FACT_MUNDO[z])
                            input5 = open(filename4+'/' +
                                      FACT_MUNDO[z], 'rb')
                    else:
                        if jpg[i] == FACT_MUNDO[z]:
                            print(jpg[i]+' es igual a '+FACT_MUNDO[z])
                            input5 = open(filename4+'/' +
                                FACT_MUNDO[z], 'rb')
                merger.append(input4)
                merger.append(input5)
                merger.append(input2)
                merger.append(input3)
                merger.append(input1)
                output = open(folder+'/'+Xl1[j], 'wb')
                merger.write(output)
                print('archivo creado')
                merger.close()
                Label_Estado.configure(text='Progreso '+str(i+1)+' de '+str(nPdfs))
    messagebox.showinfo(
        'Importante', 'Los archivos fueron creados exitosamente en '+folder)
    Label_Estado.configure(text=str(nPdfs)+ ' archivos procesados correctamente')
def thread_start():
    t1 = threading.Thread(target=mezclar, name='t1')
    t1.start()


window = Tk()
window.title('Generador de facturas 2.0')
window.config()
window.iconbitmap(r'data/favicon.ico')

img = PhotoImage(file='data/logo1.png')

photolabel = Label(window, image=img)
window.config()
Label_Fecha_actual = Label(
    window, text='Generador de facturas para el mes de '+fecha, width=50, height=4)
Buscar_Carpeta1 = Label(
    window, text="Seleccione la carpeta de procedimientos subsidiados", width=50, height=4, fg="blue")
Buscar_Carpeta2 = Label(
    window, text="Seleccione la carpeta de validaciones", width=50, height=4, fg="blue")
Buscar_Carpeta3 = Label(
    window, text="Seleccione la carpeta de facturas electronica", width=50, height=4, fg="blue")
Buscar_Carpeta4 = Label(
    window, text="Seleccione la carpeta de facturas del sistema o reportes", width=50, height=4, fg="blue")
Buscar_Carpeta5 = Label(
    window, text="Seleccione la carpeta de ordenes escaneadas", width=50, height=4, fg="blue")
Boton_explorar1 = Button(
    window, text='Buscar', command=browseFiles1)
Boton_explorar2 = Button(
    window, text='Buscar', command=browseFiles2)
Boton_explorar3 = Button(
    window, text='Buscar', command=browseFiles3)
Boton_explorar4 = Button(
    window, text='Buscar', command=browseFiles4)
Boton_explorar5 = Button(
    window, text='Buscar', command=browseFiles5)
Boton_mezclar = Button(
    window, text='COMBINAR', command=thread_start
)
Label_Estado = Label(
    window, text='Proceso no iniciado', width=50, height=4
)
Boton_cerrar = Button(
    window, text='SALIR', command=exit
)
Label_Fecha_actual.grid(column=1, row=1)
Buscar_Carpeta1.grid(column=1, row=2)
Boton_explorar1.grid(column=1, row=3)
Buscar_Carpeta2.grid(column=1, row=4)
Boton_explorar2.grid(column=1, row=5)
Buscar_Carpeta3.grid(column=1, row=6)
Boton_explorar3.grid(column=1, row=7)
Buscar_Carpeta4.grid(column=1, row=8)
Boton_explorar4.grid(column=1, row=9)
Buscar_Carpeta5.grid(column=1, row=10)
Boton_explorar5.grid(column=1, row=11, padx=10, pady=10)
Label_Estado.grid(column=1, row=12, padx=10, pady=10)
Boton_mezclar.grid(column=1, row=13, padx=10, pady=10)
Boton_cerrar.grid(column=1, row=14, padx=10, pady=10)
photolabel.grid(column=1, row=15)

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()+100
print(windowHeight, ' ', windowWidth)
positionRight = int(window.winfo_screenwidth()/2 - windowWidth)
positionDown = int(window.winfo_screenheight()/2 - windowHeight)

window.geometry("+{}+{}".format(positionRight, positionDown))
window.mainloop()
