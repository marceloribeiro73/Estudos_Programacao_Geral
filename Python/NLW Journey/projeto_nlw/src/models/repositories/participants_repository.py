from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn : Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_infos: dict) -> None:
        """Insert a participant on database
        
        :param participant_infos: dict - The dict with the participant infos.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                (?, ?, ?, ?)
            """, (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"]
            )
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
        """Finds the participants from a trip using tripID
        
        :param trip_id: str - The id from a trip.
        :return: List of tuples contain each participant on that trip 
        """ 
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT p.id, p.name, e.email, p.trip_id
                FROM participants AS p
                JOIN emails_to_invite AS e ON p.emails_to_invite_id = e.id
                WHERE p.trip_id = ?
            """, (trip_id,)
        )
        participants = cursor.fetchall()
        return participants
    
    def confirm_a_participant_trip(self, participant_id :str, trip_id : str) -> None:
        """Update a register of a participant, change de value of is_confirmed to 1

        :param participant_id: str - Participant ID
        :param trip_id: str - Trip ID
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                UPDATE participants
                SET is_confirmed = 1
                WHERE trip_id = ?
                    AND id = ?
            """, (trip_id, participant_id,)
        )
        self.__conn.commit()
        