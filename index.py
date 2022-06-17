from PIL import Image
import qrcode
import xlrd


productos_titulo = []

workbook = xlrd.open_workbook("Excel_Tarzan/GalaTarzanEntrekidsCortesia.xlsx","rb")
sheets = workbook.sheet_names()
type_code = []
for sheet_name in sheets:
    sh = workbook.sheet_by_name(sheet_name)
    for rownum in range(sh.nrows):
        row_valaues = sh.row_values(rownum)
        type_code.append(row_valaues[0])
 


HEIGHT = 500
WIDTH = 500
TEMPLATE_TARZAN = Image.open('Tarzan/Cortesia/TemplateRetiro.jpg').convert('RGBA')
TEMPLATE_TARZAN_W, TEMPLATE_TARZAN_H = TEMPLATE_TARZAN.size




data = 'OK3uq31a'
img = qrcode.make(data)
img.save('QRCODE/TARZAN/Cortesia/MyQRCode1.png')
loadQR = Image.open('QRCODE/TARZAN/Cortesia/MyQRCode1.png').convert('RGBA')
loadQR = loadQR.resize((180, 180), Image.ANTIALIAS)
loadQR_w, loadQR_h = loadQR.size


position_qr_w = TEMPLATE_TARZAN_W - TEMPLATE_TARZAN_W // 2

TEMPLATE_TARZAN.paste(loadQR, ((position_qr_w - 145) // 2, (TEMPLATE_TARZAN_H - loadQR_w) // 2 + 30), loadQR)

for i in range(len(type_code)):
    if type_code == 'PLATEA':
        TEMPLATE_TARZAN.save('Tarzan/Cortesia/TarzanCortesia.jpg')




#bg = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
TEMPLATE_TARZAN.show()



