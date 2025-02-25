# renpy-who-input
An editable Dialogue Speaker Name for Ren'Py.

## Demo
[![renpy who input demo](https://img.youtube.com/vi/6lnUsDlzEw8/0.jpg)](https://www.youtube.com/watch?v=6lnUsDlzEw8)

## Installation
1. Download a release: https://github.com/enaielei/renpy-who-input/releases/
2. Copy the contents of the release's `game` folder inside your project's `game` folder.
3. Create the input data inside your `say` screen: https://github.com/enaielei/renpy-who-input/blob/0208be420bbb21a2cc5828618293caf06be2cb3c/game/screens.rpy#L99-L100
4. Replace the default `text` displayable with an `id` of `"who"` with the `who_input_button` displayable: https://github.com/enaielei/renpy-who-input/blob/0208be420bbb21a2cc5828618293caf06be2cb3c/game/screens.rpy#L111-L116
5. Optionally, provide a way for the user to discard unwanted changes through a hotkey: https://github.com/enaielei/renpy-who-input/blob/0208be420bbb21a2cc5828618293caf06be2cb3c/game/screens.rpy#L126-L129
6. In your `after_load` label, call `_who_input_after_load` label: https://github.com/enaielei/renpy-who-input/blob/0208be420bbb21a2cc5828618293caf06be2cb3c/game/script.rpy#L1-L5

## Usage
1. Initialize the variable that will hold the edited name for the character: https://github.com/enaielei/renpy-who-input/blob/0208be420bbb21a2cc5828618293caf06be2cb3c/game/script.rpy#L12-L13
2. Use that variable as the `Character` object's name and set it to be `dynamic`: https://github.com/enaielei/renpy-who-input/blob/0208be420bbb21a2cc5828618293caf06be2cb3c/game/script.rpy#L14-L16
