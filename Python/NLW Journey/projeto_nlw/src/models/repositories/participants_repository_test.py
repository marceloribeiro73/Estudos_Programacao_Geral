import uuid
import pytest

#Settings
from src.models.settings.db_connection_handler import db_connection_handler

#Repositories
from src.models.repositories.participants_repository import ParticipantsRepository

db_connection_handler.connect()

trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())

def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    new_participant = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": str(uuid.uuid4()),
        "name": "tester Person one"
    }

    participant_repository.registry_participant(new_participant)

def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participant_repo = ParticipantsRepository(conn)

    participants = participant_repo.find_participants_from_trip(trip_id)

    print()
    print(participants)

    assert isinstance(participants,list)

def test_confirm_a_participant_trip():
    conn = db_connection_handler.get_connection()
    participant_repo = ParticipantsRepository(conn)

    participant_repo.confirm_a_participant_trip(participant_id,trip_id)