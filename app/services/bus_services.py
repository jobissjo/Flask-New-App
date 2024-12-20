from app import db
from app.models.bus import Bus, BusRoute, RouteStop
from app.utils.common import get_country_code


class BusService:
    @staticmethod
    def generate_bus_unique_id(country, state, district, city, bus_number):
        # Extract max 3 characters from each component
        country_code, error = get_country_code(country)
        if error:
            country_code = country[:3].upper()
        state_code = state[:3].upper()
        district_code = district[:3].upper()
        city_code = city[:3].upper()

        # Concatenate to form the unique ID
        bus_unique_id = (
            f"{country_code}{state_code}{district_code}{city_code}{bus_number}"
        )

        # Ensure it doesn't exceed 16 characters
        return bus_unique_id[:16]

    @staticmethod
    def create_bus(data):
        # Generate bus_unique_id
        data["bus_unique_id"] = BusService.generate_bus_unique_id(
            country=data["country"],
            state=data["state"],
            district=data["district"],
            city=data["city"],
            bus_number=data["bus_number"],
        )
        # Check if bus_unique_id already exists
        if Bus.query.filter_by(bus_unique_id=data["bus_unique_id"]).first():
            raise ValueError("Bus unique ID already exists.")

        # Create and save the bus
        bus = Bus(**data)
        db.session.add(bus)
        db.session.commit()
        return bus

    @staticmethod
    def get_bus_by_id(bus_id):
        return Bus.query.get(bus_id)

    @staticmethod
    def get_all_buses():
        return Bus.query.all()

    @staticmethod
    def update_bus(bus_id, data):
        bus = Bus.query.get(bus_id)
        if not bus:
            return None
        for key, value in data.items():
            setattr(bus, key, value)
        db.session.commit()
        return bus

    @staticmethod
    def delete_bus(bus_id):
        bus = Bus.query.get(bus_id)
        if not bus:
            return False
        db.session.delete(bus)
        db.session.commit()
        return True



class BusRouteService:

    @staticmethod
    def create_bus_route(data):
        # Create a new BusRoute instance with the provided data
        route = BusRoute(**data)
        try:
            db.session.add(route)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            raise e
        return route

    @staticmethod
    def get_bus_routes():
        # Return all bus routes
        return BusRoute.query.all()

    @staticmethod
    def get_bus_route_by_id(route_id):
        # Fetch a bus route by its ID
        return BusRoute.query.get(route_id)

    @staticmethod
    def update_bus_route(route_id, data):
        # Fetch the bus route by its ID
        bus_route = BusRoute.query.get(route_id)
        if not bus_route:
            return None  # Return None if the route is not found
        try:
            for key, value in data.items():
                setattr(bus_route, key, value)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            raise e
        return bus_route

    @staticmethod
    def delete_bus_route(route_id):
        # Fetch the bus route by its ID
        bus_route = BusRoute.query.get(route_id)
        if not bus_route:
            return False  # Return False if the route is not found
        try:
            db.session.delete(bus_route)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            raise e
        return True  # Return True if the route was successfully deleted
