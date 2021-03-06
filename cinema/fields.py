from django.core.exceptions import ValidationError
from django.forms import Field
from django.utils.translation import gettext as _

from cinema.widgets import LayoutWidget


class LayoutField(Field):
    """
        Represents dynamic layout field used by room.
    """
    rows = 0
    cols = 0
    widget = LayoutWidget

    def __init__(self, **kwargs):
        super(LayoutField, self).__init__(**kwargs)

    def validate(self, value):
        """
            Check if list contains only numbers and is not none.
        """
        try:
            for num in value:
                if num[0] > self.rows or num[1] > self.cols or num[0] < 0 or num[1] < 0:
                    raise ValidationError(_('Zaznaczono miejsce nie objemowane przez rozkład sali'))
        except TypeError:
            raise ValidationError(_('Niepoprawne wartości lub rozmiar sali'))

    def to_python(self, value):
        """
            Try to convert values in list to ints.
            If it cannot be done change value to None.
            If list is empty or invalid return None.
        """
        # print(value)
        raw_layout = value[0]
        self.rows = int(value[1])
        self.cols = int(value[2])
        if len(raw_layout) == 0:
            raise ValidationError(_('Sala nie może być pusta.'))
        if self.rows <= 0 or self.cols <= 0:
            raise ValidationError(_('Niepoprawny rozmiar sali. Ilość rzędów i kolumn musi być większa od zera.'))

        # Get minimal values to remove the offset
        min_row_index = min(map(lambda v: int(v) // self.cols, raw_layout))
        min_col_index = min(map(lambda v: int(v) % self.cols, raw_layout))

        layout = list()
        for pos in raw_layout:
            try:
                # Convert to int
                value = int(pos)
                # Get indices without offset
                row = value // self.cols + 1 - min_row_index
                col = value % self.cols + 1 - min_col_index
                # Create dict with real indices and labels
                layout.append((row, col))
            except ValueError or TypeError:
                raise ValidationError(_('Niepoprawne wartości.'))

        return layout
