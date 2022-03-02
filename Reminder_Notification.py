# Reminder Application With Notification in Python.
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Sagar Please Drink Water Now!!",
            message = "Water Keeps Every System in the Body Functioning Properly. Your Body Depends on Water to Survive.",
            # message = "Water is your body's principal chemical component and makes up about 50% to 70% of your body weight.",
            app_icon = "D:\Python Projects\Glass.ico",
            timeout = 2
        )
        time.sleep(60*60)
        # time.sleep(7)