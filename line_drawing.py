def draw_pixel(screen, x, y, tags="default"):
    """
    Desenha um pixel na tela.
    """
    screen.canvas.create_rectangle(x, y, x + 1, y + 1, tags=tags)

def draw(screen, item):
    """
    Chama as funções de desenho de acordo com o tipo do item.
    """
    print(item)
    if item["type"] == "circ_bresenham":
        circ_bresenham(screen, item)
    else:
        DDA(screen, item)

def DDA(screen, item):
    """
    Algoritmo de DDA para desenhar uma linha entre dois pontos.
    """
    x1, y1 = item["p1"]
    x2, y2 = item["p2"]

    dx = int(x2 - x1)
    dy = int(y2 - y1)

    passos = max(abs(dx), abs(dy))

    x_incr = dx / passos
    y_incr = dy / passos

    x, y = x1, y1
    draw_pixel(screen, x, y)

    for _ in range(passos):
        x += x_incr
        y += y_incr
        draw_pixel(screen, x, y)

def circ_bresenham(screen, item):
    """
    Algoritmo de Bresenham para desenhar um círculo.
    """
    def _plot_circle_points(screen, xc, yc, x, y):
        draw_pixel(screen, xc + x, yc + y)
        draw_pixel(screen, xc - x, yc + y)
        draw_pixel(screen, xc + x, yc - y)
        draw_pixel(screen, xc - x, yc - y)
        draw_pixel(screen, xc + y, yc + x)
        draw_pixel(screen, xc - y, yc + x)
        draw_pixel(screen, xc + y, yc - x)
        draw_pixel(screen, xc - y, yc - x)

    xc, yc = item["p1"]
    r = item["r"]
    x, y = 0, r
    p = 3 - 2 * r

    _plot_circle_points(screen, xc, yc, x, y)

    while (x < y):
        if (p < 0):
            p += 4 * x + 6
        else:
            p += 4 * (x - y) + 10
            y -= 1
        x += 1
        _plot_circle_points(screen, xc, yc, x, y)

def bresenham(screen, item):
    """
    Algoritmo de Bresenham para desenhar uma linha.
    """
    x1, y1 = item["p1"]
    x2, y2 = item["p2"]

    dx = int(x2 - x1)
    dy = int(y2 - y1)

    incrx = 1 if dx >= 0 else -1
    incry = 1 if dy >= 0 else -1
    dx, dy = abs(dx), abs(dy)

    x, y = x1, y1
    draw_pixel(screen, x, y)

    if dy < dx:
        p = 2 * dy - dx
        c1 = 2 * dy
        c2 = 2 * (dy - dx)

        for _ in range(dx):
            x += incrx
            if p < 0:
                p += c1
            else:
                y += incry
                p += c2
            draw_pixel(screen, x, y)
    else:
        p = 2 * dx - dy
        c1 = 2 * dx
        c2 = 2 * (dx - dy)

        for _ in range(dy):
            y += incry
            if p < 0:
                p += c1
            else:
                x += incrx
                p += c2
            draw_pixel(screen, x, y)
