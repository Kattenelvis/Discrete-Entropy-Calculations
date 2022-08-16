def calculate_distance_matricies(ones, x_size, y_size):

    distance_matricies = []

    for one in ones:
        distance_matricies.append(calculate_distance_matrix(one, x_size, y_size))
    
    return distance_matricies

def calculate_distance_matrix(one, x_size, y_size):
    distance_matrix = [[0 for _ in range(x_size)] for _ in range(y_size)]
    for x in range(x_size):

            can_search_left = one[0] - x >= 0
            can_search_right = one[0] + x < x_size

            for y in range(y_size):
                can_search_higher = one[1] - y >= 0
                can_search_lower = one[1] + y < y_size

                if (can_search_left and can_search_higher):
                    distance_matrix[one[1] - y][one[0] - x] = x + y

                if (can_search_right and can_search_higher):
                    distance_matrix[one[1] - y][one[0] + x] = x + y

                if (can_search_left and can_search_lower):
                    distance_matrix[one[1] + y][one[0] - x] = x + y

                if (can_search_right and can_search_lower):
                    distance_matrix[one[1] + y][one[0] + x] = x + y

    return distance_matrix

def calculate_shortest_distance_matrix(distance_matricies):
    
    x_size = len(distance_matricies[0])
    y_size = len(distance_matricies[0][0])

    added_shortest_distances = 0
    shortest_distance_matrix = [[0 for _ in range(x_size)] for _ in range(y_size)]
    
    for x in range(x_size):
        for y in range(y_size):
            distances = [distance_matrix[y][x] for distance_matrix in distance_matricies]
            shortest_distance_matrix[y][x] = min(distances)
            added_shortest_distances += min(distances)

    return shortest_distance_matrix, added_shortest_distances


