import random
import string


class SequentialBind:
    def __init__(self, key) -> None:
        self.key = key
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def generate(self, cycle=False):
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        newline = '\n'

        output = f'alias "{id}" "{id}0"' + newline
        for i,command in enumerate(self.commands):
            output += f'alias "{id}{i}" "{command}; alias {id}{i} {id}{i+1}"' + newline

        last_alias = f"{id}0" if cycle else f"{id}{len(self.commands)-1}"
        output += f'alias "{id}{len(self.commands)-1}" "{last_alias}"' + newline
        output += f'bind "{self.key}" "{id}"' + newline
        return output

if __name__ == "__main__":
    bind = SequentialBind("o") # <- change the key here
    with open("input.txt", "r", encoding="UTF-8") as f:
        for line in f.readlines():
            line = line.strip()
            bind.add("say " + line)
    output = bind.generate(cycle=True)
    with open("output.txt", "w+", encoding="UTF-8") as f:
        f.write(output)
