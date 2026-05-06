import random

def generate_timetable(
    profile,
    burnout_status,
    burnout_severity,
    lighten_workload=False,
    regenerate=False
):
    """
    profile.weekly_availability -> total hours available in a week
    burnout_status -> 'Low Risk' or 'At Risk'
    burnout_severity -> 'Very Low', 'Low', 'Moderate', 'High', 'Severe'
    lighten_workload -> user manually wants lighter plan
    regenerate -> reshuffle day distribution
    """

    total_hours = profile.weekly_availability

    # -------------------------------
    # Burnout-based adjustment
    # -------------------------------
    if burnout_status == "At Risk":
        if burnout_severity == "Severe":
            total_hours *= 0.5
        elif burnout_severity == "High":
            total_hours *= 0.6
        elif burnout_severity == "Moderate":
            total_hours *= 0.8
        elif burnout_severity == "Low":
            total_hours *= 0.9

    # -------------------------------
    # Manual workload reduction
    # -------------------------------
    if lighten_workload:
        total_hours *= 0.8  # extra 20% reduction

    total_hours = round(total_hours, 2)

    # -------------------------------
    # Weekly distribution
    # -------------------------------
    base_distribution = {
        "Monday": 0.15,
        "Tuesday": 0.15,
        "Wednesday": 0.20,
        "Thursday": 0.20,
        "Friday": 0.15,
        "Saturday": 0.10,
        "Sunday": 0.05
    }

    days = list(base_distribution.keys())
    weights = list(base_distribution.values())

    # -------------------------------
    # Regenerate option (reshuffle)
    # -------------------------------
    if regenerate:
        random.shuffle(weights)

    timetable = {}

    for day, weight in zip(days, weights):
        timetable[day] = round(total_hours * weight, 2)

    return {
        "total_weekly_hours": total_hours,
        "timetable": timetable,
        "lighten_workload": lighten_workload,
        "regenerated": regenerate
    }