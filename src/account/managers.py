from django.contrib.auth.base_user import BaseUserManager


class AnstoreUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        # Создание пользователя с логином, email и паролем 
        if username is None:
            raise TypeError('Пользователи должны иметь имя')

        if email is None:
            raise TypeError('Пользователи должны иметь адрес электронной почты')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        # Создание суперпользователя (администратора)
        if password is None:
            raise TypeError('Администратор должен иметь пароль')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
