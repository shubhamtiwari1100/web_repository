from django import forms

class RegistrationForm(forms.Form):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # user_name = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # mobile = forms.IntegerField()
    # email = forms.EmailField()
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'First Name'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Last Name'
            }
        )
    )
    user_name = forms.CharField(
        label="Enter Your UserName",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'UserName'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Password'
            }
        )
    )
    mobile = forms.CharField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Email ID'
            }
        )
    )

class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="Enter Your UserName",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'User Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Password'
            }
        )
    )

class FeebackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )

from multiselectfield import MultiSelectFormField

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email ID'
            }
        )
    )
    COURSES_CHOICES = (
        ('Python', 'PYTHON'),
        ('Django', 'DJANGO'),
        ('Ui', 'UI'),
        ('RestAPI', 'REST API')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES,label="Select Required Courses"
                               )

    TRAINER_CHOICES = (
        ('Shubham', 'SHUBHAM'),
        ('Uttam', 'UTTAM'),
        ('Harun', 'HARUN')
    )
    trainers = MultiSelectFormField(choices=TRAINER_CHOICES, label="Select Your Trainers:")

    BRANCHES_CHOICES = (
        ('Pune', 'PUNE'),
        ('Mumbai', 'MUMBAI'),
        ('Hyd', 'HYDERABAD'),
        ('Bang', 'BANGALORE')
    )
    branches = MultiSelectFormField(choices=BRANCHES_CHOICES, label="Select Required Branches:")


    GENDER_CHOICES =(
        ('M','Male'),
        ('F','Female')
    )

    gender = forms.ChoiceField(
        widget=forms.RadioSelect,choices=GENDER_CHOICES,label="Select Your Gender:"
    )

    date = forms.DateField(
        widget=forms.SelectDateWidget(),label="Enter Your Date:"
    )