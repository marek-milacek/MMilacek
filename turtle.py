"""
Unikátní Ornámenty - Collaborative Turtle Graphics

Program vykreslí několik unikátních ornamentů pomocí collaborative turtle.
Každý ornament má své vlastní želvy, které spolu pracují na jednom plátně.
Spuštění: python idk.py
"""

import turtle
import math
import time

# Barvy v daném schématu
PALETTE = {
    "bg": "#1a1a2e",
    "accent1": "#ff6b6b",      # růžová
    "accent2": "#ffa500",      # oranžová
    "accent3": "#4ecdc4",      # tyrkysová
    "accent4": "#ffe66d",      # zlatá
    "accent5": "#a8e6cf",      # mintová
    "accent6": "#dda0dd",      # švestková
}


def create_turtle(screen, color, speed=0):
    """Vytvoří nový turtle s daným nastavením."""
    t = turtle.Turtle()
    t.color(color)
    t.speed(speed)
    t.hideturtle()
    return t


def ornament_1_mandala(screen, x, y, size, color1, color2):
    """Ornament 1: Mandala - dvě spolupracující želvy kreslí koncentrické kruhy a hvězdy."""
    t1 = create_turtle(screen, color1)
    t2 = create_turtle(screen, color2)
    
    # Turtle 1 kreslí soustředné kruhy
    t1.penup()
    t1.goto(x, y - size)
    t1.pensize(3)
    for i in range(6):
        t1.pendown()
        t1.circle(size - (i * size / 6))
        t1.penup()
        t1.goto(x, y - (size - (i + 1) * size / 6))
    
    # Turtle 2 kreslí hvězdy na kruzích
    t2.penup()
    t2.pensize(2)
    for ring in range(1, 5):
        radius = size * (ring / 5)
        for angle in range(0, 360, 45):
            tx = x + radius * math.cos(math.radians(angle))
            ty = y + radius * math.sin(math.radians(angle))
            t2.goto(tx, ty)
            # Malá hvězda
            t2.pendown()
            for _ in range(5):
                t2.forward(5)
                t2.right(144)
            t2.penup()


def ornament_2_fractal_tree(screen, x, y, length, angle, depth, color1, color2):
    """Ornament 2: Fraktální strom - dvě želvy kreslí větve postupně."""
    t1 = create_turtle(screen, color1)
    t2 = create_turtle(screen, color2)
    
    def draw_branch(turtle_obj, x, y, length, angle, depth, is_main):
        if depth == 0:
            return
        
        # Spočítej konec větve
        x_end = x + length * math.cos(math.radians(angle))
        y_end = y + length * math.sin(math.radians(angle))
        
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        turtle_obj.pensize(max(1, depth))
        turtle_obj.goto(x_end, y_end)
        
        # Rekurzivní kreslení levé a pravé větve
        angle_left = angle + 25
        angle_right = angle - 25
        new_length = length * 0.7
        
        draw_branch(turtle_obj, x_end, y_end, new_length, angle_left, depth - 1, is_main)
        draw_branch(turtle_obj, x_end, y_end, new_length, angle_right, depth - 1, is_main)
    
    # Turtle 1 kreslí první (levé) větve
    # Turtle 2 kreslí druhé (pravé) větve
    for branch in range(1, 3):
        t = t1 if branch == 1 else t2
        angle_start = 90 + (branch - 1) * 20
        draw_branch(t, x, y, length, angle_start, depth, branch == 1)


def ornament_3_spiral_galaxy(screen, x, y, size, color1, color2, color3):
    """Ornament 3: Spirální galaxie - tři želvy kreslí spirály."""
    t1 = create_turtle(screen, color1)
    t2 = create_turtle(screen, color2)
    t3 = create_turtle(screen, color3)
    
    turtles = [t1, t2, t3]
    
    for idx, t in enumerate(turtles):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(2)
        
        start_angle = idx * 120
        t.setheading(start_angle)
        
        # Spirála
        for i in range(200):
            step = size * i / 200
            t.forward(step / 20)
            t.right(3)
            if i % 20 == 0:
                t.penup()
                t.forward(1)
                t.pendown()


