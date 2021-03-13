add_library('pdf')

def setup():
    id = str(random(1))
    files = ['IMG_6274.JPG', 'IMG_6286.JPG']
    file_name_in = files[1]
    file_name_out = 'out/{id}.{f}.pdf'.format(id=id, f=file_name_in)
    pdf = createGraphics(900, 900, PDF, file_name_out) 
    scaler = 8.0
    left_slice = int(random(0, pdf.width / 2))
    right_slice = int(random(pdf.width / 2, pdf.width))
    img = loadImage(file_name_in)
    img.resize(pdf.width, pdf.height)
    pdf.beginDraw()
    for u in range(0, pdf.width):
        for v in range(0, pdf.height):
            x = u * scaler
            y = v * scaler
            left_color = img.get(left_slice, int(y))
            left_color = color(left_color)
            right_color = img.get(right_slice, int(y))
            right_color = color(right_color)
            ammount = map(x, 0, pdf.width, 0, 1)
            new_color = lerpColor(left_color, right_color, ammount)
            pdf.stroke(new_color)
            pdf.fill(new_color)
            pdf.rect(x, y, scaler, scaler)
    pdf.dispose()
    pdf.endDraw()
    exit()
