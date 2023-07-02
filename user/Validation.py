from django.contrib.auth.models import User as UserModel

class User:
    @staticmethod
    def register(
        email,
        username,
        password1,
        password2,
        first_name = "",
        last_name = "",
    ):
        err_dict = {
            'e':False,
            'u':False,
            'p':False
        }
        
        if(
            not User.__validate_email(email) 
        ):
            err_dict.update(
                {'e':True}
            )

            
        if(not User.__validate_username(username)):
            err_dict.update(
                {'u':True}
            )
            
        if(not User.__validate_password(password1,password2)):
            err_dict.update(
                {'p':True}
            )
            
        if(err_dict['e']==False and err_dict['u']==False and err_dict['p']==False):
            return True
        return err_dict
            
            
        
    @staticmethod  
    def __validate_email(email):
        return not UserModel.objects.all().filter(email=email).exists()
    
    @staticmethod
    def __validate_username(username):
        return not UserModel.objects.all().filter(username=username).exists()
    
    @staticmethod
    def __validate_password(password1, password2):
        return password1==password2