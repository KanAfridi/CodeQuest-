import os
import time
import sys


def countdown_timer(second):
    while second > 0:
        hrs, rem = divmod(second, 3600)
        mins, secs = divmod(rem, 60)
        print(f"\rTime remaining: {hrs:02}:{mins:02}:{secs:02}", end="") # \r use to execute the loop in a same line
        time.sleep(1)
        second -=1


while True:
    try:

        S_R_confirm = input("Restart or shut down the computer? (s/r): ").strip().lower()
        

        if S_R_confirm not in ["s", "r"]:  # Validates the user's action input
            print("Invalid input for timer. Please enter 'y' or 'n'.")
            continue

        timer = input("Do you want to set a timer? (y/n): ").strip().lower()
        if timer not in ["y", "n"]:
            print("Invalid input for timer. Please enter 'y' or 'n'.")
            continue

        if timer == "y":
            time_type = input("Set timer in minutes or hours? (m/h): ").strip().lower()

            if time_type == "h":  # Timer in hours
                askforhour = int(input("How many hours later? ").strip())
                if askforhour <= 0:
                    print("Please enter a value greater than 0.")
                    continue
                total_second = askforhour * 60 * 60
            elif time_type == "m":  # Timer in minutes
                askformin = int(input("How many minutes later? "))
                if askformin <= 0:
                    print("Please enter a value greater than 0.")
                    continue
                total_second = askformin * 60

            else:
                print("Invalid input for timer.")
                continue

            print(f"Starting countdown...")
            countdown_timer(total_second)  # Call countdown function

        # This else will shutdown the pc within one min if the timer = no
        else:
            # Confirmation before action
            confirm = input("Are you sure you want to shutdown or restart your pc? (y/n): ").strip().lower()
            if confirm == "y":

                #notimer_s_r = input("Restart : r or shutdown : s")
                if S_R_confirm == "s":
                    print("Your Pc will be shutdown in one minute or press crtl + c to end the operation")
                    countdown_timer(60)
                    os.system("shutdown /s /t 0")
                    break  # Exit the while loop

                else:
                    print("Your Pc will be Restart in one minute or press crtl + c to end the operation")
                    countdown_timer(60)
                    os.system("shutdown /s /t 0")
                    break  # Exit the while loop

            else:
                print("Action canceled. Exiting.")
                sys.exit()

    except KeyboardInterrupt:
        print("\nAction aborted by the user. Exiting.")
        sys.exit()
    except ValueError:
        print("Invalid input! Please enter numeric values for time.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
