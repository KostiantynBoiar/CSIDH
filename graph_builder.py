import raylibpy as rl
# Define screen dimensions for Full HD
WIDTH = 1920
HEIGHT = 1080

# Set up grid parameters and scaling factor
GRID_SIZE = 10  # Base grid size
scale_factor = 1.0  # Start with a scaling factor of 1 (100%)

# Node structure with relative positioning
nodes = {'218*a + 21': {'pos': (386, 116), 'connections': ['218*a + 21', '167*a + 31', '23*a + 193', '192*a + 18']}, '28': {'pos': (1322, 837), 'connections': ['28', '8', '192*a + 18', '49*a + 112']}, '86*a + 227': {'pos': (985, 69), 'connections': ['86*a + 227', '8', '66*a + 39', '196*a + 105']}, '196*a + 105': {'pos': (1018, 232), 'connections': ['196*a + 105', '167*a + 31', '86*a + 227', '190*a + 183']}, '155*a + 3': {'pos': (174, 562), 'connections': ['155*a + 3', '45*a + 211', '8', '175*a + 237']}, '23*a + 193': {'pos': (1525, 825), 'connections': ['23*a + 193', '218*a + 21', '74*a + 50', '49*a + 112']}, '51*a + 30': {'pos': (1031, 508), 'connections': ['51*a + 30', '45*a + 211', '93', '216']}, '49*a + 112': {'pos': (139, 906), 'connections': ['49*a + 112', '23*a + 193', '192*a + 18', '28']}, '192*a + 18': {'pos': (1056, 271), 'connections': ['192*a + 18', '28', '49*a + 112', '218*a + 21']}, '190*a + 183': {'pos': (302, 174), 'connections': ['190*a + 183', '196*a + 105', '93', '216']}, '45*a + 211': {'pos': (865, 738), 'connections': ['45*a + 211', '51*a + 30', '74*a + 50', '155*a + 3']}, '8': {'pos': (488, 649), 'connections': ['8', '28', '155*a + 3', '86*a + 227']}, '175*a + 237': {'pos': (1178, 250), 'connections': ['175*a + 237', '66*a + 39', '155*a + 3', '64']}, '64': {'pos': (925, 591), 'connections': ['64', '216', '175*a + 237', '66*a + 39']}, '66*a + 39': {'pos': (906, 316), 'connections': ['66*a + 39', '64', '175*a + 237', '86*a + 227']}, '240': {'pos': (1522, 298), 'connections': ['240', '240', '240', '93']}, '74*a + 50': {'pos': (1241, 534), 'connections': ['74*a + 50', '45*a + 211', '23*a + 193', '167*a + 31']}, '216': {'pos': (1448, 765), 'connections': ['216', '64', '51*a + 30', '190*a + 183']}, '93': {'pos': (1156, 894), 'connections': ['93', '240', '51*a + 30', '190*a + 183']}, '167*a + 31': {'pos': (1429, 61), 'connections': ['167*a + 31', '218*a + 21', '74*a + 50', '196*a + 105']}}


scroll_offset_x, scroll_offset_y = 0, 0

rl.init_window(WIDTH, HEIGHT, "Scalable and Scrollable Graph Builder")
rl.set_target_fps(60)

def draw_grid():
    """Draw grid lines with scaling and scrolling offsets."""
    scaled_grid_size = int(GRID_SIZE * scale_factor)
    # Adjust grid starting points based on scroll offset and scale factor
    start_x = -scroll_offset_x % scaled_grid_size
    start_y = -scroll_offset_y % scaled_grid_size
    
    for x in range(start_x, WIDTH, scaled_grid_size):
        rl.draw_line(x, 0, x, HEIGHT, rl.LIGHTGRAY)
    for y in range(start_y, HEIGHT, scaled_grid_size):
        rl.draw_line(0, y, WIDTH, y, rl.LIGHTGRAY)

def draw_nodes():
    """Draw each node as a circle with its label, with scaling and scrolling."""
    for node, data in nodes.items():
        # Scale and apply scroll offsets to node position
        x = int(data["pos"][0] * scale_factor) + scroll_offset_x
        y = int(data["pos"][1] * scale_factor) + scroll_offset_y
        
        # Draw the node as a circle
        rl.draw_circle(x, y, int(10 * scale_factor), rl.BLUE)
        
        # Draw the text above the node
        rl.draw_text(node, x - int(10 * scale_factor), y - int(25 * scale_factor), int(10 * scale_factor), rl.DARKGRAY)

def draw_connections():
    """Draw lines between connected nodes, with scaling and scrolling."""
    for node, data in nodes.items():
        # Scale and apply scroll offsets to the start node position
        x1 = int(data["pos"][0] * scale_factor) + scroll_offset_x
        y1 = int(data["pos"][1] * scale_factor) + scroll_offset_y
        for connection in data["connections"]:
            if connection in nodes:
                # Scale and apply scroll offsets to the connected node position
                x2 = int(nodes[connection]["pos"][0] * scale_factor) + scroll_offset_x
                y2 = int(nodes[connection]["pos"][1] * scale_factor) + scroll_offset_y
                # Draw a line to the connected node
                rl.draw_line(x1, y1, x2, y2, rl.RED)

# Main loop
while not rl.window_should_close():
    # Handle zoom controls (mouse wheel up to zoom in, down to zoom out)
    mouse_wheel_move = rl.get_mouse_wheel_move()
   
    # Scroll controls with arrow keys
    if rl.is_key_down(rl.KEY_RIGHT):
        scroll_offset_x -= 15
    if rl.is_key_down(rl.KEY_LEFT):
        scroll_offset_x += 15
    if rl.is_key_down(rl.KEY_DOWN):
        scroll_offset_y -= 15
    if rl.is_key_down(rl.KEY_UP):
        scroll_offset_y += 15

    # Zoom in or out
    if mouse_wheel_move > 0:
        scale_factor *= 1.1  # Zoom in
    elif mouse_wheel_move < 0:
        scale_factor *= 0.9  # Zoom out
    
    # Begin drawing
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    
    # Draw grid, nodes, and connections with scaling and scrolling
    draw_grid()
    draw_connections()
    draw_nodes()
    
    # End drawing
    rl.end_drawing()

# Cleanup raylib
rl.close_window()