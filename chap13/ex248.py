class PublicPrivateExample:
    def __init__(self):
        self.public = "безопасно"
        self.private = "опасно"

    def public_method(self):
        # Клиенты могут это использовать
        pass

    def _unsafe_method(self):
        # клиенты не должны это использовать
        pass
        self.public = "безопасно"
        self.private = "опасно"