# NOTE: installation step 4 - in order for the ReloadWhoInput's action to work,
# call _who_input_after_load in your after_load label
label after_load:
    call _who_input_after_load
    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# NOTE: usage step 1 - create a default variable where the edited name will be stored
default e = "Eileen"
# NOTE: usage step 2 - use that variable name as the character's name and set the
# character to be dynamic
define character.e = Character("e", dynamic=True)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You can edit my name by clicking it.\nPress Enter to accept changes. Press ESC to discard changes.\nRight now my name is \"[e]\"."
    e "See? My new name \"[e]\" persisted even on this new line!\nYou can edit it anytime."

    return
