init offset = -1

# NOTE: setting 1 - the name to use for the save to be created for reloading
define who_input_save = "_who_input"
# NOTE: setting 2 - name of the argument in the say screen that will hold the input data
define who_input_data_key = "who_input_data"

init offset = 0

default _who_input_on_reload = None

init -1 python:
    class WhoInputCharacter(ADVCharacter):
        """A `Character` that allows storing an `InputValue` as its name."""

        def __init__(self, input_value, kind=None, *args, **kwargs):
            if input_value is renpy.character.NotSet and isinstance(kind, WhoInputCharacter):
                self.input_value = kind.input_value
            else:
                self.input_value = input_value
            self.input_value = self.input_value
            super().__init__(name=self.input_value.get_text, kind=kind, dynamic=True, *args, **kwargs)

    class WhoInputData():
        """The data for the `who_input` screen."""

        def __init__(self, input_value, prefix="", suffix=""):
            self._input_value = input_value
            self._prefix = prefix
            self._suffix = suffix
            self._old_text = self.input_value.get_text()

        @property
        def input_value(self):
            """Get the `InputValue`."""
            return self._input_value

        @property
        def activated(self):
            """Tell if the `InputValue` is currently active."""
            # https://github.com/renpy/renpy/blob/ec79a20c2ca0762c87d4aa2a049009e80a70de95/renpy/common/00action_file.rpy#L717-L719
            val, edi = renpy.get_editable_input_value()
            return (val is self.input_value) and edi

        @property
        def new_text(self):
            """Convenient property for getting the current text."""
            return self.input_value.get_text()

        @property
        def old_text(self):
            """Get the old text."""
            return self._old_text

        @property
        def prefix(self):
            """Get the prefix."""
            return self._prefix

        @property
        def suffix(self):
            """Get the suffix."""
            return self._suffix

        def update(self):
            """Update the old text to the current text."""
            self._old_text = self.new_text

        def discard(self):
            """Discard the current text and revert to the old text."""
            self.input_value.set_text(self.old_text)

        def Update(self):
            """Convenient `Action` for `update`."""
            return Function(self.update)

        def Discard(self):
            """Convenient `Action` for `discard`."""
            return Function(self.discard)

    def reload_who_input(action=None):
        """Reload after `who_input` change.

        This is useful for updating the `what` in the current `say` statement that contains Ren'Py interpolations of the `what_input`'s target variable.

        The `action` parameter is executed after reload.
        """
        global _who_input_on_reload
        _who_input_on_reload = action
        renpy.save(who_input_save)
        renpy.load(who_input_save)

    def _process_say_who_input(who, interact=True, *args, **kwargs):
        """Create the necessary data for `who_input` and retain after load."""
        kwargs["interact"] = interact
        if isinstance(who, WhoInputCharacter):
            kwargs[f"show_{who_input_data_key}"] = WhoInputData(
                who.input_value, who.who_prefix, who.who_suffix
            )
            renpy.retain_after_load()
        return args, kwargs

    def _combine_say_arguments_callback(*callbacks):
        """Combine multiple `config.say_arguments_callback` functions."""
        def combined(who, interact=True, *args, **kwargs):
            for callback in callbacks:
                args, kwargs = callback(who, interact, *args, **kwargs)
                interact = kwargs.pop("interact", True)
            kwargs["interact"] = interact
            return args, kwargs
        return combined

    if config.say_arguments_callback is None:
        config.say_arguments_callback = _process_say_who_input
    else:
        config.say_arguments_callback = _combine_say_arguments_callback(
            config.say_arguments_callback,
            _process_say_who_input,
        )

    def ReloadWhoInput(action=None):
        """Convenient `Action` for `reload_who_input`."""
        return Function(reload_who_input, action)

label _who_input_after_load:
    if renpy.can_load(who_input_save):
        python:
            if _who_input_on_reload:
                renpy.run(_who_input_on_reload)
                _who_input_on_reload = None
            renpy.unlink_save(who_input_save)
    return

style who_input_button is namebox

screen who_input_button(data, **properties):
    python:
        input_properties, button_properties = renpy.split_properties(properties, "input_", "")

    button id "namebox":
        action data.input_value.Toggle()
        style style.who_input_button
        properties button_properties

        who_input id "who":
            value data.input_value
            prefix renpy.substitute(data.prefix)
            suffix renpy.substitute(data.suffix)
            properties input_properties

screen who_input_key(data, key):
    if data.activated:
        key key action [data.Discard(), data.input_value.Disable()]