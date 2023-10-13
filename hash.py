import bcrypt

# 3 hierarquias possiveis: admin, moderator e user

class UserControl():

    def __init__(self, username, password, role):

        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()

        if self.string2role(role) == -1:
             raise ValueError("Não foi possível definir a função do usuário. Favor utilizar as seguintes opções: admin, moderator ou user e certificar-se de utilizar letras minúsculas.")
    
        self.role = self.string2role(role)
        self.username = username.lower()
        self.hash = bcrypt.hashpw(bytes,salt);

        print (self.hash)


    def string2role(self, role):

        if role == "admin":
            return 1

        elif role == "moderator":
            return 2

        elif role == "user":
            return 3

        else :
            return -1
                  
    def password_verification(self, password):

        bytes = password.encode('utf-8')
        result = bcrypt.checkpw(bytes, self.hash)
        print(f' Is the password correct? {result}')

        return result
    
    def role_verification(self, role):

        result = self.string2role(role) == self.role
        print(f' Is the role correct? {result}')
        return result
    
user = UserControl("Leticia","password","admin")

user.password_verification("password")
user.role_verification("admin")

