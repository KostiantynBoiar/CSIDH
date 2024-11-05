import raylibpy as rl
from math import sin, cos, radians

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Define a grid size
GRID_SIZE = 50

# Node structure: a dictionary of nodes with their positions and connections
nodes = {
    "218*i + 21": {"pos": (100, 100), "connections": ["218*i + 21", "51*i + 30", "66*i + 39"]},
    "28": {"pos": (150, 200), "connections": ["196*i + 105", "167*i + 31", "8"]},
    "86*i + 227": {"pos": (200, 300), "connections": ["167*i + 31", "155*i + 3", "86*i + 227"]},
    "196*i + 105": {"pos": (250, 150), "connections": ["86*i + 227", "45*i + 211", "8"]},
    "155*i + 3": {"pos": (300, 100), "connections": ["86*i + 227", "74*i + 50", "86*i + 227"]},
    "23*i + 193": {"pos": (350, 250), "connections": ["64", "167*i + 31", "175*i + 237"]},
    "51*i + 30": {"pos": (400, 200), "connections": ["64", "155*i + 3", "8"]},
    "49*i + 112": {"pos": (450, 300), "connections": ["192*i + 18", "175*i + 237", "192*i + 18"]},
    "192*i + 18": {"pos": (500, 150), "connections": ["192*i + 18", "167*i + 31", "86*i + 227"]},
    "190*i + 183": {"pos": (550, 250), "connections": ["28", "167*i + 31", "175*i + 237"]},
    "45*i + 211": {"pos": (600, 100), "connections": ["218*i + 21", "155*i + 3", "175*i + 237"]},
    "8": {"pos": (650, 200), "connections": ["86*i + 227", "8", "155*i + 3"]},
    "175*i + 237": {"pos": (700, 300), "connections": ["66*i + 39", "192*i + 18", "196*i + 105"]},
    "64": {"pos": (750, 150), "connections": ["155*i + 3", "74*i + 50", "86*i + 227"]},
    "66*i + 39": {"pos": (800, 250), "connections": ["86*i + 227", "175*i + 237", "86*i + 227"]},
    "240": {"pos": (100, 400), "connections": ["74*i + 50", "86*i + 227", "74*i + 50"]},
    "74*i + 50": {"pos": (150, 350), "connections": ["218*i + 21", "8", "66*i + 39"]},
    "216": {"pos": (200, 450), "connections": ["155*i + 3", "155*i + 3", "74*i + 50"]},
    "93": {"pos": (250, 400), "connections": ["93", "8", "23*i + 193"]},
    "167*i + 31": {"pos": (300, 350), "connections": ["74*i + 50", "74*i + 50", "23*i + 193"]}
}


# Initialize raylib
rl.init_window(WIDTH, HEIGHT, "Simple Graph Builder")
rl.set_target_fps(60)

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        rl.draw_line(x, 0, x, HEIGHT, rl.LIGHTGRAY)
    for y in range(0, HEIGHT, GRID_SIZE):
        rl.draw_line(0, y, WIDTH, y, rl.LIGHTGRAY)

def draw_nodes():
    for node, data in nodes.items():
        # Draw the node as a circle
        x, y = data["pos"]
        rl.draw_circle(x, y, 10, rl.BLUE)
        # Draw the text inside the node
        rl.draw_text(node, x - 10, y - 25, 10, rl.DARKGRAY)

def draw_connections():
    for node, data in nodes.items():
        x1, y1 = data["pos"]
        for connection in data["connections"]:
            if connection in nodes:
                x2, y2 = nodes[connection]["pos"]
                # Draw line to connected node
                rl.draw_line(x1, y1, x2, y2, rl.RED)

# Main loop
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    # Draw grid, nodes, and connections
    draw_grid()
    draw_connections()
    draw_nodes()

    rl.end_drawing()

# Cleanup raylib
rl.close_window()
