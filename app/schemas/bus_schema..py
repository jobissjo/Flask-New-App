from marshmallow import Schema, fields, validate


class BusSchema(Schema):
    id = fields.Int(dump_only=True)
    bus_number = fields.Str(required=True, validate=validate.Length(max=20))
    capacity = fields.Int(required=True)
    route_id = fields.Int(allow_none=True)
    country = fields.Str(required=True, validate=validate.Length(max=100))
    state = fields.Str(required=True, validate=validate.Length(max=100))
    city = fields.Str(required=True, validate=validate.Length(max=100))
    bus_unique_id = fields.Str(required=True, validate=validate.Length(max=16))
    
    route = fields.Nested('BusRouteSchema', only=('id', 'route_name'), dump_only=True)


class BusRouteSchema(Schema):
    id = fields.Int(dump_only=True)
    route_name = fields.Str(required=True, validate=validate.Length(max=100))
    start_location = fields.Str(required=True, validate=validate.Length(max=100))
    end_location = fields.Str(required=True, validate=validate.Length(max=100))
    
    buses = fields.List(fields.Nested('BusSchema', only=('id', 'bus_number')), dump_only=True)
    stops = fields.List(fields.Nested('RouteStopSchema', only=('id', 'stop_name', 'order')), dump_only=True)


class RouteStopSchema(Schema):
    id = fields.Int(dump_only=True)
    stop_name = fields.Str(required=True, validate=validate.Length(max=100))
    order = fields.Int(required=True)
    route_id = fields.Int(required=True)
    
    route = fields.Nested('BusRouteSchema', only=('id', 'route_name'), dump_only=True)