"""
Created on 25th September 2024
@author: Mahima Gyamlani
Description: This program generates faces with different facial features (hair, eyes, nose, and mouth)
and allows for both fixed and random faces with customizable parts.
"""

import random

# Face part functions

def part_hair_pointy():
    """
    Returns a string for pointy hair.
    """
    a2 = r" /\/\/\/\/\/\/\/\ "
    return a2

def part_hair_plain():
    """
    Returns a string for plain hair.
    """
    a2 = r" ________________ " + "\n"
    a2 += r" ________________ "
    return a2

def part_hair_curly():
    """
    Returns a string for curly hair.
    """
    a2 = r"                  " + "\n"
    a2 += r" ~~~~~~~~~~~~~~~~ "
    return a2

def part_nose_up():
    """
    Returns a string for an upturned nose.
    """
    a = r" |      /\      | " + "\n"
    a += r" |     /  \     | " + "\n"
    a += r" |              | "
    return a

def part_nose_plain():
    """
    Returns a string for a plain nose.
    """
    a = r" |      |       | " + "\n"
    a += r" |      |       | "
    return a

def part_nose_large():
    """
    Returns a string for a large nose.
    """
    a = r" |      __      | " + "\n"
    a += r" |     /  \     | " + "\n"
    a += r" |    /____\    | "
    return a

def part_mouth_surprised():
    """
    Returns a string for a surprised mouth.
    """
    b = r" | |          | | " + "\n"
    b += r" | |__________| | "
    return b

def part_mouth_laughing():
    """
    Returns a string for a laughing mouth.
    """
    a = r" |              | " + "\n"
    a += r" |  \  ____  /  | " + "\n"
    a += r" |   \______/   | "
    return a

def part_mouth_smile():
    """
    Returns a string for a smiling mouth.
    """
    a = r" |              | " + "\n"
    a += r" |   \______/   | " + "\n"
    a += r" |              | "
    return a

def part_eyes_normal():
    """
    Returns a string for normal eyes.
    """
    c = r" /     \  /     \ " + "\n"
    c += r"    O   ||   O    " + "\n"
    c += r" \_____/  \_____/ "
    return c

def part_eyes_glasses():
    """
    Returns a string for eyes with glasses.
    """
    return r" |----O    O----| "

def part_eyes_closed():
    """
    Returns a string for closed eyes.
    """
    return r" |   --    --   | "

# Functions to print complete faces with fixed or customizable features

def funny_face():
    """
    Print a face with pointy hair, normal eyes, an upturned nose, and a surprised mouth.
    """
    print(part_hair_pointy())
    print(part_eyes_normal())
    print(part_nose_up())
    print(part_mouth_surprised())

def smiley_face():
    """
    Print a face with plain hair, glasses, a plain nose, and a smiling mouth.
    """
    print(part_hair_plain())
    print(part_eyes_glasses())
    print(part_nose_plain())
    print(part_mouth_smile())

def enjoying_face():
    """
    Print a face with curly hair, closed eyes, a large nose, and a laughing mouth.
    """
    print(part_hair_curly())
    print(part_eyes_closed())
    print(part_nose_large())
    print(part_mouth_laughing())

def faces_fixed():
    """
    Print a group of three fixed faces. Each face is predefined and remains the same
    every time the function is called.
    """
    smiley_face()
    funny_face()
    enjoying_face()

# Functions for customizable face parts

def face_with_eyes(eyefunc):
    """
    Print a face with customizable eyes based on the passed parameter.
    """
    print(part_hair_plain())      # Static hair part
    print(eyefunc())              # Call the eyes function passed as a parameter
    print(part_nose_plain())      # Static nose part
    print(part_mouth_smile())     # Static mouth part

def face_with_mouth(mouthfunc):
    """
    Print a face with customizable mouth based on the passed parameter.
    """
    print(part_hair_curly())      # Static hair part
    print(part_eyes_glasses())    # Static eyes part
    print(part_nose_large())      # Static nose part
    print(mouthfunc())            # Call the mouth function passed as a parameter

def face_with_hair(hairfunc):
    """
    Print a face with customizable hair based on the passed parameter.
    """
    print(hairfunc())             # Call the hair function passed as a parameter
    print(part_eyes_normal())     # Static eyes part
    print(part_nose_up())         # Static nose part
    print(part_mouth_smile())     # Static mouth part

def face_with_hair_and_mouth(hairfunc, mouthfunc):
    """
    Print a face with customizable hair and mouth based on the passed parameters.
    """
    print(hairfunc())             # Call the hair function passed as a parameter
    print(part_eyes_glasses())    # Static eyes part
    print(part_nose_plain())      # Static nose part
    print(mouthfunc())            # Call the mouth function passed as a parameter

# Selfie functions with a customized name band

def selfie_band():
    """
    Returns a string for the selfie band with the NetID mg595.
    """
    band = " +--------------+ " + "\n"
    band += " |mg595    mg595| " + "\n"
    band += " +--------------+ "
    return band

def selfie(hairfunc, mouthfunc):
    """
    Print a face with a selfie band, customizable hair, and mouth.
    """
    print(selfie_band())          # Print the selfie band
    print(hairfunc())             # Call the hair function passed as a parameter
    print(part_eyes_glasses())    # Static eyes part
    print(part_nose_plain())      # Static nose part
    print(mouthfunc())            # Call the mouth function passed as a parameter

def faces_selfie():
    """
    Print a group of three faces with selfie bands by calling the selfie() helper function.
    """
    selfie(part_hair_curly, part_mouth_laughing)
    selfie(part_hair_pointy, part_mouth_smile)
    selfie(part_hair_plain, part_mouth_surprised)

# Functions to print random faces

def face_random():
    """
    Generate and print a random face by randomly selecting hair, eyes, and mouth.
    """
    # Random hair
    hair_choice = random.randint(1, 3)
    if hair_choice == 1:
        hair = part_hair_curly
    elif hair_choice == 2:
        hair = part_hair_pointy
    else:
        hair = part_hair_plain

    # Random eyes
    eyes_choice = random.randint(1, 3)
    if eyes_choice == 1:
        eyes = part_eyes_glasses
    elif eyes_choice == 2:
        eyes = part_eyes_closed
    else:
        eyes = part_eyes_normal

    # Random mouth
    mouth_choice = random.randint(1, 3)
    if mouth_choice == 1:
        mouth = part_mouth_smile
    elif mouth_choice == 2:
        mouth = part_mouth_surprised
    else:
        mouth = part_mouth_laughing

    # Print the randomly chosen face parts
    face_with_hair_and_mouth(hair, mouth)

def faces_random():
    """
    Print a group of three random faces.
    """
    face_random()
    face_random()
    face_random()

# Main function to print different sets of faces

if __name__ == '__main__':
    print("\nFixed group of three faces\n")
    faces_fixed()

    print("\nGroup of three selfie faces\n")
    faces_selfie()

    print("\nGroup of three random faces\n")
    faces_random()
