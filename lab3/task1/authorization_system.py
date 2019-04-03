import hashlib

class User:

    def __init__(self, username, password):
        self._username = username
        self._password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        hasher = hashlib.sha256()
        hasher.update(bytes(password, encoding="utf-8"))
        return hasher.digest()

    def check_password(self, password):
        return True if self._password == self._encrypt_password(password) else False


class Authenticator:

    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists()
        elif len(password) <= 7:
            raise PasswordTooShort()
        else:
            self.users[username] = User(username, password)

    def login(self, username, password):
        if not username in self.users:
            raise IncorrectUsername()
        elif not self.users[username].check_password(password):
            raise IncorrectPassword()
        else:
            self.users[username].is_logged = True
            return True

    def is_logged_in(self, username):
        if not username in self.users:
            raise IncorrectUsername()
        else:
            return self.users[username].is_logged


class Authorizator:
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        if permission in self.permissions:
            raise PermissionError()
        else:
            self.permissions[permission] = []

    def permit_user(self, username, permission):
        if not username in self.authenticator.users:
            raise IncorrectUsername()
        elif not permission in self.permissions:
            raise PermissionError()
        else:
            self.permissions[permission].append(username)

    def check_permission(self, username, permission):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedError()
        elif not permission in self.permissions:
            raise PermissionError()
        elif not username in self.permissions[permission]:
            raise NotPermittedError()
        else:
            return True


class AuthenticationException(Exception):

    def __init__(self, username = None, user = None):
        self._username = username
        self._user = user


class PermissionError(Exception):
    pass

class NotPermittedError(AuthenticationException):
    pass

class UsernameAlreadyExists(AuthenticationException):
    pass

class PasswordTooShort(AuthenticationException):
    pass

class NotLoggedError(AuthenticationException):
    pass

class IncorrectUsername(AuthenticationException):
    pass

class IncorrectPassword(AuthenticationException):
    pass

# def setup():
authenticator = Authenticator()
authorizator = Authorizator(authenticator)
authenticator.add_user("Machina", "zaq1@WSX")
authenticator.add_user("TestUser", "iksde123")
authorizator.add_permission("test")
authorizator.add_permission("change")
authorizator.permit_user("Machina", "test")
authorizator.permit_user("TestUser", "change")
