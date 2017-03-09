from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "lastname",
            "firstname",
            "skills",
            "Experience",
            "Designation",
            "currentsalary",
            "expectedsalary",
            "Noticeperiod",
            "Resume",
            "coverletter",
            "image",
            "profile_status"
        ]