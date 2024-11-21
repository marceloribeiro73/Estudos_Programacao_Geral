from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, conn : Connection) -> None:
        self.__conn = conn

    def registry_activit(self, activit_infos: dict) -> None:
        """Insert a activit on database
        
        :param activit_infos: dict - The dict with the activit infos.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO activities
                    (id, trip_id, title, occurs_at)
                VALUES
                (?, ?, ?, ?)
            """, (
                activit_infos["id"],
                activit_infos["trip_id"],
                activit_infos["title"],
                activit_infos["occurs_at"]
            )
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> list[tuple]:
        """Finds the activities from a trip using tripID
        
        :param trip_id: str - The id from a trip.
        :return: List of tuples contain each activities on that trip 
        """ 
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT *
                FROM activities
                WHERE trip_id = ? 
            """, (trip_id,)
        )
        activities = cursor.fetchall()
        return activities
    