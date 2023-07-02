from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

class UserInitialiser():
    def __init__(self, user):
        self.__set_user_profile(user)
        
        
    def __set_user_profile(self, user):
        try:
            pf = user.profile
        except ObjectDoesNotExist:
            newpf = Profile(
                user = user,
                profile_picture='default.png'
            )
            newpf.save()
            
        else:
            return

    @staticmethod
    def set_user_profile_picture(url):
        pass
        