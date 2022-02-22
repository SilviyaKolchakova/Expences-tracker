from django import forms


import os

from expenses_tracker.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        labels = {
            'budget': 'Budget',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image',

        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        labels = {
            'budget': 'Budget',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image',

        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        Expense.objects.all().delete()   # Delete all expenses when deleting the Profile
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'   # Q&A session- to be confirmed how to do it
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')