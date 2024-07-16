import time

def calculate_watch_time(episodes, minutes_per_episode, daily_hours=None, daily_minutes=None, skip_units=None):
    if skip_units is None:
        skip_units = []

    # Calculate total time in minutes
    total_minutes = episodes * minutes_per_episode
    
    # Calculate seconds, minutes, hours, days, weeks, months
    total_seconds = total_minutes * 60
    total_hours = total_minutes / 60
    total_days = total_hours / 24
    total_weeks = total_days / 7
    total_months = total_days / 30  # Approximation
    
    # Prepare the output
    time_units = [
        ('months', total_months),
        ('weeks', total_weeks),
        ('days', total_days),
        ('hours', total_hours),
        ('minutes', total_minutes),
        ('seconds', total_seconds)
    ]
    
    # Print the detailed results
    print("Total watch time:")
    for unit, value in time_units:
        if unit not in skip_units and value >= 1:
            print(f"{value:.2f} {unit}")
    
    # Calculate time if watching a certain number of hours or minutes per day
    if daily_hours is not None or daily_minutes is not None:
        if daily_hours is not None:
            daily_limit = daily_hours * 60
        else:
            daily_limit = daily_minutes
        
        total_days_limited = total_minutes / daily_limit
        total_weeks_limited = total_days_limited / 7
        total_months_limited = total_days_limited / 30
        
        # Prepare the limited time output
        limited_time_units = [
            ('months', total_months_limited),
            ('weeks', total_weeks_limited),
            ('days', total_days_limited),
            ('hours', total_days_limited * 24),
            ('minutes', total_days_limited * 24 * 60),
            ('seconds', total_days_limited * 24 * 60 * 60)
        ]
        
        # Print the limited time results
        print("\nIf you watch for a certain amount of time per day:")
        for unit, value in limited_time_units:
            if unit not in skip_units and value >= 1:
                print(f"{value:.2f} {unit}")

def main():
    while True:
        try:
            skip_units = []
            skip_detailed = input("Would you like to skip detailed time units? (y/n): ").strip().lower() == 'y'
            if skip_detailed:
                units = ['seconds', 'minutes', 'hours', 'days', 'weeks', 'months']
                for unit in units:
                    skip = input(f"Do you want to skip {unit}? (y/n): ").strip().lower() == 'y'
                    if skip:
                        skip_units.append(unit)

            episodes = int(input("Enter the number of episodes: "))
            minutes_per_episode = int(input("Enter the duration of each episode in minutes: "))
            
            daily_hours = None
            daily_minutes = None
            choice = input("Would you like to calculate based on a certain amount of watch time per day? (y/n): ").strip().lower()
            if choice == 'y':
                time_choice = input("Enter 'h' for hours per day or 'm' for minutes per day: ").strip().lower()
                if time_choice == 'h':
                    daily_hours = float(input("Enter the number of hours per day: "))
                elif time_choice == 'm':
                    daily_minutes = float(input("Enter the number of minutes per day: "))
            
            calculate_watch_time(episodes, minutes_per_episode, daily_hours, daily_minutes, skip_units)
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue
        
        print("\nTo quit the program, press 'q'.")
        print("Script made by KeiraOMG0, contact her @ keiraomg0 on Discord.")
        
        if input("Press any key to continue or 'q' to quit: ").strip().lower() == 'q':
            print("Closing in 5 seconds...")
            for i in range(5, 0, -1):
                print(f"{i}...", end=' ', flush=True)
                time.sleep(1)
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
