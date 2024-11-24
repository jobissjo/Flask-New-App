from flask import Blueprint, request, jsonify
from app.services.bus_service import BusService
from app.schemas.bus_schema import BusSchema

bus_bp = Blueprint('bus', __name__)

# Initialize schemas
bus_schema = BusSchema()
buses_schema = BusSchema(many=True)

# Create Bus
@bus_bp.route('/buses', methods=['POST'])
def create_bus():
    try:
        data = request.json
        validated_data = bus_schema.load(data)
        bus = BusService.create_bus(validated_data)
        return jsonify(bus_schema.dump(bus)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get All Buses
@bus_bp.route('/buses', methods=['GET'])
def get_all_buses():
    buses = BusService.get_all_buses()
    return jsonify(buses_schema.dump(buses)), 200

# Get Bus by ID
@bus_bp.route('/buses/<int:bus_id>', methods=['GET'])
def get_bus(bus_id):
    bus = BusService.get_bus_by_id(bus_id)
    if not bus:
        return jsonify({"error": "Bus not found"}), 404
    return jsonify(bus_schema.dump(bus)), 200

# Update Bus
@bus_bp.route('/buses/<int:bus_id>', methods=['PUT'])
def update_bus(bus_id):
    try:
        data = request.json
        validated_data = bus_schema.load(data, partial=True)
        bus = BusService.update_bus(bus_id, validated_data)
        if not bus:
            return jsonify({"error": "Bus not found"}), 404
        return jsonify(bus_schema.dump(bus)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete Bus
@bus_bp.route('/buses/<int:bus_id>', methods=['DELETE'])
def delete_bus(bus_id):
    success = BusService.delete_bus(bus_id)
    if not success:
        return jsonify({"error": "Bus not found"}), 404
    return jsonify({"message": "Bus deleted successfully"}), 200