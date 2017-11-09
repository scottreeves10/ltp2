class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
        """ (Contact, str, str, str) -> NoneType
    
        Initialize this Contact with first name first_name, last name
        last_name, and email address email_address.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def add_phone_number(self, telephone_num): ## New method added by Question 3
        """ (Contact, str) -> NoneType

        Add phone number telephone_num for this contact.
        """

        self.phone_number = telephone_num

    def __str__(self): ##New method added by Question 6
        """ (Contact) -> str

        Return a string representation of this contact.
        """

        return '{0} {1} <{2}>'.format(self.first_name, self.last_name, self.email_address)

class Email: ## New Class added by Question 7
    """ An email with a list of recipients, a subject and a body. """

    def __init__(self, recipients, subject, body):
        """ (Email, list of Contact, str, str) -> NoneType

        Initialize this Email with recipients, subject and body.       """

        self.recipients = recipients
        self.subject = subject
        self.body = body

    def __str__(self): ##New method added by Question 8
        """ (Email) -> str

        Return a string representation of this email.
        """

        result = 'To: '
        for contact in self.recipients:
            result = result + '{0}, '.format(contact)

        result = result + '\nSubject: {0}'.format(self.subject)
        result = result + '\n{0}'.format(self.body)
        return result

## Question 1
## Select the code fragment(s) that create and initialize a
##Contact using the constructor (method __init__).

## -------------------------- YES below

'''paul = Contact('Paul', 'Gries', 'paul@example.com') #YES'''

## -------------------------- NO below

'''contact = Contact()
paul = Contact(contact, 'Paul', 'Gries', 'paul@example.com')

## NO - TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'email_address' '''

## -------------------------- NO below

'''
paul = Contact()

paul.first_name = 'Paul'

paul.last_name = 'Gries'

paul.email_address = 'paul@example.com'

## NO - TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'email_address'
'''

## -------------------------- NO below

'''
info = ['Paul', 'Gries', 'paul@example.com'] ## This is a list which is not a valid argument type

paul = Contact(info)

##NO - TypeError: __init__() missing 2 required positional arguments: 'last_name' and 'email_address'
'''
