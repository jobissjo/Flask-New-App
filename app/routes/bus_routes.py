from flask import Blueprint, request, jsonify
from app.services.bus_services import BusService
from app.schemas.bus_schema import BusSchema, BusRouteSchema
from app import constants
from app.routes.bus_routes import bus_router

bus_router = Blueprint('bus', __name__)

bus_schema = BusSchema()
buses_schema = BusSchema(many=True)

bus_route_schema = BusRouteSchema()
bus_routes_schema = BusRouteSchema(many=True)




@bus_router.route("/buses", methods=['POST'])
def create_bus():
    try:
        data = request.get_json()
        if data:
            validated_data = bus_schema.load(data)
            bus = BusService.create_bus(validated_data)
            return jsonify(bus_schema.dump(bus)), 201
        else:
            return jsonify({"error": constants.BODY_NOT_PASSED}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bus_router.route('/buses', methods=['GET'])
def get_all_buses():
    buses = BusService.get_all_buses()
    return jsonify(buses_schema.dump(buses)), 200


@bus_router.route('/buses/<int:bus_id>', methods=['GET'])
def get_bus(bus_id):
    bus = BusService.get_bus_by_id(bus_id)
    if not bus:
        return jsonify({"error": constants.BUS_NOT_FOUND}), 404
    return jsonify(bus_schema.dump(bus)), 200

# Update Bus
@bus_router.route('/buses/<int:bus_id>', methods=['PUT'])
def update_bus(bus_id):
    try:
        data = request.get_json()
        if data:
            validated_data = bus_schema.load(data, partial=True)
            bus = BusService.update_bus(bus_id, validated_data)
            if not bus:
                return jsonify({"error": constants.BUS_NOT_FOUND}), 404
        
            return jsonify(bus_schema.dump(bus)), 200
        else:
            return jsonify({"error": "no body received"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete Bus
@bus_router.route('/buses/<int:bus_id>', methods=['DELETE'])
def delete_bus(bus_id):
    success = BusService.delete_bus(bus_id)
    if not success:
        return jsonify({"error": constants.BUS_NOT_FOUND}), 404
    return jsonify({"message": "Bus deleted successfully"}), 200


@bus_router.route('/route/<int:bus_id>', methods=['POST'])
def create_bus_route(bus_id):
    try:
        data = request.get_json()
        if data:
            validated_data = bus_route_schema.load(data)
            bus_route = BusService.create_bus_route(bus_id, validated_data)
            return jsonify(bus_route_schema.dump(bus_route)), 201
        else:
            return jsonify({"error": constants.BODY_NOT_PASSED}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400