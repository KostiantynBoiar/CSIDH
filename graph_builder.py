import raylibpy as rl
# Define screen dimensions for Full HD
WIDTH = 2000
HEIGHT = 1580

# Set up grid parameters and scaling factor
GRID_SIZE = 10  # Base grid size
scale_factor = 1.0  # Start with a scaling factor of 1 (100%)

# Node structure with relative positioning
nodes_5 = {'218*a + 21': {'pos': (1325, 525), 'connections': ['218*a + 21']}, '28': {'pos': (1305, 648), 'connections': ['28', '64', '64', '86*a + 227', '86*a + 227', '155*a + 3', '155*a + 3', '93', '93', '192*a + 18', '192*a + 18', '86*a + 227', '86*a + 227', '192*a + 18', '192*a + 18', '64', '64', '49*a + 112', '49*a + 112', '93', '93', '49*a + 112', '49*a + 112', '155*a + 3', '155*a + 3']}, '86*a + 227': {'pos': (1248, 760), 'connections': ['86*a + 227']}, '196*a + 105': {'pos': (1160, 848), 'connections': ['196*a + 105']}, '155*a + 3': {'pos': (1048, 905), 'connections': ['155*a + 3']}, '23*a + 193': {'pos': (925, 925), 'connections': ['23*a + 193']}, '51*a + 30': {'pos': (801, 905), 'connections': ['51*a + 30']}, '49*a + 112': {'pos': (689, 848), 'connections': ['49*a + 112']}, '192*a + 18': {'pos': (601, 760), 'connections': ['192*a + 18']}, '190*a + 183': {'pos': (544, 648), 'connections': ['190*a + 183']}, '45*a + 211': {'pos': (525, 525), 'connections': ['45*a + 211']}, '8': {'pos': (544, 401), 'connections': ['8']}, '175*a + 237': {'pos': (601, 289), 'connections': ['175*a + 237', '192*a + 18', '192*a + 18', '240', '240', '196*a + 105', '196*a + 105', '240', '240', '74*a + 50', '74*a + 50', '192*a + 18', '192*a + 18', '93', '93', '192*a + 18', '192*a + 18', '74*a + 50', '74*a + 50', '192*a + 18', '192*a + 18', '93', '93', '196*a + 105', '196*a + 105']}, '64': {'pos': (689, 201), 'connections': ['64']}, '66*a + 39': {'pos': (801, 144), 'connections': ['66*a + 39', '167*a + 31', '167*a + 31', '167*a + 31', '167*a + 31', '45*a + 211', '45*a + 211', '49*a + 112', '49*a + 112', '93', '93', '240', '240', '45*a + 211', '45*a + 211', '49*a + 112', '49*a + 112', '49*a + 112', '49*a + 112', '93', '93', '49*a + 112', '49*a + 112', '240', '240']}, '240': {'pos': (924, 125), 'connections': ['240', '64', '64', '175*a + 237', '175*a + 237', '86*a + 227', '86*a + 227', '66*a + 39', '66*a + 39', '155*a + 3', '155*a + 3', '8', '8', '66*a + 39', '66*a + 39', '86*a + 227', '86*a + 227', '8', '8', '175*a + 237', '175*a + 237', '64', '64', '155*a + 3', '155*a + 3']}, '74*a + 50': {'pos': (1048, 144), 'connections': ['74*a + 50', '196*a + 105', '196*a + 105', '51*a + 30', '51*a + 30', '51*a + 30', '51*a + 30', '175*a + 237', '175*a + 237', '167*a + 31', '167*a + 31', '23*a + 193', '23*a + 193', '175*a + 237', '175*a + 237', '23*a + 193', '23*a + 193', '196*a + 105', '196*a + 105', '86*a + 227', '86*a + 227', '86*a + 227', '86*a + 227', '167*a + 31', '167*a + 31']}, '216': {'pos': (1160, 201), 'connections': ['216', '8', '8', '216', '216', '23*a + 193', '23*a + 193', '23*a + 193', '23*a + 193', '93', '93', '216', '216', '216', '216', '93', '93', '218*a + 21', '218*a + 21', '216', '216', '8', '8', '218*a + 21', '218*a + 21']}, '93': {'pos': (1248, 289), 'connections': ['93', '175*a + 237', '175*a + 237', '45*a + 211', '45*a + 211', '216', '216', '196*a + 105', '196*a + 105', '66*a + 39', '66*a + 39', '216', '216', '66*a + 39', '66*a + 39', '28', '28', '45*a + 211', '45*a + 211', '175*a + 237', '175*a + 237', '196*a + 105', '196*a + 105', '28', '28']}, '167*a + 31': {'pos': (1305, 401), 'connections': ['167*a + 31', '45*a + 211', '45*a + 211', '218*a + 21', '218*a + 21', '190*a + 183', '190*a + 183', '45*a + 211', '45*a + 211', '74*a + 50', '74*a + 50', '155*a + 3', '155*a + 3', '66*a + 39', '66*a + 39', '66*a + 39', '66*a + 39', '190*a + 183', '190*a + 183', '218*a + 21', '218*a + 21', '155*a + 3', '155*a + 3', '74*a + 50', '74*a + 50']}}
nodes_2 = {'218*a + 21': {'pos': (1325, 525), 'connections': ['218*a + 21', '167*a + 31', '23*a + 193', '192*a + 18']}, '28': {'pos': (1305, 648), 'connections': ['28', '8', '192*a + 18', '49*a + 112']}, '86*a + 227': {'pos': (1248, 760), 'connections': ['86*a + 227', '8', '66*a + 39', '196*a + 105']}, '196*a + 105': {'pos': (1160, 848), 'connections': ['196*a + 105', '167*a + 31', '86*a + 227', '190*a + 183']}, '155*a + 3': {'pos': (1048, 905), 'connections': ['155*a + 3', '45*a + 211', '8', '175*a + 237']}, '23*a + 193': {'pos': (925, 925), 'connections': ['23*a + 193', '218*a + 21', '74*a + 50', '49*a + 112']}, '51*a + 30': {'pos': (801, 905), 'connections': ['51*a + 30', '45*a + 211', '93', '216']}, '49*a + 112': {'pos': (689, 848), 'connections': ['49*a + 112', '23*a + 193', '192*a + 18', '28']}, '192*a + 18': {'pos': (601, 760), 'connections': ['192*a + 18', '28', '49*a + 112', '218*a + 21']}, '190*a + 183': {'pos': (544, 648), 'connections': ['190*a + 183', '196*a + 105', '93', '216']}, '45*a + 211': {'pos': (525, 525), 'connections': ['45*a + 211', '51*a + 30', '74*a + 50', '155*a + 3']}, '8': {'pos': (544, 401), 'connections': ['8', '28', '155*a + 3', '86*a + 227']}, '175*a + 237': {'pos': (601, 289), 'connections': ['175*a + 237', '66*a + 39', '155*a + 3', '64']}, '64': {'pos': (689, 201), 'connections': ['64', '216', '175*a + 237', '66*a + 39']}, '66*a + 39': {'pos': (801, 144), 'connections': ['66*a + 39', '64', '175*a + 237', '86*a + 227']}, '240': {'pos': (924, 125), 'connections': ['240', '240', '240', '93']}, '74*a + 50': {'pos': (1048, 144), 'connections': ['74*a + 50', '45*a + 211', '23*a + 193', '167*a + 31']}, '216': {'pos': (1160, 201), 'connections': ['216', '64', '51*a + 30', '190*a + 183']}, '93': {'pos': (1248, 289), 'connections': ['93', '240', '51*a + 30', '190*a + 183']}, '167*a + 31': {'pos': (1305, 401), 'connections': ['167*a + 31', '218*a + 21', '74*a + 50', '196*a + 105']}}
nodes_3 = {'218*a + 21': {'pos': (1325, 525), 'connections': ['218*a + 21']}, '28': {'pos': (1305, 648), 'connections': ['28', '93', '93', '155*a + 3', '155*a + 3', '93', '93', '86*a + 227', '86*a + 227']}, '86*a + 227': {'pos': (1248, 760), 'connections': ['86*a + 227']}, '196*a + 105': {'pos': (1160, 848), 'connections': ['196*a + 105']}, '155*a + 3': {'pos': (1048, 905), 'connections': ['155*a + 3']}, '23*a + 193': {'pos': (925, 925), 'connections': ['23*a + 193']}, '51*a + 30': {'pos': (801, 905), 'connections': ['51*a + 30']}, '49*a + 112': {'pos': (689, 848), 'connections': ['49*a + 112']}, '192*a + 18': {'pos': (601, 760), 'connections': ['192*a + 18']}, '190*a + 183': {'pos': (544, 648), 'connections': ['190*a + 183']}, '45*a + 211': {'pos': (525, 525), 'connections': ['45*a + 211']}, '8': {'pos': (544, 401), 'connections': ['8']}, '175*a + 237': {'pos': (601, 289), 'connections': ['175*a + 237', '49*a + 112', '49*a + 112', '167*a + 31', '167*a + 31', '66*a + 39', '66*a + 39', '64', '64']}, '64': {'pos': (689, 201), 'connections': ['64']}, '66*a + 39': {'pos': (801, 144), 'connections': ['66*a + 39', '175*a + 237', '175*a + 237', '64', '64', '74*a + 50', '74*a + 50', '192*a + 18', '192*a + 18']}, '240': {'pos': (924, 125), 'connections': ['240', '218*a + 21', '218*a + 21', '49*a + 112', '49*a + 112', '192*a + 18', '192*a + 18', '23*a + 193', '23*a + 193']}, '74*a + 50': {'pos': (1048, 144), 'connections': ['74*a + 50', '190*a + 183', '190*a + 183', '66*a + 39', '66*a + 39', '93', '93', '218*a + 21', '218*a + 21']}, '216': {'pos': (1160, 201), 'connections': ['216', '23*a + 193', '23*a + 193', '155*a + 3', '155*a + 3', '86*a + 227', '86*a + 227', '218*a + 21', '218*a + 21']}, '93': {'pos': (1248, 289), 'connections': ['93', '167*a + 31', '167*a + 31', '28', '28', '74*a + 50', '74*a + 50', '28', '28']}, '167*a + 31': {'pos': (1305, 401), 'connections': ['167*a + 31', '175*a + 237', '175*a + 237', '93', '93', '23*a + 193', '23*a + 193', '51*a + 30', '51*a + 30']}}
steps = {
    '49*a + 112': {'pos': (689, 848), 'connections': ['86*a + 227', '66*a + 39', '8']},
}

