"""One Line, One Laugh entry.

The joke: Ken spends eight months training for a marathon and crosses the
finish line sobbing with triumph, then hugs the first stranger he sees in
gratitude. That stranger turns out to be the bus driver who picked him up
at mile 9. The hug is the tell: the tears are real, the marathon is not.
The last words flip the whole scene from a triumph into a fraud, and the
man he thanks is the very man who helped him cheat.
"""

ENTRY = "Ken trained 8 months for the marathon, crossed sobbing and hugged the nearest stranger: the bus driver who'd given him a lift at mile 9."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
