from PIL import Image, ImageDraw, ImageFont
import qrcode
import xlrd
import os
import glob
productos_titulo = []

workbook = xlrd.open_workbook("Excel_Madagascar/Municipalidades_EntreKids_invitacion.xlsx","rb")
sheets = workbook.sheet_names()
type_code = []
codigo_qr_texto = []
codigo_qr_imagen = []
for sheet_name in sheets:
    sh = workbook.sheet_by_name(sheet_name)
    for rownum in range(sh.nrows):
        row_valaues = sh.row_values(rownum)
        type_code.append(row_valaues[0])
        codigo_qr_texto.append(row_valaues[1])
        codigo_qr_imagen.append(row_valaues[2])
 

HEIGHT = 500
WIDTH = 500


TEXTO = ''

for i in range(len(type_code)):
 
    if type_code[i] == 'Palco':
        TEMPLATE_TARZAN = Image.open('Madagascar/Cortesia/entrada.jpg').convert('RGBA')
        TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size
        draw = ImageDraw.Draw(TEMPLATE_TARZAN)
        TEXTO = Image.open('Madagascar/Corte/palco.png').convert('RGBA')
        TEXTO = TEXTO.resize((75, 26), Image.ANTIALIAS)

        TEXTO_QR_W = TEMPLATE_TARZAN_W // 2 - TEMPLATE_TARZAN_W // 4
        TEXT_QR_H = TEMPLATE_TARZAN_H // 2 - TEMPLATE_TARZAN_H // 4

        data = str(codigo_qr_imagen[i])
        qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 1
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('tempQR/' + str(i) + '.png')
        loadQR = Image.open('tempQR/' + str(i) + '.png').convert('RGBA')


        loadQR = loadQR.resize((200, 200), Image.ANTIALIAS)
        loadQR_w, loadQR_h = loadQR.size

        better_w = TEXTO.size[0]


        position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

        TEMPLATE_TARZAN.paste(loadQR, ((TEMPLATE_TARZAN_W // 2) - loadQR_w // 2, 140), loadQR)
        TEMPLATE_TARZAN.paste(TEXTO, ((TEMPLATE_TARZAN_W // 2) - better_w // 2, TEXT_QR_H - 105), TEXTO)

        font = ImageFont.truetype("Pangram-Regular.otf", 20)
        font = ImageFont.truetype("Pangram-Medium.otf", 20)



        w, h = draw.textsize(str(codigo_qr_imagen[i]), font)
        #draw.text( ((TEMPLATE_TARZAN_W // 2) - w / 2, 100), str(type_code[i]),  fill="white", font=font)
        

        #TEMPLATE_TARZAN.show()

   
        TEMPLATE_TARZAN.save('QR_MUNICIPALIDADES_INVITACION/qr_' + str(type_code[i].lower()) + '_' + str(i) + '.png')
        os.remove('tempQR/' + str(i) + '.png')
      
  

    if type_code[i] == 'Platea Alta':
        TEMPLATE_TARZAN = Image.open('Madagascar/Cortesia/entrada.jpg').convert('RGBA')
        TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size
        draw = ImageDraw.Draw(TEMPLATE_TARZAN)
        TEXTO = Image.open('Madagascar/Corte/platea_alta.png').convert('RGBA')
        TEXTO = TEXTO.resize((75, 26), Image.ANTIALIAS)

        TEXTO_QR_W = TEMPLATE_TARZAN_W // 2 - TEMPLATE_TARZAN_W // 4
        TEXT_QR_H = TEMPLATE_TARZAN_H // 2 - TEMPLATE_TARZAN_H // 4

        data = str(codigo_qr_imagen[i])
        qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 1
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('tempQR/' + str(i) + '.png')
        loadQR = Image.open('tempQR/' + str(i) + '.png').convert('RGBA')


        loadQR = loadQR.resize((200, 200), Image.ANTIALIAS)
        loadQR_w, loadQR_h = loadQR.size

        better_w = TEXTO.size[0]


        position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

        TEMPLATE_TARZAN.paste(loadQR, ((TEMPLATE_TARZAN_W // 2) - loadQR_w // 2, 140), loadQR)
        TEMPLATE_TARZAN.paste(TEXTO, ((TEMPLATE_TARZAN_W // 2) - better_w // 2, TEXT_QR_H - 105), TEXTO)

        font = ImageFont.truetype("Pangram-Regular.otf", 20)
        font = ImageFont.truetype("Pangram-Medium.otf", 20)



        w, h = draw.textsize(str(codigo_qr_imagen[i]), font)
        draw.text( ((TEMPLATE_TARZAN_W // 2) - w / 2, 670), str(codigo_qr_imagen[i]),  fill="white", font=font)
        

        #TEMPLATE_TARZAN.show()
        TEMPLATE_TARZAN.save('QR_MUNICIPALIDADES_INVITACION/qr_' + str(type_code[i].lower()) + '_' + str(i) + '.png')
        os.remove('tempQR/' + str(i) + '.png')

    if type_code[i] == 'Platea':
        TEMPLATE_TARZAN = Image.open('Madagascar/Cortesia/entrada.jpg').convert('RGBA')
        TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size
        draw = ImageDraw.Draw(TEMPLATE_TARZAN)
        TEXTO = Image.open('Madagascar/Corte/platea.png').convert('RGBA')
        TEXTO = TEXTO.resize((75, 26), Image.ANTIALIAS)

        TEXTO_QR_W = TEMPLATE_TARZAN_W // 2 - TEMPLATE_TARZAN_W // 4
        TEXT_QR_H = TEMPLATE_TARZAN_H // 2 - TEMPLATE_TARZAN_H // 4

        data = str(codigo_qr_imagen[i])
        qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 1
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('tempQR/' + str(i) + '.png')
        loadQR = Image.open('tempQR/' + str(i) + '.png').convert('RGBA')


        loadQR = loadQR.resize((200, 200), Image.ANTIALIAS)
        loadQR_w, loadQR_h = loadQR.size

        better_w = TEXTO.size[0]


        position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

        TEMPLATE_TARZAN.paste(loadQR, ((TEMPLATE_TARZAN_W // 2) - loadQR_w // 2, 140), loadQR)
        TEMPLATE_TARZAN.paste(TEXTO, ((TEMPLATE_TARZAN_W // 2) - better_w // 2, TEXT_QR_H - 105), TEXTO)

        font = ImageFont.truetype("Pangram-Regular.otf", 20)
        font = ImageFont.truetype("Pangram-Medium.otf", 20)



        w, h = draw.textsize(str(codigo_qr_imagen[i]), font)
        #draw.text( ((TEMPLATE_TARZAN_W // 2) - w / 2, 100), str(type_code[i]),  fill="white", font=font)
        

        #TEMPLATE_TARZAN.show()

   
        TEMPLATE_TARZAN.save('QR_MUNICIPALIDADES_INVITACION/qr_' + str(type_code[i].lower()) + '_' + str(i) + '.png')
        os.remove('tempQR/' + str(i) + '.png')
   