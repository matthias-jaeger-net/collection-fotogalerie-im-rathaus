def setup():
    size(1200, 900)
    img = loadImage('rolle1_10.jpg')
    for u in range(0, width, 80):
        for v in range (0, height, 80):
            x1 = u * 80
            y1 = v * 80
            x2 = u + random(-140, 140)
            y2 = v + random(-20, 20)
            a = PVector(x1, y1)
            b = PVector(x2, y2)
            c1 = img.get(int(x1), int(y1))
            c2 = img.get(int(x2), int(y2))
            d = a.copy().sub(b)
            m = d.mag()
            d.normalize()
            for i in range(0, m, m / 100):
                a.add(d)
                c = lerpColor(color(c1), color(c2), map(i, 0, m, 2, 30))
                stroke(c)
                strokeWeight(noise(i * 0.01, a.x * 0.01, a.y * 0.01) * th)
                point(a.x + noise(i * 0.01, a.x * 0.01, a.y * 0.01) * th, a.y + noise(i * 0.01, a.x * 0.01, a.y * 0.01) * th)
                    
    # save("picture-painter.jpg")
