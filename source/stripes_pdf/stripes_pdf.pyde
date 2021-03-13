add_library('pdf')

def setup():
    
    files = ['IMG_6274.JPG', 'IMG_6286.JPG']
    file_name_in = files[1]    
    id = str(random(1))
    file_name_out = 'out/{id}.{f}.pdf'.format(id=id, f=file_name_in)
    
    pdf = createGraphics(900, 900, PDF, file_name_out) 
    img = loadImage(file_name_in)
    img.resize(pdf.width, pdf.height)
    
    scaler = 8.0
    left_slice = random(0, pdf.width / 2)
    right_slice = random(pdf.width / 2, pdf.width)
    
    pdf.beginDraw()
    
    for u in range(0, pdf.width):
        for v in range(0, pdf.height):
            left_color = img.get(int(left_slice), int(v * scaler))
            right_color = img.get(int(right_slice), int(v * scaler))
            ammount = map(u * scaler, 0, pdf.width, 0, 1)
            new_color = lerpColor(color(left_color), color(right_color), ammount)
            
            pdf.stroke(new_color)
            pdf.fill(new_color)
            pdf.rect(u * scaler, v * scaler, scaler, scaler)
    
    pdf.dispose()
    pdf.endDraw()
    
    exit()
