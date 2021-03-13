add_library('pdf')

files = ['IMG_6274.JPG', 'IMG_6286.JPG']
file_name_in = files[0]
file_name_out = 'out/stripes.pdf'

scaler = 8.0

pdf = None
img = None
left_slice = None
right_slice = None

def setup():
    global pdf, img, left_slice, right_slice
    pdf = createGraphics(900, 900, PDF, file_name_out) 
    pdf.beginDraw()
    
    img = loadImage(file_name_in)
    img.resize(pdf.width, pdf.height)

    left_slice = int(random(0, pdf.width / 2))
    right_slice = int(random(pdf.width / 2, pdf.width))

    for u in range(0, pdf.width):
        for v in range(0, pdf.height):
            x = u * scaler
            y = v * scaler
                        
            left_color = img.get(left_slice, int(y))
            left_color = color(left_color)
            right_color = img.get(right_slice, int(y))
            right_color = color(right_color)
            new_color = lerpColor(left_color, right_color, map(x, 0, pdf.width, 0, 1))
            
            pdf.stroke(new_color)
            pdf.fill(new_color)
            pdf.rect(x, y, scaler, scaler)
    
    pdf.dispose()
    pdf.endDraw()
    exit()
