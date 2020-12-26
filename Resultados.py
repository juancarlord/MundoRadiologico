import os
import PIL
from datetime import datetime, timedelta
from fpdf import FPDF
import tkinter as tk
import barcode
from barcode import Code128
from barcode.writer import ImageWriter
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
class Application(ttk.Frame):
    

    def __init__(self, main_window):
        PIL.ImageFont

        #Dias de la semana
        days = {
            'Monday' : 'Lunes',
            'Tuesday' : 'Martes',
            'Wednesday' : 'Miercoles',
            'Thursday' : 'Jueves',
            'Friday' : 'Viernes'
        }

    #Diccionario de estudio que puede ser usado para versiones futuras
        estudios = {
            '870001' : 'RX DE CRÁNEO SIMPLE',
            '870003' : 'RX DE BASE DE CRANEO',
            '870004' : 'RX DE SILLA TURCA',
            '870005' : 'RX DE MASTOIDES COMPARATIVAS',
            '870006' : 'RX DE PEÑASCOS',
            '870007' : 'RX DE CONDUCTO AUDITIVO INTERNO',
            '870101' : 'RX DE CARA (PERFILOGRAMA)',
            '870102' : 'RX DE ÓRBITAS',
            '870103' : 'RX DE AGUJEROS ÓPTICOS',
            '870104' : 'RX DE MALAR',
            '870105' : 'RX DE ARCO CIGOMATICO',
            '870107' : 'RX DE HUESOS NASALES',
            '870108' : 'RX DE SENOS PARANASALES',
            '870112' : 'RX DE MAXILAR SUPERIOR',
            '870113' : 'RX DE MAXILAR INFERIOR',
            '870131' : 'RX DE ARTICULACIÓN TEMPOROMAXILAR [ATM]',
            '870601' : 'RX DE TEJIDOS BLANDOS DE CUELLO',
            '870602' : 'RX DE CAVUM FARÍNGEO',
            '871010' : 'RX DE COLUMNA CERVICAL',
            '871019' : 'RX DE COLUMNA UNIÓN CERVICO DORSAL',
            '871020' : 'RX DE COLUMNA TORÁCICA',
            '871040' : 'RX DE COLUMNA LUMBOSACRA',
            '871050' : 'RX DE SACRO CÓCCIX',
            '871062' : 'RX DE PANORAMICA DE COLUMNA (GONIOMETRIA U ORTOGRAMA NIÑOS)',
            '871070' : 'RX DINÁMICA DE COLUMNA VERTEBRAL',
            '871060' : 'RX DE COLUMNA VERTEBRAL TOTAL (TEST DE ESCOLIOSIS)',
            '871091' : 'RX DE ARTICULACIONES  SACROILIACAS',
            '871111' : 'RX DE REJA COSTAL',
            '871112' : 'RX DE ESTERNÓN',
            '871121' : 'RX DE TÓRAX',
            '871129' : 'RX DE ARTICULACIONES ESTERNOCLAVICULARES',
            '872002' : 'RX DE ABDOMEN SIMPLE',
            '872011' : 'RX DE ABDOMEN SIMPLE CON PROYECCIONES ADICIONALES',
            '872104' : 'RX DE COLON POR ENEMA O COLON POR INGESTA',
            '872105' : 'RX DE COLON POR ENEMA CON DOBLE CONTRASTE',
            '873002' : 'RX DE HUESOS LARGOS SERIE COMPLETA',
            '873004' : 'RX PARA DETECTAR EDAD OSEA',
            '873111' : 'RX DE OMOPLATO',
            '873112' : 'RX DE CLAVICULA',
            '873121' : 'RX DE HUMERO',
            '873122' : 'RX DE ANTEBRAZO',
            '873123' : 'RX COMPARATIVAS DE EXTREMIDADES SUPERIORES',
            '873202' : 'RX DE ARTICULACIONES ACROMIO CLAVICULARES COMPARATIVAS',
            '873204' : 'RX DE HOMBRO',
            '873205' : 'RX DE CODO',
            '873206' : 'RX DE PUÑO O MUÑECA',
            '873210' : 'RX DE MANO',
            '873302' : 'RX PARA MEDICICION DE MIEMBROS INFERIORES',
            '873303' : 'RX COMPARATIVA DE PIES CON APOYO',
            '873306' : 'RX PANORAMICA DE MIEMBROS INFERIORES',
            '873312' : 'RX DE FEMÚR',
            '873313' : 'RX DE PIERNA',
            '873333' : 'RX DE PIE',
            '873335' : 'RX DE CALCÁNEO',
            '873411' : 'RX DE CADERA O ARTICULACION COXO-FEMORAL',
            '873412' : 'RX DE CADERA COMPARATIVA',
            '873420' : 'RX DE RODILLA',
            '873422' : 'RX DE RODILLAS COMPARATIVAS POSICIÓN VERTICAL',
            '873423' : 'RX DE TANGENCIAL O AXIAL DE RÓTULA',
            '873431' : 'RX DE TOBILLO',
            '873443' : 'RX DE COMPARATIVAS DE EXTREMIDADES INFERIORES',
            '873444' : 'RX EN EXTREMIDADES PROYECCIONES ADICIONALES',
            '876801' : 'MAMOGRAFIA UNILATERAL O DE PIEZA QUIRURGICA',
            '876802' : 'MAMOGRAFIA BILATERAL',
            '877812' : 'PIELOGRAFÍA A TRAVÉS DE TUBO O NEFROSTOMIA',
            '877815' : 'PIELOGRAFÍA RETRÓGRADA O ANTERÓGRADA',
            '877851' : 'CISTOGRAFÍA CON PROYECCIONES OBLICUAS',
            '877861' : 'URETROCISTOGRAFÍA',
            '877862' : 'URETROCISTOGRAFÍA MICCIONAL',
            '877863' : 'URETROCISTOGRAFÍA RETRÓGRADA',
            '877871' : 'URETROGRAFÍA RETRÓGRADA',
            '879111' : 'TAC DE CRÁNEO SIMPLE',
            '879112' : 'TAC DE CRÁNEO CON CONTRASTE',
            '879113' : 'TAC DE CRÁNEO SIMPLE Y CON CONTRASTE',
            '879116' : 'TAC DE SILLA TURCA (HIPOFISIS)',
            '879121' : 'TAC DE ÓRBITAS',
            '879122' : 'TAC DE OIDO, PEÑASCO Y CONDUCTO AUDITIVO',
            '879131' : 'TAC DE SENOS PARANASALES O CARA',
            '879132' : 'TAC DE RINOFARINGE',
            '879150' : 'TAC DE ARTICULACION TEMPORO MANDIBULAR (BILATERAL)',
            '879161' : 'TAC DE CUELLO',
            '879162' : 'TAC DE LARÍNGE',
            '879201' : 'TAC DE COLUMNA SEGMENTOS CERVICAL, TORACICO, LUMBAR O SACRO POR CADA NIVEL',
            '879205' : 'TAC DE COLUMNA SEGMENTOS CERVICAL, TORACICO, LUMBAR O SACRO, COMPLEMENTO A MIELOGRAFÍA',
            '879301' : 'TAC DE TÓRAX',
            '879391' : 'TAC DE TÓRAX EXTENDIDO AL ABDOMEN SUPERIOR CON SUPRARRENALES',
            '879410' : 'TAC DE ABDOMEN SUPERIOR',
            '879420' : 'TAC DE ABDOMEN Y PELVIS (ABDOMEN TOTAL)',
            '879421' : 'TAC DE CADERA',
            '879430' : 'TAC DE VÍAS URINARIAS',
            '879460' : 'TAC DE PELVIS',
            '879510' : 'TAC DE MIEMBROS SUPERIORES Y ARTICULACIONES',
            '879520' : 'TAC DE MIEMBROS INFERIORES Y ARTICULACIONES',
            '879522' : 'TAC DE MIEMBROS INFERIORES (ANTEVERSIONES FEMORAL O TORSION TIBIAL)',
            '879523' : 'TAC DE MIEMBROS INFERIORES (AXIALES DE RÓTULA O LONGITUD DE MIEMBROS INFERIORES)',
            '879910' : 'TAC EN RECONSTRUCCIÓN TRIDIMENSIONAL',
            '879990' : 'TAC COMO GUIA PARA PROCEDIMIENTOS',
        }
        #Lista de estudios aprovechada por el AutoComplete Widget
        listaEstudios = [
            'RX DE CRÁNEO SIMPLE',
            'RX DE BASE DE CRANEO',
            'RX DE SILLA TURCA',
            'RX DE MASTOIDES COMPARATIVAS',
            'RX DE PEÑASCOS',
            'RX DE CONDUCTO AUDITIVO INTERNO',
            'RX DE CARA',
            'RX DE ÓRBITAS',
            'RX DE AGUJEROS ÓPTICOS',
            'RX DE MALAR',
            'RX DE ARCO CIGOMATICO',
            'RX DE HUESOS NASALES',
            'RX DE SENOS PARANASALES',
            'RX DE MAXILAR SUPERIOR',
            'RX DE MAXILAR INFERIOR',
            'RX DE ARTICULACIÓN TEMPOROMAXILAR',
            'RX DE TEJIDOS BLANDOS DE CUELLO',
            'RX DE CAVUM FARÍNGEO',
            'RX DE COLUMNA CERVICAL',
            'RX DE COLUMNA UNIÓN CERVICO DORSAL',
            'RX DE COLUMNA TORÁCICA',
            'RX DE COLUMNA LUMBOSACRA',
            'RX DE SACRO CÓCCIX',
            'RX DE PANORAMICA DE COLUMNA',
            'RX DINÁMICA DE COLUMNA VERTEBRAL',
            'RX DE COLUMNA VERTEBRAL TOTAL',
            'RX DE ARTICULACIONES  SACROILIACAS',
            'RX DE REJA COSTAL',
            'RX DE ESTERNÓN',
            'RX DE TÓRAX',
            'RX DE ARTICULACIONES ESTERNOCLAVICULARES',
            'RX DE ABDOMEN SIMPLE',
            'RX DE ABDOMEN SIMPLE CON PROYECCIONES ADICIONALES',
            'RX DE COLON POR ENEMA O COLON POR INGESTA',
            'RX DE COLON POR ENEMA CON DOBLE CONTRASTE',
            'RX DE HUESOS LARGOS SERIE COMPLETA',
            'RX PARA DETECTAR EDAD OSEA',
            'RX DE OMOPLATO',
            'RX DE CLAVICULA',
            'RX DE HUMERO',
            'RX DE ANTEBRAZO',
            'RX COMPARATIVAS DE EXTREMIDADES SUPERIORES',
            'RX DE ARTICULACIONES ACROMIO CLAVICULARES COMPARATIVAS',
            'RX DE HOMBRO',
            'RX DE CODO',
            'RX DE PUÑO O MUÑECA',
            'RX DE MANO',
            'RX PARA MEDICICION DE MIEMBROS INFERIORES',
            'RX COMPARATIVA DE PIES CON APOYO',
            'RX PANORAMICA DE MIEMBROS INFERIORES',
            'RX DE FEMÚR',
            'RX DE PIERNA',
            'RX DE PIE',
            'RX DE CALCÁNEO',
            'RX DE CADERA O ARTICULACION COXO-FEMORAL',
            'RX DE CADERA COMPARATIVA',
            'RX DE RODILLA',
            'RX DE RODILLAS COMPARATIVAS POSICIÓN VERTICAL',
            'RX DE TANGENCIAL O AXIAL DE RÓTULA',
            'RX DE TOBILLO',
            'RX DE COMPARATIVAS DE EXTREMIDADES INFERIORES',
            'RX EN EXTREMIDADES PROYECCIONES ADICIONALES',
            'MAMOGRAFIA UNILATERAL',
            'MAMOGRAFIA BILATERAL',
            'PIELOGRAFÍA A TRAVÉS DE TUBO O NEFROSTOMIA',
            'PIELOGRAFÍA RETRÓGRADA O ANTERÓGRADA',
            'CISTOGRAFÍA CON PROYECCIONES OBLICUAS',
            'URETROCISTOGRAFÍA',
            'URETROCISTOGRAFÍA MICCIONAL',
            'URETROCISTOGRAFÍA RETRÓGRADA',
            'URETROGRAFÍA RETRÓGRADA',
            'TAC DE CRÁNEO SIMPLE',
            'TAC DE CRÁNEO CON CONTRASTE',
            'TAC DE CRÁNEO SIMPLE Y CON CONTRASTE',
            'TAC DE SILLA TURCA (HIPOFISIS)',
            'TAC DE ÓRBITAS',
            'TAC DE OIDO, PEÑASCO Y CONDUCTO AUDITIVO',
            'TAC DE SENOS PARANASALES O CARA',
            'TAC DE RINOFARINGE',
            'TAC DE ARTICULACION TEMPORO MANDIBULAR (BILATERAL)',
            'TAC DE CUELLO',
            'TAC DE LARÍNGE',
            'TAC DE COLUMNA SEGMENTOS CERVICAL, TORACICO, LUMBAR O SACRO POR CADA NIVEL',
            'TAC DE COLUMNA SEGMENTOS CERVICAL, TORACICO, LUMBAR O SACRO, COMPLEMENTO A MIELOGRAFÍA',
            'TAC DE TÓRAX',
            'TAC DE TÓRAX EXTENDIDO AL ABDOMEN SUPERIOR CON SUPRARRENALES',
            'TAC DE ABDOMEN SUPERIOR',
            'TAC DE ABDOMEN Y PELVIS (ABD TOTAL)',
            'TAC DE CADERA',
            'TAC DE VÍAS URINARIAS',
            'TAC DE PELVIS',
            'TAC DE MIEMBROS SUPERIORES Y ARTICULACIONES',
            'TAC DE MIEMBROS INFERIORES Y ARTICULACIONES',
            'TAC DE MIEMBROS INFERIORES (ANTEVERSIONES FEMORAL O TORSION TIBIAL)',
            'TAC DE MIEMBROS INFERIORES (AXIALES DE RÓTULA O LONGITUD DE MIEMBROS INFERIORES)',
            'TAC EN RECONSTRUCCIÓN TRIDIMENSIONAL',
            'TAC COMO GUIA PARA PROCEDIMIENTOS'
        ]
        #Funcion que crea el pdf y lo manda a imprimir
        def cleanCampos():
            #datadatadata
            self.UserID.delete(0, 'end')
            self.UserLN1.delete(0, 'end')
            self.UserLN2.delete(0, 'end')
            self.UserFN1.delete(0, 'end')
            self.UserFN2.delete(0, 'end')
            self.UserGN.delete(0, 'end')
            self.UserBD.delete(0, 'end')
            self.UserBT.delete(0, 'end')
            self.UserSN.delete(0, 'end')
            self.UserSN2.delete(0, 'end')
            self.UserID.focus()


        def regexScanner():
            arguments = self.combo.get()
            estudio = self.Auto.get()
            doctype = self.comboID.get()
            print(arguments)
            ScannedID = self.UserID.get()
            ScannedFN1 = self.UserFN1.get()
            ScannedFN2 = self.UserFN2.get()
            ScannedLN1 = self.UserLN1.get()
            ScannedLN2 = self.UserLN2.get()
            #Code = self.entryEstudio.get()

            datenow = datetime.now()
            datenowNm = datenow.strftime('%A')
            
            if datenowNm == 'Monday':
                datenext = datenow + timedelta(1)
            elif datenowNm == 'Tuesday':
                datenext = datenow + timedelta(1)
            elif datenowNm == 'Wednesday':
                datenext = datenow + timedelta(1)
            elif datenowNm == 'Thursday':
                datenext = datenow + timedelta(1)
            elif datenowNm == 'Friday':
                datenext = datenow + timedelta(1)
            elif datenowNm == 'Saturday':
                datenext = datenow + timedelta(2)

            if datenowNm == 'Monday' and arguments == 'EPS':
                datenext = datenow + timedelta(3)
            elif datenowNm == 'Tuesday' and arguments == 'EPS':
                datenext = datenow + timedelta(3)
            elif datenowNm == 'Wednesday' and arguments == 'EPS':
                datenext = datenow + timedelta(5)
            elif datenowNm == 'Thursday' and arguments == 'EPS':
                datenext = datenow + timedelta(5)
            elif datenowNm == 'Friday' and arguments == 'EPS':
                datenext = datenow + timedelta(5)
            elif datenowNm == 'Saturday' and arguments == 'EPS':
                datenext = datenow + timedelta(4)

            fechaEstudio = datenow.strftime('%d/%m/%Y')
            fechaRecol = datenext.strftime('%d/%m/%Y')
            fullString = ScannedFN1+' '+ScannedFN2+' '+ScannedLN1+' '+ScannedLN2
            #value = estudios.get(Code)
            if estudio in listaEstudios:
                messagebox.showinfo('Solicitud exitosa','Haga click para imprimir' )
                bc = barcode.get('code128', ScannedID, writer=ImageWriter())
                filename = bc.save('codigo', options={"write_text": False})

                pdf = FPDF('P', 'mm', (72, 320))
                pdf.add_page()
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(40, 10, 'MUNDO RADIOLOGICO S.A.S')
                pdf.ln()
                pdf.set_font('Arial', 'B', 9)
                pdf.cell(55, 4, 'TICKET DE RESULTADOS', 0,0, 'C')
                pdf.ln()
                pdf.set_font('Arial', 'B', 8)
                pdf.cell(0,5, arguments,0,0,'R')
                pdf.ln()
                pdf.set_font('Arial', '', 7)
                pdf.cell(15, 5, 'Nombre del paciente: ')
                pdf.ln()
                pdf.set_font('Arial', '', 6)
                pdf.multi_cell(50, 3, fullString ,0,0,'L')
                pdf.ln()
                pdf.set_font('Arial', '', 7)
                pdf.cell(10, 3, 'Documento: ')
                pdf.ln()
                pdf.cell(20, 5, doctype+' '+ScannedID)
                pdf.ln()
                pdf.cell(15, 5, 'Estudio realizado: ')
                pdf.ln()
                pdf.set_font('Arial', '', 6)
                pdf.multi_cell(50, 3, estudio, 0,0,'L')
                pdf.ln()
                pdf.set_font('Arial', '', 7)
                pdf.cell(24, 5, 'Fecha de realizacion:')
                pdf.cell(45, 5, fechaEstudio)
                pdf.ln()
                pdf.cell(24, 5, 'Fecha de entrega:')
                pdf.cell(45, 5, fechaRecol)
                pdf.ln()
                pdf.image('codigo.png', w=50, h=20)
                pdf.output('resultado.pdf', 'F')

                #Comando de impresion, Acrobat Reader o Similar es necesario para su ejecucion
                os.startfile("resultado.pdf", "print")
                
            else:
                #En caso de error revisar
                messagebox.showerror('Solicitud Cancelada', 'Corrija el nombre del estudio.\n\nSi desconoce el nombre puede buscarlo\nen la lista plegable alfabeticamente')
            #print(ScannedID)
            #print(fullString)
            #print(estudio)
            
        super().__init__(main_window)
        main_window.title('RESULTADOS MUNDO RADIOLOGICO')
        self.label = tk.Label(text='Seleccionar la entidad')
        self.comboID = ttk.Combobox(self, state='readonly', width=5)
        self.comboID.place(x=15, y=50)
        self.comboID['values']=['C.C.', 'T.I.', 'R.C.']
        self.comboID.current(0)
        self.label.place(x=80, y=300)
        self.IDlabel = tk.Label(text='Numero de cedula')
        self.LN1label = tk.Label(text='Primer Apellido')
        self.LN2label = tk.Label(text='Segudo Apellido')
        self.FN1label = tk.Label(text='Primer Nombre')
        self.FN2label = tk.Label(text='Segundo Nombre')
        self.IGNORElabel = tk.Label(text='Ignorar Campos')
        self.userLabel = tk.Label(text='Escanear codigo de barras')
        self.userLabel.place(x=150, y=10)
        self.UserID = tk.Entry(main_window)
        self.UserLN1 = tk.Entry(main_window)
        self.UserLN2 = tk.Entry(main_window)
        self.UserFN1 = tk.Entry(main_window)
        self.UserFN2 = tk.Entry(main_window)
        self.UserGN = tk.Entry(main_window)
        self.UserBD = tk.Entry(main_window)
        self.UserBT = tk.Entry(main_window)
        self.UserSN = tk.Entry(main_window)
        self.UserSN2 = tk.Entry(main_window)
        self.IDlabel.place(x=80, y=30)
        self.UserID.place(x=80, y=50)
        self.UserID.focus()
        self.LN1label.place(x=250, y=30)
        self.UserLN1.place(x=250, y=50)
        self.LN2label.place(x=80, y=80)
        self.UserLN2.place(x=80, y=100)
        self.FN1label.place(x=250, y=80)
        self.UserFN1.place(x=250, y=100)
        self.FN2label.place(x=80, y=130)
        self.UserFN2.place(x=80, y=150)
        self.IGNORElabel.place(x=250, y=130)
        self.UserGN.place(x=250, y=150)
        self.UserBD.place(x=80, y=200)
        self.UserBT.place(x=250, y=200)
        self.UserSN.place(x=80, y=250)
        self.UserSN2.place(x=250, y=250)
        self.combo = ttk.Combobox(self, state='readonly')
        self.combo.place(x=250, y=300)
        self.combo['values']= ['EPS', 'PREPAGADA', 'PARTICULAR']
        self.combo.current(0)
        self.codigo = tk.Label(text='Estudio realizado: ')
        self.codigo.place(x=80, y=330)
        self.introBtn = tk.Button(main_window, text='Solicitar', command=regexScanner)
        self.introBtn.place(x=150, y=400)
        self.Auto = AutocompleteCombobox(width=48, completevalues=(listaEstudios))
        self.Auto.place(x=80, y=360)
        self.cleanBtn = tk.Button(main_window, text='Reiniciar', command=cleanCampos)
        self.cleanBtn.place(x=250, y=400)
        #self.entryEstudio = tk.Entry(main_window)
        #self.entryEstudio.place(x=250, y=350)
        main_window.configure(width=500, height=450)
        self.place(width=500, height=450)



main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