def ornament_4_geometric_dance(screen, x, y, size, color1, color2):
    """Ornament 4: Geometrický tanec - rotující polygony od dvou želv."""
    t1 = create_turtle(screen, color1)
    t2 = create_turtle(screen, color2)
    
    # Turtle 1 kreslí vnější polygon
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.pensize(3)
    
    sides = 8
    for _ in range(sides):
        t1.forward(size)
        t1.right(360 / sides)
    
    # Turtle 2 kreslí rotovaný vnitřní polygon
    t2.penup()
    t2.goto(x, y)
    t2.setheading(360 / (sides * 2))
    t2.pendown()
    t2.pensize(2)
    
    for _ in range(sides):
        t2.forward(size * 0.6)
        t2.right(360 / sides)
    
    # Turtle 1 kreslí diagonály
    t1.penup()
    t1.pensize(1)
    for i in range(sides):
        angle = (360 / sides) * i
        t1.goto(x, y)
        t1.setheading(angle)
        t1.pendown()
        t1.forward(size * 0.7)


def ornament_5_flower_bloom(screen, x, y, size, color_petal, color_center, color_stamen):
    """Ornament 5: Kvetoucí květina - tři želvy (okvětí, střed, tyčinky)."""
    t_petal = create_turtle(screen, color_petal)
    t_center = create_turtle(screen, color_center)
    t_stamen = create_turtle(screen, color_stamen)
    
    # Turtle 1: Okvětí (7 lístků)
    t_petal.penup()
    t_petal.pensize(3)
    petals = 7
    for i in range(petals):
        angle = (360 / petals) * i
        px = x + size * 0.7 * math.cos(math.radians(angle))
        py = y + size * 0.7 * math.sin(math.radians(angle))
        
        t_petal.goto(px, py)
        t_petal.setheading(angle)
        t_petal.pendown()
        t_petal.circle(size * 0.3, 180)
        t_petal.penup()
    
    # Turtle 2: Střed (velký kruh)
    t_center.penup()
    t_center.goto(x, y - size * 0.4)
    t_center.pendown()
    t_center.pensize(2)
    t_center.circle(size * 0.4)
    
    # Turtle 3: Tyčinky v centru
    t_stamen.penup()
    t_stamen.pensize(1)
    for i in range(12):
        angle = (360 / 12) * i
        t_stamen.goto(x, y)
        t_stamen.setheading(angle)
        t_stamen.pendown()
        t_stamen.forward(size * 0.3)
        t_stamen.penup()


def main():
    """Hlavní funkce - collaborative ornament kreslení."""
    screen = turtle.Screen()
    screen.setup(width=1400, height=900)
    screen.bgcolor(PALETTE["bg"])
    screen.title("Unikátní Ornámenty - Collaborative Turtle")
    screen.tracer(0, 0)
    
    print("Kreslení ornamentů...")
    
    # Ornament 1: Mandala
    ornament_1_mandala(screen, -500, 300, 80, PALETTE["accent1"], PALETTE["accent4"])
    
    # Ornament 2: Fraktální strom
    ornament_2_fractal_tree(screen, 0, 250, 60, 90, 8, PALETTE["accent5"], PALETTE["accent2"])
    
    # Ornament 3: Spirální galaxie
    ornament_3_spiral_galaxy(screen, 500, 300, 100, PALETTE["accent3"], PALETTE["accent6"], PALETTE["accent1"])
    
    # Ornament 4: Geometrický tanec
    ornament_4_geometric_dance(screen, -500, -100, 70, PALETTE["accent2"], PALETTE["accent3"])
    
    # Ornament 5: Kvetoucí květina
    ornament_5_flower_bloom(screen, 0, -150, 80, PALETTE["accent4"], PALETTE["accent5"], PALETTE["accent6"])
    
    # Ornament 6: Další spirála (bonus)
    t_spiral = create_turtle(screen, PALETTE["accent1"])
    t_spiral.penup()
    t_spiral.goto(500, -150)
    t_spiral.pendown()
    t_spiral.pensize(2)
    for i in range(300):
        step = 100 * i / 300
        t_spiral.forward(step / 25)
        t_spiral.right(8)
    
    screen.update()
    print("Ornámenty nakresleny! Klikni na obrazovku pro výstup.")
    screen.exitonclick()


if __name__ == "__main__":
    main()

