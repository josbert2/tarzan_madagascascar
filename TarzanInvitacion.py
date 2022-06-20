from PIL import Image, ImageDraw, ImageFont
import qrcode
import xlrd
import os
import glob
productos_titulo = []

workbook = xlrd.open_workbook("Excel_Tarzan/CortesíasNidoCirc3000_invitacion.xlsx","rb")
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
   
    if type_code[i] == 'PLATEA':
        TEMPLATE_TARZAN = Image.open('Tarzan/inauguracion/TemplateRetiro.jpg').convert('RGBA')
        TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size
        draw = ImageDraw.Draw(TEMPLATE_TARZAN)
        TEXTO = Image.open('Tarzan/Corte/platea.png').convert('RGBA')
        TEXTO = TEXTO.resize((75, 26), Image.ANTIALIAS)

        TEXTO_QR_W = TEMPLATE_TARZAN_W // 2 - TEMPLATE_TARZAN_W // 4
        TEXT_QR_H = TEMPLATE_TARZAN_H // 2 - TEMPLATE_TARZAN_H // 4

        data = str(codigo_qr_imagen[i] + '?utm_source=qr_ticketfisico&utm_campaign=tarzan_y_jane&utm_medium=qr_ticketfisico_goldencircus')
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


        loadQR = loadQR.resize((180, 180), Image.ANTIALIAS)
        loadQR_w, loadQR_h = loadQR.size


        position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

        TEMPLATE_TARZAN.paste(loadQR, ((position_qr_w - 145) // 2, (TEMPLATE_TARZAN_H - loadQR_w) // 2 + 30), loadQR)
        TEMPLATE_TARZAN.paste(TEXTO, (TEXTO_QR_W - 16, TEXT_QR_H + 10), TEXTO)

        font = ImageFont.truetype("Pangram-Regular.otf", 20)
        font = ImageFont.truetype("Pangram-Medium.otf", 20)
        draw.text( (TEXTO_QR_W - 115, TEXT_QR_H + 235), str(codigo_qr_texto[i]),  fill="white", font=font)
        

       
        TEMPLATE_TARZAN.save('QR_TARZAN_INVITACIONES/qr_' + str(type_code[i].lower()) + '_' + str(i) + '.png')
        os.remove('tempQR/' + str(i) + '.png')

    if type_code[i] == 'TRIBUNA':
        TEMPLATE_TARZAN = Image.open('Tarzan/Cortesia/TemplateRetiro.jpg').convert('RGBA')
        TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size
        draw = ImageDraw.Draw(TEMPLATE_TARZAN)
        TEXTO = Image.open('Tarzan/Corte/tribuna.png').convert('RGBA')
        TEXTO = TEXTO.resize((95, 26), Image.ANTIALIAS)

        TEXTO_QR_W = TEMPLATE_TARZAN_W // 2 - TEMPLATE_TARZAN_W // 4
        TEXT_QR_H = TEMPLATE_TARZAN_H // 2 - TEMPLATE_TARZAN_H // 4

        data = str(codigo_qr_imagen[i] + '?utm_source=qr_ticketfisico&utm_campaign=tarzan_y_jane&utm_medium=qr_ticketfisico_goldencircus')
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


        loadQR = loadQR.resize((180, 180), Image.ANTIALIAS)
        loadQR_w, loadQR_h = loadQR.size


        position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

        TEMPLATE_TARZAN.paste(loadQR, ((position_qr_w - 145) // 2, (TEMPLATE_TARZAN_H - loadQR_w) // 2 + 30), loadQR)
        TEMPLATE_TARZAN.paste(TEXTO, (TEXTO_QR_W - 25, TEXT_QR_H + 10), TEXTO)

        font = ImageFont.truetype("Pangram-Regular.otf", 20)
        font = ImageFont.truetype("Pangram-Medium.otf", 20)
        draw.text( (TEXTO_QR_W - 115, TEXT_QR_H + 235), str(codigo_qr_texto[i]),  fill="white", font=font)
        

       
        TEMPLATE_TARZAN.save('QR_TARZAN_INVITACIONES/qr_' + str(type_code[i].lower()) + '_' + str(i) + '.png')
        os.remove('tempQR/' + str(i) + '.png')
     
    if type_code[i] == 'PALCO':
      
        TEMPLATE_TARZAN = Image.open('Tarzan/Cortesia/TemplateRetiro.jpg').convert('RGBA')
        TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size
        draw = ImageDraw.Draw(TEMPLATE_TARZAN)
        TEXTO = Image.open('Tarzan/Corte/palco.png').convert('RGBA')
        TEXTO = TEXTO.resize((75, 26), Image.ANTIALIAS)

        TEXTO_QR_W = TEMPLATE_TARZAN_W // 2 - TEMPLATE_TARZAN_W // 4
        TEXT_QR_H = TEMPLATE_TARZAN_H // 2 - TEMPLATE_TARZAN_H // 4

        data = str(codigo_qr_imagen[i] + '?utm_source=qr_ticketfisico&utm_campaign=tarzan_y_jane&utm_medium=qr_ticketfisico_goldencircus')
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


        loadQR = loadQR.resize((180, 180), Image.ANTIALIAS)
        loadQR_w, loadQR_h = loadQR.size


        position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

        TEMPLATE_TARZAN.paste(loadQR, ((position_qr_w - 145) // 2, (TEMPLATE_TARZAN_H - loadQR_w) // 2 + 30), loadQR)
        TEMPLATE_TARZAN.paste(TEXTO, (TEXTO_QR_W - 16, TEXT_QR_H + 10), TEXTO)

        font = ImageFont.truetype("Pangram-Regular.otf", 20)
        font = ImageFont.truetype("Pangram-Medium.otf", 20)
        draw.text( (TEXTO_QR_W - 115, TEXT_QR_H + 235), str(codigo_qr_texto[i]),  fill="white", font=font)
        

        #bg = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
        TEMPLATE_TARZAN.save('QR_TARZAN_INVITACIONES/qr_' + str(type_code[i].lower()) + '_' + str(i) + '.png')
        os.remove('tempQR/' + str(i) + '.png')





