from django import forms


class NameForm(forms.Form):
    word1 = forms.CharField(label="Английское слово", max_length=100)
    word2 = forms.CharField(label="Перевод на русский", max_length=100)