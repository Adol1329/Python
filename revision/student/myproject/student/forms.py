from django import forms


class ContactForm(forms.Form):

    first_name = forms.CharField(
        max_length=50,
        error_messages={
            "required": "Please enter your first name.",
            "max_length": "First name cannot exceed 50 characters.",
        }
    )

    last_name = forms.CharField(
        max_length=50,
        error_messages={
            "required": "Please enter your last name.",
            "max_length": "Last name cannot exceed 50 characters.",
        }
    )

    dob = forms.DateField(
        error_messages={
            "required": "Please enter your date of birth.",
            "invalid": "Please enter a valid date.",
        }
    )

    email = forms.EmailField(
        error_messages={
            "required": "Please enter your email address.",
            "invalid": "Please enter a valid email address.",
        }
    )

    def clean_dob(self):
        dob = self.cleaned_data["dob"]

        if dob >= date.today():
            raise forms.ValidationError(
                "Date of birth must be in the past."
            )

        return dob