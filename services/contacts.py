# create a service class to handle business logic
from repository.contacts import ContactsRepository
from typing import List

class ContactsService:

    def __init__(self, repository):
        self.repository = ContactsRepository()

    def create_contact(self, contact: dict) -> str:
        contact_id = self.contacts_repo.create_contact(contact)
        return contact_id

    def get_contact(self, contact_id: str) -> dict:
        contact = self.contacts_repo.get_contact(contact_id)
        return contact

    def update_contact(self, contact_id: str, updates: dict) -> dict:
        contact = self.contacts_repo.update_contact(contact_id, updates)
        return contact

    def delete_contact(self, contact_id: str) -> None:
        self.contacts_repo.delete_contact(contact_id)

    def get_contacts_by_location(self, city: str, country: str) -> List[dict]:
        contacts = self.contacts_repo.get_contacts_by_location(city, country)
        return contacts