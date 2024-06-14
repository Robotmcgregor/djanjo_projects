from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Name needst to start with Z")
        

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # add a second email varification
    varify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    # # bot capture
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0),
    #                                          ])
    
    def clean(self):
        all_clean_data = super().clean()
        o_email = all_clean_data['email']
        v_email = all_clean_data['varify_email']
        
        
        if o_email != v_email:
            raise forms.ValidationError("Emails do not match, please try again.")

        
 # check for z valitator   
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     # bot capture
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0),
#                                              ])    
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
    