from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from adventure.models import Player, Room
import random
import string
ROOM_NUMBERS = 100

class Command(BaseCommand):
    help = 'create rooms for MUD game'

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
        Room.objects.all().delete()

        # create grid matrix for rooms
        if (ROOM_NUMBERS % 10 == 0):
            grid = [[None] * int(ROOM_NUMBERS/10) for i in range(int(ROOM_NUMBERS/10))]
        else:
            print("ROOM_NUMBERS must be multiply of 10")
            return

        # Generate room title and description
        rooms = [None] * ROOM_NUMBERS
        room_title_list = [self.randomText() for i in range(ROOM_NUMBERS)]
        room_description_list = [self.randomText() + self.randomText() + self.randomText() for i in range(ROOM_NUMBERS)]
        for i in range(ROOM_NUMBERS):
            rooms[i] = Room(title="Pacman Digital Dot Coin Room Address: "+room_title_list[i], description="Public Key Hash: " + room_description_list[i])
            rooms[i].save()

# ##############################################################################
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0
        size_x = 10

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None
        while room_count < ROOM_NUMBERS:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
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

            # # Create a room
            room = rooms[-1]

            # Save the room in the World grid
            grid[y][x] = room
            room.x = x
            room.y = y

            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
                previous_room.save()
            room.save()
            rooms.pop()
            room_count += 1

        players=Player.objects.all()
        for p in players:
            p.currentRoom=grid[0][0].id
            p.save()