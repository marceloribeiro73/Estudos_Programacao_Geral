from flask import jsonify, Blueprint, request

#Controllers
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

#Repositories
from src.models.repositories.links_repository import LinksRepository

#Settings
from src.models.settings.db_connection_handler import db_connection_handler

links_routes_bp = Blueprint("link_routes", __name__)

@links_routes_bp.route("/trips/<tripID>/links", methods=["POST"])
def create_link(tripID):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    link_controller = LinkCreator(link_repository)

    response = link_controller.create(request.json, tripID)

    return jsonify(response["body"]), response["status_code"]

@links_routes_bp.route("/trips/<tripID>/links", methods=["GET"])
def get_links(tripID):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    link_controller = LinkFinder(link_repository)

    response = link_controller.find_by_trip_id(tripID)

    return jsonify(response["body"]), response["status_code"]