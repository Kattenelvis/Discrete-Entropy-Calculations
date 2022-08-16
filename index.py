from json.encoder import INFINITY
from distance_matricies import calculate_distance_matricies, calculate_shortest_distance_matrix, calculate_distance_matrix
from visualizations import display_distance_matrix


x_size = 4
y_size = 4
number_of_ones = 4
positions = [(x, y) for x in range(x_size) for y in range(y_size)]

distance_matricies = []
distance_matricies_average = []
distance_matricies_average_largest = [(-INFINITY,0) for i in range(number_of_ones)]

for k, position in enumerate(positions):
    distance_matrix = calculate_distance_matrix(position, x_size, y_size)
    # distance_matricies.append(distance_matrix)
    average_distance = 0
    for x in range(len(distance_matrix)):
        for y in range(len(distance_matrix[0])):
            average_distance += distance_matrix[x][y]

    average_distance /= x_size * y_size - 1
    distance_matricies_average.append(average_distance)
    
    # All DMADS arrays have larger numbers first [5,4,3,2]
    # If a new distance shows up like 3.5 then it bubbles up to it's position
    #[4,3.5,3,2]
    if (average_distance > distance_matricies_average_largest[0][0]):
        distance_matricies_average_largest[0] = (average_distance, k)
        for i in range(1, number_of_ones):
            if average_distance > distance_matricies_average_largest[i][0]:
                distance_matricies_average_largest[i-1] = distance_matricies_average_largest[i]
                distance_matricies_average_largest[i] = (average_distance, k)
    

    print(distance_matricies_average_largest)

print(distance_matricies)

matricies_with_largest_average_distance = []
for distance_matrix in distance_matricies_average_largest:
    print(positions[distance_matrix[1]])
    matricies_with_largest_average_distance.append(positions[distance_matrix[1]])

calculate_shortest_distance_matrix(matricies_with_largest_average_distance)


ones = [(1,1)]


def main_loop():

    distance_matricies = calculate_distance_matricies(ones, x_size, y_size)

    shortest_distance_matrix, added_shortest_distances = calculate_shortest_distance_matrix(distance_matricies)

    average_distance = added_shortest_distances / (x_size * y_size - len(ones))

    print("Average distance is: ", average_distance)

    display_distance_matrix(shortest_distance_matrix)


# main_loop()