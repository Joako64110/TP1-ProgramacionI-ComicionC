class Contact:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def _str_(self):
        return f"{self.name} - {self.phone} - {self.email}"