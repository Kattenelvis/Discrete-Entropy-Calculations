from turtle import distance
import matplotlib.pyplot as plt

def display_distance_matrix(distance_matrix):

    x_size = len(distance_matrix)
    y_size = len(distance_matrix[0])

    fig, ax = plt.subplots()
    im = ax.imshow(distance_matrix)
    for x in range(x_size):
        for y in range(y_size):
            text = ax.text(x, y, distance_matrix[y][x],
                        ha="center", va="center", color="w")
    fig.tight_layout()
    plt.show()