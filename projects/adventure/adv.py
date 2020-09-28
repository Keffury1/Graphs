from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# # map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

world.print_rooms()

player = Player(world.starting_room)

traversal_path = []

opposites = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

previous = [None]

visited = {}

while len(visited) < len(room_graph) - 1:
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()

        if previous[-1]:
            visited[player.current_room.id].remove(previous[-1])
        
        else:
            continue

    while len(visited[player.current_room.id]) == 0:
        backward = previous.pop()
        traversal_path.append(backward)
        player.travel(backward)
    
    forward = visited[player.current_room.id].pop()
    traversal_path.append(forward)
    previous.append(opposites[forward])
    player.travel(forward)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
