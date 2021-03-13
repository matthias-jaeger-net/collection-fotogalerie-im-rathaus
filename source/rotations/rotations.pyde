add_library('pdf')

def setup():
    files = ['IMG_6479.JPG', 'IMG_6315.JPG']
    file_name_in = files[1]    
    id = str(random(1))
    file_name_out = 'out/{id}.{f}.pdf'.format(id=id, f=file_name_in)
    
    pdf = createGraphics(900, 900, PDF, file_name_out) 
    pdf.beginDraw()
    pdf.background(255)
    
    img = loadImage(file_name_in)
    img.resize(pdf.width * 2, pdf.height * 2)

    vals = []
    for x in range(0, img.width):
        for y in range(0, img.height):
            b = brightness(img.get(x, y))
            vals.append(b / 255.0)

    angle = 0
    step = TAU / 360
    maximum = pdf.width / 2
    rotations = TAU * 200
    index = 0
    
    while (angle < rotations):
        radius = vals[index] * maximum
        
        pdf.pushMatrix()
        pdf.translate(pdf.width / 2, pdf.height / 2)
        pdf.rotate(angle)
        pdf.translate(radius, 0)
        pdf.point(0, 0)
        pdf.popMatrix()
        
        angle = angle + step
        if (index < len(vals)):
            index = index + 1
        else:
            index = 0
    
    pdf.dispose()
    pdf.endDraw()
    exit()
