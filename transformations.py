import math
from line_drawing import draw

def translacao(screen, items, tx, ty):
    """
    Translação 2D dos itens.
    """
    for item in items:
        item["p1"] = (item["p1"][0] + tx, item["p1"][1] + ty)
        item["p2"] = (item["p2"][0] + tx, item["p2"][1] + ty)
        draw(screen, item)  # Desenha os itens recalculados

def escala(screen, items, sx, sy):
    """
    Escala dos itens.
    """
    for item in items:
        item["p1"] = (item["p1"][0] * sx, item["p1"][1] * sy)
        item["p2"] = (item["p2"][0] * sx, item["p2"][1] * sy)
        item["r"] = item["r"] * max(sx, sy)
        draw(screen, item)

def rotacao(screen, items, theta):
    """
    Rotação dos itens.
    """
    theta = math.radians(theta)

    for item in items:
        x1, y1 = item["p1"]
        x2, y2 = item["p2"]

        item["p1"] = (
            x1 * math.cos(theta) - y1 * math.sin(theta),
            x1 * math.sin(theta) + y1 * math.cos(theta)
        )
        item["p2"] = (
            x2 * math.cos(theta) - y2 * math.sin(theta),
            x2 * math.sin(theta) + y2 * math.cos(theta)
        )
        draw(screen, item)

def reflexao(screen, items, ref_type):
    """
    Reflexão dos itens.
    """
    for item in items:
        x1 = item["p1"][0]
        y1 = item["p1"][1]
        x2 = item["p2"][0]
        y2 = item["p2"][1]

        if ref_type == "X":
            item["p1"], item["p2"] = (x1, -y1), (x2, -y2)
        elif ref_type == "Y":
            item["p1"], item["p2"] = (-x1, y1), (-x2, y2)
        else:  # "XY"
            item["p1"], item["p2"] = (-x1, -y1), (-x2, -y2)

        draw(screen, item)
