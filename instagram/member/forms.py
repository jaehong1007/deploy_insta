from django import forms
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm

from member.models import User


# class SignupForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     age = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )
#
#     # clean_<field_name>
#     def clean_username(self):
#         data = self.cleaned_data['username']
#         # 유저가 존재하면 forms.ValidationError를 발생시킴
#         # 아니면 data를 리턴
#         if User.objects.filter(username=data).exists():
#             raise forms.ValidationError('오아ㅏ아아아아아')
#         return data
#
#     def clean_password2(self):
#         """
#         password, password2의 값이 같은지 비교
#         다르면 raise forms.ValidationError
#         :return:
#         """
#         # 이건 됨
#         password = self.cleaned_data['password']
#         password2 = self.cleaned_data['password2']
#         if password != password2:
#             raise forms.ValidationError('Password1 and Password2 not equal')
#         return password2
#
#     def clean(self):
#         if self.is_valid():
#             setattr(self, 'signup', self._signup)
#         return self.cleaned_data
#
#     def _signup(self):
#         """
#         User를 생성
#         :return:
#         """
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         age = self.cleaned_data['age']
#         return User.objects.create_user(
#             username=username,
#             password=password,
#             age=age,
#         )


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ('password1', 'password2')
        for field in class_update_fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'img_profile',
            'age',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'img_profile': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        self.user = authenticate(
            username=username,
            password=password
        )
        if not self.user:
            raise forms.ValidationError('Invalid login credentials')
        else:
            setattr(self, 'login', self._login)

    def _login(self, request):
        """

        :param request: django.contrib.auth.login()
        :return:
        """
        django_login(request, self.user)



