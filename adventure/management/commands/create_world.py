from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from adventure.models import Player, Room
import random
import string

class Command(BaseCommand):
    help = 'create rooms for adventure app within django shell'

    def randomText(self):
        """Generate a random Text """
        source = string.ascii_letters + string.digits
        text = random.choice(string.ascii_lowercase)
        text += random.choice(string.ascii_uppercase)
        text += random.choice(string.digits)

        for i in range(30):
            text += random.choice(source)

        textList = list(text)
        random.SystemRandom().shuffle(textList)
        text = ''.join(textList)
        return text

    def handle(self, *args, **options):
        """initial executing component for BaseCommand"""
        ROOM_NUMBERS = 500
        MAP_WIDTH = 10
        MAP_HEIGHT = 100

        Room.objects.all().delete()

        # Create grid matrix for rooms
        if (ROOM_NUMBERS % 10 == 0):
            grid = [[None] * int(ROOM_NUMBERS/10) for i in range(int(ROOM_NUMBERS/10))]
        else:
            raise ValueError("ROOM_NUMBERS must be multiply of 10")

        # Generate room title and description
        rooms = [None] * ROOM_NUMBERS
        room_title_list = [self.randomText() for i in range(ROOM_NUMBERS)]
        room_description_list = [self.randomText() + self.randomText() + self.randomText() for i in range(ROOM_NUMBERS)]
        for i in range(ROOM_NUMBERS):
            # rooms[i] = Room(title=str(i),
            rooms[i] = Room(title="Pacman Digital Dot Coin Room Address: "+room_title_list[i], 
            description="Public Key Hash: " + room_description_list[i])
            rooms[i].save()
        
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0
        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}

        # While there are rooms to be created...
        previous_room = None
        while room_count < ROOM_NUMBERS:

            # Calculate the direction of the room to be created
            if direction > 0 and x < MAP_WIDTH - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "s"
                y += 1
                direction *= -1

            # Create a room
            room = rooms[-1]
            room.x = x
            room.y = y

            # Save the room in the World grid for player object
            grid[y][x] = room

            # Connect two room together (Zig Zag Pattern)
            if previous_room is not None:
                # randomize north south connection
                xConnect = set([random.randrange(1,MAP_WIDTH - 1) for i in range(5)])
                if direction < 0 and y > 0 and y < MAP_HEIGHT and x+1 in xConnect:
                    previous_room.connectRooms(grid[y-1][x+1], "s")
                    grid[y-1][x+1].connectRooms(previous_room, reverse_dirs["s"])

                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_dirs[room_direction])
                previous_room.save()
            room.save()
            rooms.pop()

            previous_room = room
            room_count += 1

        players=Player.objects.all()
        for p in players:
            p.currentRoom=grid[0][0].id
            p.save()