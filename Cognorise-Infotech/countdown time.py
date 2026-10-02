import time

def countdown(target_seconds):
  """
  This function takes the target seconds as input and displays a countdown on the screen.
  """
  while target_seconds > 0:
    minutes, seconds = divmod(target_seconds, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end="\n")
    time.sleep(1)
    target_seconds -= 1
  print("Time's Up!")

# Get the target time in seconds from the user
target_time_minutes = int(input("Enter the desired countdown time in minutes: "))
target_seconds = target_time_minutes * 60

# Start the countdown
countdown(target_seconds)
