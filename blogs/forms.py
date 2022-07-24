from .models import  Comments  #, ReplyingComent
from django import forms

class COmmentForm(forms.ModelForm):
    class Meta:
        # comment_body = forms.CharField(widget=forms.Textarea, attrs={'class':'form-control input-mf','placeholder':'Add Comment'})
        model = Comments
        fields = ('comment_body',)
        
        widgets = {
            'comment_body':forms.Textarea(attrs={'class':'form-control input-mf',
                                                 'placeholder':'Add Comment'
                                                 
                                                 })
        }
        
        
# class ReplyComent(forms.ModelForm):
#     comment_body = forms.CharField( widget=forms.TextInput(attrs={"placeholder":"Reply comment", "class":"form-control"}) )
#     class Meta:
#         model = ReplyingComent
#         fields = ('comment_body',)
        
       
        