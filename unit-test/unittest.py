from datetime import datetime, timedelta
from src.habit_tracker import load_habits_from_json, save_habits_to_json
from src.DailyHabit import DailyHabit

def test_streak_count_update():
    # Create a temporary JSON file for testing
    test_json_filename = 'test_habits.json'

    # Load habits from the provided JSON data
    habits_data = [{"name": "Brush Teath Daily", "start_date": "2023-11-01T00:00:00", "completed_dates": ["2023-11-02", "2023-11-03"], "broken": False, "streak_count": 2}]
    habits = [DailyHabit(habit['name'], datetime.fromisoformat(habit['start_date'])) for habit in habits_data]
    for i, habit in enumerate(habits):
        habit.completed_dates = {datetime.fromisoformat(date).date() for date in habits_data[i]['completed_dates']}
        habit.broken = habits_data[i]['broken']
        setattr(habit, 'streak_count', habits_data[i]['streak_count'])

    # Save the habits to the temporary JSON file
    save_habits_to_json(habits, test_json_filename)

    # Load habits from the temporary JSON file
    loaded_habits = load_habits_from_json(test_json_filename)

    # Retrieve the habit to test
    brush_teeth_habit = next((habit for habit in loaded_habits if habit.name == 'Brush Teath Daily'), None)
    
    # Check if the streak count is updated correctly
    assert brush_teeth_habit.get_streak_count() == 2  # The streak count is expected to be 2

    # Print a success message if the test passes
    print("Unit test passed successfully!")

    # Clean up: Remove the temporary JSON file after testing
    import os
    os.remove(test_json_filename)

# Run the test
test_streak_count_update()
