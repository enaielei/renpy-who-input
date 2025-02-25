init python early:
    class _WhoInput(Input):
        """An Input displayable that can be used in a say screen with `id` of `"who"`."""
        _NOT_SET = object()

        def __init__(self, *args, **kwargs):
            # https://github.com/renpy/renpy/blob/4804b04dcc744a7554e3213c11adc26d66f40de2/renpy/character.py#L992
            # pop the substitute keyword argument and set it later as this is
            # being passed by the character object
            substitute = kwargs.pop("substitute", self._NOT_SET)
            super().__init__(*args, **kwargs)
            if substitute is not self._NOT_SET:
                self.substitute = substitute

init python early hide:
    # NOTE: using a custom screen statement here due to the id
    # property being mapped to the displayable at runtime.
    # which means that we can't set the id via **kwargs
    sl = renpy.register_sl_displayable('who_input', _WhoInput, None)
    sl.copy_properties('input')