init offset = -1

# NOTE: setting 1 - the name to use for the save to be created for reloading
define who_input_save = "_who_input"
# NOTE: setting 2 - whether to retain the updated name upon save on the point where it was edited
# if False, this will cause the updated name to be only saved starting the next
# say statement/dialogue and forward
define who_input_retained = True
define who_input_button_id_prefix = "who_button"

define _who_input_data_val_name = "val"
define _who_input_data_old_name = "old"

init offset = 0

default _who_input_on_reload = None

init -1 python:
    class WhoInputCharacter(ADVCharacter):
        """A `Character` that allows storing an `InputValue` as its name."""

        def __init__(self, input_value, *args, **kwargs):
            self.input_value = input_value
            super().__init__(name=self.input_value.get_text, dynamic=True, *args, **kwargs)

    def is_active_input(input_value):
        """Tell if an editable `InputValue` is currently active."""
        # https://github.com/renpy/renpy/blob/ec79a20c2ca0762c87d4aa2a049009e80a70de95/renpy/common/00action_file.rpy#L717-L719
        val, edi = renpy.get_editable_input_value()
        return (val is input_value) and edi

    def reload_who_input(action=None):
        """Reload after `who_input` change.

        This is useful for updating the `what` in the current `say` statement that contains Ren'Py interpolations of the `what_input`'s target variable.

        The `action` parameter is executed after reload.
        """
        global _who_input_on_reload
        _who_input_on_reload = action
        renpy.save(who_input_save)
        renpy.load(who_input_save)

    def create_who_input_data():
        """Create the data needed for `who_input`."""
        char = renpy.scry().who or narrator
        if isinstance(char, WhoInputCharacter):
            return {
                _who_input_data_val_name: char.input_value,
                _who_input_data_old_name: char.name(),
            }

    def _retain_who_input(statement):
        """Use `renpy.retain_after_load` before `say` statement's execution."""
        if statement == "say":
            renpy.retain_after_load()

    if who_input_retained:
        config.statement_callbacks.append(_retain_who_input)

    config.character_id_prefixes.append(who_input_button_id_prefix)

    def ReloadWhoInput(action=None):
        """Convenient `Action` for `reload_who_input`."""
        return Function(reload_who_input, action)

label _who_input_after_load:
    if renpy.can_load(who_input_save) and _who_input_on_reload:
        python:
            renpy.unlink_save(who_input_save)
            renpy.run(_who_input_on_reload)
            _who_input_on_reload = None
    return

style who_input_button is namebox

screen who_input_button(data, **properties):
    python:
        # properties prefixed with input_ will be treated as input properties,
        # otherwise as button properties
        input_properties, button_properties = renpy.split_properties(properties, "input_", "")
        who_val, who_old = data[_who_input_data_val_name], data[_who_input_data_old_name]
        who_new = who_val.get_text()

        # NOTE: setting 3 - what action to execute if the player entered an emtpy text?
        on_empty = Notify(_("Entered name is empty, reverted back to the original name."))
        # NOTE: setting 4 - what action to execute after updating the name?
        on_update = ReloadWhoInput(
            Notify(_('Name was changed from "{}" to "{}".').format(
                who_old,
                who_new,
            ))
        )

    button id "namebox":
        action who_val.Toggle()
        style "who_input_button"
        properties button_properties

        who_input id "who":
            value who_val
            action If(
                not who_new.strip(),
                [
                    Function(who_val.set_text, who_old),
                    who_val.Disable(),
                    on_empty,
                ],
                If(
                    who_old != who_new,
                    [
                        SetDict(data, _who_input_data_old_name, who_new),
                        who_val.Disable(),
                        on_update,
                    ],
                    who_val.Disable(),
                ),
            )
            properties input_properties

screen who_input_key(data, key):
    $ who_val, who_old = data[_who_input_data_val_name], data[_who_input_data_old_name]
    if is_active_input(who_val):
        key key action [Function(who_val.set_text, who_old), who_val.Disable()]