class LinkFinder:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def find_by_trip_id(self, trip_id: str) -> dict:
        try:
            links = self.__link_repository.find_links_from_trip(trip_id)
            if not links: raise Exception("No Trip Found")

            body = []
            for link in links:
                body.append({
                    "id": link[0],
                    "trip_id": link[1],
                    "link": link[2],
                    "title": link[3]
                })
            return {
                "body": {"links": tuple(body)}, "status_code": 200
            }
        except Exception as exception:
            return {
                "body": {"error":"Bad Request", "message": str(exception)},
                "status_code": 400
            }