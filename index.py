from distance_matricies import calculate_distance_matricies, calculate_shortest_distance_matrix, calculate_distance_matrix
from visualizations import display_distance_matrix


x_size = 4
y_size = 4
number_of_ones = 4
positions = [(x, y) for x in range(x_size) for y in range(y_size)]

distance_matricies = []
distance_matricies_average_distance = []
distance_matricies_average_distance_smallest = []

for position in positions:
    distance_matrix = calculate_distance_matrix(position, x_size, y_size)
    # distance_matricies.append(distance_matrix)
    average_distance = 0
    for x in range(len(distance_matrix)):
        for y in range(len(distance_matrix[0])):
            average_distance += distance_matrix[x][y]

    average_distance /= x_size * y_size - 1
    distance_matricies_average_distance.append(average_distance)

print(min(distance_matricies_average_distance))


ones = [(1,1)]


def main_loop():

    distance_matricies = calculate_distance_matricies(ones, x_size, y_size)

    shortest_distance_matrix, added_shortest_distances = calculate_shortest_distance_matrix(distance_matricies)

    average_distance = added_shortest_distances / (x_size * y_size - len(ones))

    print("Average distance is: ", average_distance)

    display_distance_matrix(shortest_distance_matrix)


# main_loop()