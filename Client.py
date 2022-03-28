from rsk import field_dimensions

# Field length (x axis)
field_dimensions.length
# Field width (y axis)
field_dimensions.width

# Goal width
field_dimensions.goal_width

# Side of the (green) border we should be able to see around the field
field_dimensions.border_size

def print_the_ball(client, dt):
    print(client.ball)

# This will print the ball everytime a new information is obtained from the client
client.on_update = print_the_ball

with rsk.Client() as client:

