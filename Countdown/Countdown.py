import time
import sys

def countdown_timer(seconds):
    """Display a countdown timer from the given seconds to zero."""
    try:
        while seconds > 0:
            # Convert seconds to hours, minutes, seconds
            hrs, rem = divmod(seconds, 3600)
            mins, secs = divmod(rem, 60)
            print(f"\rTime remaining: {hrs:02}:{mins:02}:{secs:02}", end="")
            time.sleep(1)  # Wait for 1 second
            seconds -= 1
        print("\nTime's up!")
    except KeyboardInterrupt:
        print("\nCountdown aborted by the user.")
        sys.exit()

countdown_timer(5000)