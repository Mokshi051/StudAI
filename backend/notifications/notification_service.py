import random
import time
from plyer import notification
from datetime import datetime

# --------------------------
# USER SETTINGS
# --------------------------
QUIET_HOURS = (22, 7)  # 10 PM to 7 AM
MAX_NOTIFICATIONS_PER_DAY = 5
DELAY_BETWEEN_NOTIFICATIONS = 60 * 30  # 30 minutes

# --------------------------
# AFFIRMATIONS
# --------------------------
affirmations = [
    "You're doing better than you think.",
    "Start small. Progress will follow.",
    "Take a breath. You're allowed to pause.",
    "You handled more than you realize today.",
    "One step at a time is enough.",
    "You don't need to be perfect to move forward."
]

# --------------------------
# REMINDERS
# --------------------------
reminders = [
    "Drink some water 💧",
    "Stand up and stretch 🧍",
    "Take a short break 🧘",
    "Check your posture 👍"
]


def within_quiet_hours():
    current_hour = datetime.now().hour  # Fixed: was a broken markdown link
    start, end = QUIET_HOURS
    if start > end:
        return current_hour >= start or current_hour < end
    return start <= current_hour < end


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )


def get_random_affirmation():
    return random.choice(affirmations)


def get_random_reminder():
    return random.choice(reminders)


def run_notification_loop():
    """
    Run as a background thread from main entry point.
    Example:
        import threading
        from backend.notifications.notification_service import run_notification_loop
        t = threading.Thread(target=run_notification_loop, daemon=True)
        t.start()
    """
    notifications_sent_today = 0
    last_notification_time = 0

    print("Notification system started... Press CTRL+C to stop.")

    while True:
        current_time = time.time()

        if within_quiet_hours():
            time.sleep(60)
            continue

        if notifications_sent_today >= MAX_NOTIFICATIONS_PER_DAY:
            time.sleep(60)
            continue

        if current_time - last_notification_time >= DELAY_BETWEEN_NOTIFICATIONS:
            if notifications_sent_today % 2 == 0:
                message = get_random_reminder()
                title = "Reminder ⏰"
            else:
                message = get_random_affirmation()
                title = "Affirmation ✨"

            send_notification(title, message)
            notifications_sent_today += 1
            last_notification_time = current_time
            print(f"Sent: {title} - {message}")

        time.sleep(10)


if __name__ == "__main__":
    run_notification_loop()