nodes_list = [nodes_5, nodes_3, nodes_2]
#nodes_list = [nodes_2, steps]

scroll_offset_x, scroll_offset_y = 0, 0

rl.init_window(WIDTH, HEIGHT, "Scalable and Scrollable Graph Builder")
rl.set_target_fps(60)

def draw_grid():
    """Draw grid lines with scaling and scrolling offsets."""
    scaled_grid_size = int(GRID_SIZE * scale_factor)
    # Adjust grid starting points based on scroll offset and scale factor
    start_x = -scroll_offset_x % scaled_grid_size
    start_y = -scroll_offset_y % scaled_grid_size
    i = 0
    grid_line_colours = [rl.WHITE, rl.LIGHTGRAY]
    if rl.is_key_down(rl.KEY_ENTER):
        i = 1 - i
        
    for x in range(start_x, WIDTH, scaled_grid_size):
        rl.draw_line(x, 0, x, HEIGHT, grid_line_colours[i])
    for y in range(start_y, HEIGHT, scaled_grid_size):
        rl.draw_line(0, y, WIDTH, y, grid_line_colours[i])

def draw_nodes():
    """Draw each node as a circle with its label, with scaling and scrolling."""
    for node, data in nodes_2.items():
        # Scale and apply scroll offsets to node position
        x = int(data["pos"][0] * scale_factor) + scroll_offset_x
        y = int(data["pos"][1] * scale_factor) + scroll_offset_y
        
        # Draw the node as a circle
        rl.draw_circle(x, y, int(10 * scale_factor), rl.BLUE)
        
        # Draw the text above the node
        rl.draw_text(node, x - int(10 * scale_factor), y - int(27 * scale_factor), int(20 * scale_factor), rl.DARKGRAY)

def draw_connections():
    """Draw lines between connected nodes, with scaling and scrolling."""
    i = 0
    colour_list = [rl.RED, rl.BLUE, rl.GREEN, rl.BLACK, rl.PURPLE]
    for nodes in nodes_list:
        for node, data in nodes.items():
            # Scale and apply scroll offsets to the start node position
            x1 = int(data["pos"][0] * scale_factor) + scroll_offset_x
            y1 = int(data["pos"][1] * scale_factor) + scroll_offset_y
            for connection in data["connections"]:
                if connection in nodes_5:
                    # Scale and apply scroll offsets to the connected node position
                    x2 = int(nodes_5[connection]["pos"][0] * scale_factor) + scroll_offset_x
                    y2 = int(nodes_5[connection]["pos"][1] * scale_factor) + scroll_offset_y
                    # Draw a line to the connected node
                    rl.draw_line(x1, y1, x2, y2, colour_list[i])
        i += 1
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