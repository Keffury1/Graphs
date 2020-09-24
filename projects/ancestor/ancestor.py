
def earliest_ancestor(ancestors, starting_node, distance = 0):
    couple = dft_recursive(ancestors, starting_node, distance)

    if couple[0] == starting_node:
        return -1
    
    return couple[0]

def dft_recursive(ancestors, starting_node, distance):

    parents = []

    for couple in ancestors:
        if couple[1] == starting_node:
            parents.append(couple[0])

    couple = (starting_node, distance)

    for parent in parents:
        pair = dft_recursive(ancestors, parent, distance + 1)
        if pair[1] > couple[1]:
            couple = pair
    
    return couple