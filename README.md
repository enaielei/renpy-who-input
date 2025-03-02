# renpy-who-input
An editable Dialogue Speaker Name for Ren'Py.

## Demo
[![renpy who input demo](https://img.youtube.com/vi/6lnUsDlzEw8/0.jpg)](https://www.youtube.com/watch?v=6lnUsDlzEw8)

## Installation
1. Download a release: https://github.com/enaielei/renpy-who-input/releases/
2. Copy the contents of the release's `game` folder inside your project's `game` folder.
3. Create the input data inside your `say` screen: https://github.com/enaielei/renpy-who-input/blob/764ca7c753c51060cdc53de285f27e6f10fd2091/game/screens.rpy#L98-L99
4. Replace the namebox and text with the `who_input_button` displayable: https://github.com/enaielei/renpy-who-input/blob/764ca7c753c51060cdc53de285f27e6f10fd2091/game/screens.rpy#L105-L146
5. Optionally, provide a way for the user to discard unwanted changes through a hotkey: https://github.com/enaielei/renpy-who-input/blob/764ca7c753c51060cdc53de285f27e6f10fd2091/game/screens.rpy#L156-L160
6. In your `after_load` label, call `_who_input_after_load` label: https://github.com/enaielei/renpy-who-input/blob/764ca7c753c51060cdc53de285f27e6f10fd2091/game/script.rpy#L1-L5

## Usage
1. Initialize the variable that will hold the edited name for the character: https://github.com/enaielei/renpy-who-input/blob/764ca7c753c51060cdc53de285f27e6f10fd2091/game/script.rpy#L12-L13
2. Use that variable in an `InputValue` and pass that `InputValue` in the `WhoInputCharacter` instance: https://github.com/enaielei/renpy-who-input/blob/764ca7c753c51060cdc53de285f27e6f10fd2091/game/script.rpy#L14-L16
