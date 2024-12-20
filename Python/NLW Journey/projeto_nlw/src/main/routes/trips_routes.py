from flask import jsonify, Blueprint, request

#Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

#Repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

#Settings
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trip_repository=trips_repository, emails_repository=emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripID>", methods=["GET"])
def find_trip(tripID):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository=trips_repository)

    response = controller.find_trip_details(tripID)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/confirm/<tripID>", methods=["PATCH"])
def confirm_trip(tripID):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripConfirmer(trip_repository)
    
    response = controller.confirm(tripID)
    
    return jsonify(response["body"]), response["status_code"]