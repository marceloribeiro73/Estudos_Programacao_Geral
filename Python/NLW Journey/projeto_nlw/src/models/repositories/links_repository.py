from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def insert_link(self, link_infos: dict) -> None:
        """Insert a link on database.
        
        :param link_infos: dict - the link infos Exemple: {"id:"<id>","trip_id":"<trip_id>,"link":"<link>""}
        :return: None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO links
                    (id, trip_id, link)
                VALUES
                    (?, ?, ?)
            """, (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"]
            )
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id: str) -> list[tuple]:
        """Get links from a trip by trip_id
        
        :param trip_id: str - the id from a trip
        :return: List of tuples contain the links
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """ SELECT *
                FROM links
                WHERE trip_id = ?
            """, (trip_id,)
        )
        links = cursor.fetchall()
        return links