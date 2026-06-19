from ai_contact_hub.domain.entities.contact import Contact


class ContactRepositoryImpl:

    def __init__(self, session):
        self.session = session

    def save(self, contact: Contact) -> Contact:

        model = Contact(
            name=contact.name,
            email=contact.email,
            phone=contact.phone,
            message=contact.message
        )
        self.session.add(model)
        self.session.flush()
        return model
