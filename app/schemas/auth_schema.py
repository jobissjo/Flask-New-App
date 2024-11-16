from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=150))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=150))
    password = fields.Str(required=True, validate=validate. Length (min=3, max=150))

class UserBasicSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=150))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=150))