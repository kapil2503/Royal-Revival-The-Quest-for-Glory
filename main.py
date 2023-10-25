import random
import time

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        time.sleep(1)
        enemy.take_damage(damage)

class Room:
    def __init__(self, name, description, item=None, enemy=None):
        self.name = name
        self.description = description
        self.item = item
        self.enemy = enemy
        self.locked = False

    def enter(self, player):
        if self.enemy and self.enemy.is_alive():
            print(f"You enter {self.name}. {self.description}")
            while self.enemy.is_alive() and player.is_alive():
                player.attack_enemy(self.enemy)
                if self.enemy.is_alive():
                    self.enemy.attack_enemy(player)
                if player.is_alive():
                    print(f"{player.name} has {player.health} health left.")
                if self.enemy.is_alive():
                    print(f"{self.enemy.name} has {self.enemy.health} health left.")
                else:
                    print(f"{self.enemy.name} has been defeated!")
                    if self.item:
                        print(f"You find a {self.item} in the room.")
                        player.inventory.append(self.item)
                        if self.item == "Silver Key":
                            print("You can now access Room 6.")
        elif not self.enemy:
            print(f"You enter {self.name}. {self.description}")
            if self.item:
                print(f"You find a {self.item} in the room.")
                player.inventory.append(self.item)
            self.locked = True

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

def main():
    player_name = input("Enter your character's name: ")
    player = Character(player_name, health=100, attack=20)
    player.inventory = []

    # Room descriptions
    room1_desc = "You see a dimly lit room with a flickering candle."
    room2_desc = "You enter a room with a cobweb-covered table."
    room3_desc = "You step into a chamber with a fearsome dragon."
    room4_desc = "A room with a shimmering sword."
    room5_desc = "You've entered a room with a shield."
    room6_desc = "This room contains a letter that describes how you are the heir to the royal family. " \
                "You were separated from the royal lineage by the malevolent Demon King. The letter also contains " \
                "a silver key and a clue to the puzzle in Room 7."
    room7_desc = "You enter a room with a peculiar inscription on the door that reads, 'I'm taken from a mine and " \
                "shut up in a wooden case, from which I am never released, and yet I am used by almost every person. " \
                "What am I?' Your mind races as you consider the possible answers to the riddle. In a corner, you notice " \
                "an inscription on a pedestal: 'A. A diamond\nB. A pen\nC. A watch\nD. A pencil'. The room has a " \
                "mysterious aura, and you sense that your choice will determine your fate. The inscription reminds you " \
                "of your royal lineage, cruelly separated from you by the Demon King. This quest is your chance to " \
                "reclaim your birthright."
    room8_desc = "As you push open the door, you find yourself in a vast, dimly lit chamber. At its center, a terrifying " \
                "creature, the Demon King, awaits. The Demon King's eyes gleam with malice, and you can feel its malevolent " \
                "energy filling the room. The fight ahead will be grueling, but you are prepared. Your Golden Sword, " \
                "radiant and powerful, fills you with newfound determination. The room seems to stretch on forever, the " \
                "Demon King at the far end, beckoning you to your destiny. You grip your sword, ready to face the ultimate " \
                "challenge. Victory is your only option."
    room8_defeat_desc = "Your heart sinks as the Demon King's malevolent power overwhelms you. Despite your bravery and " \
                        "determination, you couldn't prevail against the evil force. As your vision darkens, you feel the " \
                        "world slipping away from you. The kingdom remains under the shadow of the Demon King, and you " \
                        "couldn't change your tragic destiny. Do you want to start over and try again?"

    room1 = Room("Room 1", room1_desc, item="Key")
    room2 = Room("Room 2", room2_desc, item="Health Potion")
    room3 = Room("Room 3", room3_desc, enemy=Enemy("Dragon", health=100, attack=30))
    room4 = Room("Room 4", room4_desc, item="Sword")
    room5 = Room("Room 5", room5_desc, item="Shield")
    room6 = Room("Room 6", room6_desc, item="Letter")
    room7 = Room("Room 7", room7_desc, item="Golden Sword")
    room8 = Room("Room 8", room8_desc, enemy=Enemy("Demon King", health=200, attack=40))

    room1_prompt = f"1. {room1.description} (Press '1')"
    room2_prompt = f"2. {room2.description} (Press '2')"
    room3_prompt = f"3. {room3.description} (Press '3')"
    room4_prompt = f"4. {room4.description} (Press '4')"
    room5_prompt = f"5. {room5.description} (Press '5')"
    room6_prompt = f"6. {room6.description} (Press '6')"
    room7_prompt = f"7. {room7.description} (Press '7')"
    room8_prompt = f"8. {room8.description} (Press '8')"

    rooms = [room1, room2, room3, room4, room5, room6, room7, room8]

    current_room = None

    while player.is_alive():
        available_rooms = [room for room in rooms if not room.locked]

        if not available_rooms:
            print("You've explored all available rooms.")
            break

        options = "\n".join([f"{room.name} ({room.item})" for room in available_rooms])

        print(f"Available rooms:\n{options}\nTo quit, type 'quit'.")

        command = input(f"Choose your path:\n{room1_prompt}\n{room2_prompt}\n{room3_prompt}\n{room4_prompt}\n{room5_prompt}\n{room6_prompt}\n{room7_prompt}\n{room8_prompt}\nTo quit, type 'quit': ")

        if command == 'quit':
            break
        elif command in ['1', '2', '3', '4', '5', '6', '7', '8']:
            room_index = int(command) - 1
            if 0 <= room_index < len(rooms) and rooms[room_index] in available_rooms:
                current_room = rooms[room_index]
                current_room.enter(player)
                current_room.locked = True
            else:
                print("Invalid command. Choose an available room by entering its corresponding number.")
        else:
            print("Invalid command. Choose a room by entering 1, 2, 3, 4, 5, 6, 7, or 8.")

    if player.is_alive():
        print("Congratulations! You've explored all the available rooms and completed your quest.")
    else:
        print("Game over. Your character was defeated.")

if __name__ == "__main__":
    main()
