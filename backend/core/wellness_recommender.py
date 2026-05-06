def get_wellness_recommendations(burnout_status, burnout_severity):

    recommendations = {
        "sleep_hours": 7,
        "break_frequency": "Every 60 minutes",
        "exercise": "Light stretching",
        "hydration": "2-3 liters/day",
        "mindfulness": "5 minutes/day",
        "study_tip": "Maintain consistency"
    }

    if burnout_status == "At Risk":

        if burnout_severity == "Severe":
            recommendations.update({
                "sleep_hours": 9,
                "break_frequency": "Every 30 minutes",
                "exercise": "Short walks",
                "mindfulness": "15 minutes/day",
                "study_tip": "Reduce workload and focus on recovery"
            })

        elif burnout_severity == "High":
            recommendations.update({
                "sleep_hours": 8,
                "break_frequency": "Every 45 minutes",
                "exercise": "Yoga or stretching",
                "mindfulness": "10 minutes/day"
            })

        elif burnout_severity == "Moderate":
            recommendations.update({
                "sleep_hours": 7.5,
                "break_frequency": "Every 50 minutes"
            })

    return recommendations