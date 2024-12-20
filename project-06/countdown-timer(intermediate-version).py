import time

def countdown_timer(seconds):
    print("Countdown Timer Started!")

    while seconds > 0:
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60

        print(f"{hrs:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nTime's up! 🚨")

# Accept input in HH:MM:SS format
def get_time_input():
    time_input = input("Enter the countdown time in HH:MM:SS format: ")
    try:
        hrs, mins, secs = map(int, time_input.split(":"))
        return hrs * 3600 + mins * 60 + secs
    except ValueError:
        print("Invalid time format! Please enter time as HH:MM:SS.")
        return None

total_seconds = None
while total_seconds is None:
    total_seconds = get_time_input()

countdown_timer(total_seconds)