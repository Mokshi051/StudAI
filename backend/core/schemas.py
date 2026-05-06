from marshmallow import Schema, fields, validate


class BurnoutPredictionSchema(Schema):
    current_cgpa = fields.Float(required=True, validate=validate.Range(min=0, max=10))
    assignment_score = fields.Float(required=True, validate=validate.Range(min=0, max=100))
    attendance_rate = fields.Float(required=True, validate=validate.Range(min=0, max=100))

    assignments_on_time = fields.Integer(required=True, validate=validate.Range(min=0))
    assignments_late = fields.Integer(required=True, validate=validate.Range(min=0))
    assignments_missing = fields.Integer(required=True, validate=validate.Range(min=0))

    hours_before_deadline = fields.Float(required=True)
    lms_logins = fields.Integer(required=True, validate=validate.Range(min=0))
    days_since_last_lms_login = fields.Integer(required=True, validate=validate.Range(min=0))

    library_visits = fields.Integer(required=True, validate=validate.Range(min=0))
    library_study_hours = fields.Float(required=True, validate=validate.Range(min=0))

    campus_activities = fields.Integer(required=True, validate=validate.Range(min=0))
    peer_interactions = fields.Integer(required=True, validate=validate.Range(min=0))

    stress_level = fields.Integer(required=True, validate=validate.Range(min=0, max=10))
    sleep_hours = fields.Float(required=True, validate=validate.Range(min=0, max=24))
    sleep_quality = fields.Integer(required=True, validate=validate.Range(min=0, max=10))