from django import forms
from app.models import PostData
from ares_util.ares import call_ares
from validate_email import validate_email

class AddForm(forms.ModelForm):
    '''
    This is the form class. this will be render on main html page
    it consist all the parameters that we have added in model but we customized it according to our need
    '''
    name = forms.CharField(required=True)
    email = forms.CharField(required=False)
    ico = forms.CharField(required=True)
    
    def clean_ico(self):
        '''
        This function will validate ico value
        for this I have used the python library to validate ARES
        if its false than it will raise the validation error
        '''
        ico = self.cleaned_data['ico']
        if(call_ares(ico)==False):
            raise forms.ValidationError('**ICO is not valid')
        return ico

    def clean_email(self):
        '''
        this function is t validate email address
        if email is empty string it will pass because we can pass the email as per requirement
        otherwise it will check valid email or raise the validation error.
        '''
        email = self.cleaned_data['email']
        if(email!=""):
            is_valid = validate_email(email)
            if(is_valid == False):
                raise forms.ValidationError('**Email is not valid')
            return email
        else:
            return email
    
    class Meta:
        model = PostData
        fields = ['name', 'email', 'ico']
