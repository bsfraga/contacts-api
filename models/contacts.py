
class Employer:
    def __init__(self, job_title: str, company: str):
        self.job_title = job_title
        self.company = company


class Location:
    def __init__(self, city: str, country: str):
        self.city = city
        self.country = country


class ContactModel(object):

    def __init__(self, first_name: str, last_name: str, email: str, location: Location, employer: Employer):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.employer = employer

    def __repr__(self):
        return f'Contact ({self.first_name}, {self.last_name}, {self.email}, {self.location}, {self.employer})'

    def __str__(self):
        return f'Contact ({self.first_name}, {self.last_name}, {self.email}, {self.location}, {self.employer})'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'location': self.location,
            'employer': self.employer
        }
