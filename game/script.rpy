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
# NOTE: usage step 2 - use that variable name in an InputValue and pass that to
# the WhoInputCharacter instance
define character.e = WhoInputCharacter(VariableInputValue("e", False))

define j = Character("Jake")

default h = "Hailee"
define character.h = WhoInputCharacter(
    VariableInputValue("h", False),
    # namebox style properties override the button style properties
    namebox_background="#0f01",
    # who style properties override the input style properties
    who_selected_color="#ffa600",
)

default m = "Mike"
define character.m = WhoInputCharacter(
    VariableInputValue("m", False),
    who_prefix="{size=-20}*{/size}",
    who_suffix="{size=-20}*{/size}",
)

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

    j "On the other hand, my name is [j] and it's not editable. Just a normal one."

    h "I'm another character with an editable name with just overriden styles."

    m "I'm [m], a character with a name that is editable and has a prefix and a suffix."

    "And I'm the narrator. I don't have a name."

    return
