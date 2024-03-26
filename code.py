import plotly.graph_objects as go

# Initial JSON data containing x and y coordinates
json_data = [
    [
        [1217, 1069], [1582, 1041], [1570, 68], [1597, -301], [1575, -659],
        [681, -659], [558, -591], [-1822, -540], [-1854, -404], [-1525, -354],
        [-1520, 362], [-1575, 400], [-1480, 490], [-1429, 455], [-1235, 367],
        [-362, 352], [-317, 425], [1097, 405], [976, 644], [1026, 672],
        [1172, 672], [1169, 961]
    ]
]

# Extract x and y coordinates from the JSON data
x_coords = [point[0] for point in json_data[0]]
y_coords = [point[1] for point in json_data[0]]

# Create a scatter plot with the initial coordinates
fig = go.Figure(data=go.Scatter(x=x_coords, y=y_coords, mode='lines+markers'))

# Define a callback function to update coordinates when clicking on the plot
def update_coordinates(trace, points, selector):
    x_new = points.xs[0]
    y_new = points.ys[0]
    index = points.point_inds[0]
    json_data[0][index] = [x_new, y_new]
    fig.update_traces(x=[coord[0] for coord in json_data[0]],
                      y=[coord[1] for coord in json_data[0]])

# Assign the callback function to the plot
fig.data[0].on_click(update_coordinates)

# Show the plot
fig.show()
