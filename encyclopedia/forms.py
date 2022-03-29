from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title",
    required = True,
    widget= forms.TextInput(attrs={'placeholder':'Enter Title','style':'bottom:1rem'}))

    content = forms.CharField(label="Markdown content",required= False,
    widget= forms.Textarea
    (attrs={'placeholder':'Enter markdown content','style':'top:2rem'}))