from pymongo import MongoClient
from bson.objectid import ObjectId


class ContactsRepository:
    def __init__(self, mongo_uri: str, database_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[database_name]
        self.contacts = self.db.contacts

    def create_contact(self, contact: dict) -> str:
        result = self.contacts.insert_one(contact)
        return str(result.inserted_id)

    def get_contact(self, contact_id: str) -> dict:
        contact = self.contacts.find_one({"_id": ObjectId(contact_id)})
        if contact:
            return contact
        else:
            raise ValueError(f"Contact with ID {contact_id} not found.")

    def update_contact(self, contact_id: str, updates: dict) -> dict:
        result = self.contacts.update_one({"_id": ObjectId(contact_id)}, {"$set": updates})
        if result.modified_count > 0:
            return self.get_contact(contact_id)
        else:
            raise ValueError(f"Contact with ID {contact_id} not found.")

    def delete_contact(self, contact_id: str) -> None:
        result = self.contacts.delete_one({"_id": ObjectId(contact_id)})
        if result.deleted_count == 0:
            raise ValueError(f"Contact with ID {contact_id} not found.")