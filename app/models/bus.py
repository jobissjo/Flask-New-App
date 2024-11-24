from app import db

class Bus(db.Model):
    __tablename__ = 'buses'

    id = db.Column(db.Integer, primary_key=True)
    bus_number = db.Column(db.String(20), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('bus_routes.id'), nullable=True)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    bus_unique_id = db.Column(db.String(16), unique=True nullable=False)

    # Relationships
    route = db.relationship('BusRoute', back_populates='buses')

    def __repr__(self):
        return f"<Bus {self.bus_number} - {self.city} - {self.state} - {self.country}>"





class BusRoute(db.Model):
    __tablename__ = 'bus_routes'

    id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100), unique=True, nullable=False)
    start_location = db.Column(db.String(100), nullable=False)
    end_location = db.Column(db.String(100), nullable=False)
    
    # Relationships
    buses = db.relationship('Bus', back_populates='route', cascade='all, delete-orphan')
    stops = db.relationship('RouteStop', back_populates='route', order_by='RouteStop.order')

    def __repr__(self):
        return f"<BusRoute {self.route_name}>"
        

class RouteStop(db.Model):
    __tablename__ = 'route_stops'

    id = db.Column(db.Integer, primary_key=True)
    stop_name = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, nullable=False)  # To track the order of stops
    route_id = db.Column(db.Integer, db.ForeignKey('bus_routes.id'), nullable=False)

    # Relationships
    route = db.relationship('BusRoute', back_populates='stops')

    def __repr__(self):
        return f"<RouteStop {self.stop_name}, Order {self.order}>"