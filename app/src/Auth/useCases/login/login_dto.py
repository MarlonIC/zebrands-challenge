class LoginDto:
    def __init__(self, **kwargs):
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
