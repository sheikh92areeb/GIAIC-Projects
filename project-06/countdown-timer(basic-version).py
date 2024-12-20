import time

def countdown_timer(seconds):
    print("Countdown Timer Started!")

    while seconds > 0:
        # Convert seconds into hours, minutes, and seconds
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60

        # Display the time in HH:MM:SS format
        print(f"{hrs:02}:{mins:02}:{secs:02}", end='\r')  # '\r' overwrites the line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("\nTime's up! 🚨")

# Get user input
try:
    total_seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Invalid input! Please enter an integer.")