class Contact:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.phone_number = input("Please enter your phone number: ")
        self.email = input("Enter email ID: ")
        self.website = input("You have a website? enter here please: ")
        self.birthday = input("When is your birthday?: ")
        self.linkedin = input("Enter Linkedin details: ")
        self.pictures = input("Place picture here:")

new_contact = Contact()
print (new_contact.name)
