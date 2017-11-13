class FacebookBackend(object):
    def authenticate(self, request, facebook_user_id):
        try:
            return User.objects.get(username='fb_{facebook_user_id}')
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None