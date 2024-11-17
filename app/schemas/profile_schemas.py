from marshmallow import Schema, fields, validate, ValidationError

class ProfileUpdateSchema(Schema):
    bio = fields.String(validate=validate.Length(max=500), allow_none=True)
    avatar_url = fields.String(validate=validate.Length(max=500), allow_none=True)
    dob = fields.Date(allow_none=True)
    gender = fields.String(
        validate=validate.OneOf(["Male", "Female", "Other", "Prefer not to say"]),
        allow_none=True
    )
    location = fields.String(validate=validate.Length(max=150), allow_none=True)