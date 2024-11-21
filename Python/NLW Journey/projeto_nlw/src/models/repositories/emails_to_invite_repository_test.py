import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
email_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interage com o banco de dados")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails_trips_info = {
        "id": email_id,
        "trip_id": trip_id,
        "email": "tester_1@contoso.com"
    }

    emails_to_invite_repository.registry_email(emails_trips_info)
    
@pytest.mark.skip(reason="interage com o banco de dados")
def test_find_email_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_email_from_trip(trip_id)

    print()
    print(emails)