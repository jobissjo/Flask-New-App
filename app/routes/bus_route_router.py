from flask import Blueprint, request, jsonify
from app.services.bus_services import BusRouteService
from app.schemas.bus_schema import Bus, BusRou, BusRouteBusRouteSchema

bus_route_router = Blueprint('bus_route_router', __name__)

# Create a new bus route
@bus_route_router.route('/api/bus-routes', methods=['POST'])
def create_bus_route():
    data = request.get_json()
    route = BusRouteService.create_bus_route(data)
    bus_route_schema = BusRouteSchema()
    return bus_route_schema.dump(route), 201

# Get all bus routes
@bus_route_router.route('/api/bus-routes', methods=['GET'])
def get_bus_routes():
    routes = BusRouteService.get_bus_routes()
    bus_route_schema = BusRouteSchema(many=True)
    return bus_route_schema.dump(routes), 200

# Get bus route by ID
@bus_route_router.route('/api/bus-routes/<int:id>', methods=['GET'])
def get_bus_route_by_id(id):
    route = BusRouteService.get_bus_route_by_id(id)
    if not route:
        return jsonify({'message': 'Route not found'}), 404
    bus_route_schema = BusRouteSchema()
    return bus_route_schema.dump(route), 200

# Update bus route by ID
@bus_route_router.route('/api/bus-routes/<int:id>', methods=['PUT'])
def update_bus_route(id):
    data = request.get_json()
    updated_route = BusRouteService.update_bus_route(id, data)
    if not updated_route:
        return jsonify({'message': 'Route not found'}), 404
    bus_route_schema = BusRouteSchema()
    return bus_route_schema.dump(updated_route), 200

# Delete bus route by ID
@bus_route_router.route('/api/bus-routes/<int:id>', methods=['DELETE'])
def delete_bus_route(id):
    success = BusRouteService.delete_bus_route(id)
    if not success:
        return jsonify({'message': 'Route not found'}), 404
    return jsonify({'message': 'Route deleted successfully'}), 200
