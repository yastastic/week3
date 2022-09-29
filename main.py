#for xloc in range(50 , 1000, 80):
    #print(f"I want to draw a line at xposition: {xloc}")

#for countdown in range(10, 1, -1)
    #print(countdown)

import arcade

my_window = arcade.open_window(800, 600, "Graph paper")
arcade.set_background_color(arcade.color.JAPANESE_CARMINE)
arcade.start_render()
for xloc in range(50, 750, 80):
    arcade.draw_line(xloc, 50, xloc, 550, arcade.color.JASMINE, 5)
for yloc in range(50, 700, 80):
    arcade. draw_line(50, yloc, 550, yloc, arcade.color.CARMINE_PINK)

arcade.finish_render()
arcade.run()

