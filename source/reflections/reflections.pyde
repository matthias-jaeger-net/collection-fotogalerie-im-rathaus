def setup():
    def reverse_image(img):
        canvas = createGraphics(img.width, img.height)
        canvas.beginDraw()
        for i in range(0, canvas.width):
            for j in range(0, canvas.height):
                x = canvas.width - i
                c = img.get(i, j)
                canvas.stroke(c)
                canvas.point(x, j)
        canvas.endDraw()
        return canvas
    
    def reflect_image(img):
        canvas = createGraphics(img.width, img.height)
        half = canvas.width / 2
        left_side = img.get(0, 0, half, canvas.height)
        right_side = reverse_image(left_side)
        canvas.beginDraw()
        canvas.image(left_side, 0, 0)
        canvas.image(right_side, half, 0)
        canvas.endDraw()
        return canvas
    
    # IMG_20210312_100822.jpg
    # IMG_20210312_100700.jpg
    foto = loadImage("IMG_20210312_100822.jpg")    
    
    # 1x: 2736, 3648 || 2x: 5472, 7296     
    canvas = createGraphics(5472, 7296)
    canvas.beginDraw()
    canvas.image(foto, 0, 0, canvas.width, canvas.height)
    
    padding = 100
    minimum = 800
    maximum = 1200
    layers = 60
    
    for layer in range(0, layers): 
        x = int(random(padding, canvas.width - padding))
        y = int(random(padding, canvas.width - padding))
        w = int(random(minimum, maximum))
        h = int(random(minimum, maximum))        
        collage_piece = canvas.get(x, y, w, h)
        reflection = reflect_image(collage_piece)  
        canvas.image(reflection, x, y)

    canvas.endDraw()
    
    hash = str(random(1))
    extension = "jpg"
    out = "out/{h}.{e}".format(h=hash, e=extension)
    canvas.save(out)    
    exit()
        
