import sys
import random

# Read names to array
f = open("SummonerNames.txt", "r")
names = f.read().strip().split("\n")  # Read all names
onlineNames = [name for name in names if name[-1] == '-'] # We only care about names who are online, '-'suffix attach to name means the users's online

if len(onlineNames)%2 != 0:
    print("Error: Size of team isn't even")
    sys.exit()

# Shuffle it
random.shuffle(onlineNames)

# Remove "-" suffixes the name indicating the user's online
onlineNamesPretty = [name[:-1] for name in onlineNames]

# Print result
midIdx = int(len(onlineNamesPretty) / 2)
print("Team 1: " + ", ".join(onlineNamesPretty[:midIdx]))
print("Team 2: " + ", ".join(onlineNamesPretty[midIdx:]))



