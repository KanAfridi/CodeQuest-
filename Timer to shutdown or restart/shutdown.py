import os
import time
import sys

while True:

    try:
        # User input for action
        S_R_confirm = input("Restart or shut down the computer? (s/r): ").strip().lower()
        timer = input("Do you want to set a timer? (y/n): ").strip().lower()

        if S_R_confirm in ["s", "r"]:  # Validates the user's action input

            if timer == "y":
                time_type = input("Set timer in minutes or hours? (m/h): ").strip().lower()

                if time_type == "h":  # Timer in hours
                    askforhour = int(input("How many hours later? "))
                    time.sleep(askforhour * 60 * 60)
                    print(askforhour * 60 * 60)
                elif time_type == "m":  # Timer in minutes
                    askformin = int(input("How many minutes later? "))
                    time.sleep(askformin * 60)
                else:
                    print("Invalid input for timer. Exiting.")
                    exit() # sys.exit()

            # Confirmation before action
            confirm = input("Are you sure you want to proceed? (y/n): ").strip().lower()
            if confirm != "y":
                print("Action canceled. Exiting.")
                #sys.exit()

            # Execute shutdown or restart
            if S_R_confirm == "s":
                print("Your PC is going to shut down.")
                os.system("shutdown /s /t 0")  # Shutdown
            else:
                print("Your PC is going to restart.")
                os.system("shutdown /r /t 0")  # Restart
                break
        else:
            print("Invalid choice. Please select 's' for shutdown or 'r' for restart.")
            #exit()

    except KeyboardInterrupt:
        print("\nAction aborted by the user. Exiting.")
    except ValueError:
        print("Invalid input! Please enter numeric values for time.")
    except Exception as e:
        print(f"An error occurred: {e}")

            