from django import forms

class SudokuForm(forms.Form):
    def __init__(self, puzzle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(9):
            for j in range(9):
                value = puzzle[i][j]
                self.fields[f'cell_{i}_{j}'] = forms.CharField(
                    initial=value if value != 0 else '',
                    required=False,
                    max_length=1,
                    widget=forms.TextInput(attrs={
                        'class': 'cell',
                        'pattern': '[1-9]',  # Only digits 1-9 allowed
                        'inputmode': 'numeric',
                        **({'readonly': 'readonly'} if value != 0 else {}),
                    })
                )
