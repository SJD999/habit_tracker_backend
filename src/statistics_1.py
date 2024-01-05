import pandas as pd
import matplotlib.pyplot as plt

from src.habit_tracker import load_habits_from_json, save_habits_to_json
from src.Habit import *
from src.DailyHabit import DailyHabit
from src.WeeklyHabit import WeeklyHabit
from src.MonthlyHabit import MonthlyHabit

def longest_habit_streak(habits):
    """
    Finds the longest streak among all daily habits.

    Parameters:
    - habits (list): List of Habit objects.

    Returns:
    int: The length of the longest streak among daily habits.
    """
    max_streak = 0
    for habit in habits:
        if isinstance(habit, DailyHabit):
            streak = habit.get_streak_count()
            if streak is None:
                continue
            max_streak = max(max_streak, streak)
    return max_streak

def current_daily_habits(habits):
    """
    Returns a list of names of currently tracked daily habits.

    Parameters:
    - habits (list): List of Habit objects.

    Returns:
    list: Names of currently tracked daily habits.
    """
    current_daily_habits = [habit.name for habit in habits if isinstance(habit, DailyHabit)]
    return current_daily_habits

def habits_struggled_last_month(habits):
    """
    Finds habits that were struggled with last month.

    Parameters:
    - habits (list): List of Habit objects.

    Returns:
    list: Names of habits that were struggled with last month.
    """
    last_month = datetime.now().replace(day=1) - timedelta(days=1)
    struggling_habits = []

    for habit in habits:
        if isinstance(habit, DailyHabit):
            last_month_completed_dates = [date for date in habit.completed_dates if date.month == last_month.month]
            if len(last_month_completed_dates) < habit.get_streak_count():
                struggling_habits.append(habit.name)

    return struggling_habits

def all_tracked_habits(habits):
    """
    Returns a list of names of all currently tracked habits.

    Parameters:
    - habits (list): List of Habit objects.

    Returns:
    list: Names of all currently tracked habits.
    """
    return [habit.name for habit in habits]

def habits_same_periodicity(habits, habit_type):
    """
    Returns a list of names of habits with the same periodicity.

    Parameters:
    - habits (list): List of Habit objects.
    - habit_type (type): Type of Habit (DailyHabit, WeeklyHabit, MonthlyHabit).

    Returns:
    list: Names of habits with the specified periodicity.
    """
    return [habit.name for habit in habits if isinstance(habit, habit_type)]

def longest_run_streak_all_habits(habits):
    """
    Finds the longest run streak among all habits.

    Parameters:
    - habits (list): List of Habit objects.

    Returns:
    int: The length of the longest run streak among all habits.
    """
    max_streak = 0
    for habit in habits:
        streak = habit.get_streak_count()
        max_streak = max(max_streak, streak)
    return max_streak

def longest_run_streak_for_habit(habit):
    """
    Finds the longest run streak for a specific habit.

    Parameters:
    - habit (Habit): A specific Habit object.

    Returns:
    int: The length of the longest run streak for the specified habit.
    """
    return habit.get_streak_count()

def load_habits():
    """
    Loads habits from a JSON file.

    Returns:
    list: List of Habit objects.
    """
    return load_habits_from_json('habits.json')

def create_habit_df(habits):
    """
    Creates a pandas DataFrame containing information about each habit.

    Parameters:
    - habits (list): List of Habit objects.

    Returns:
    pd.DataFrame: DataFrame with columns Name, Type, Start Date, End Date, Completed Dates, Streak Count, Broken.
    """
    habit_data_list = []
    for habit in habits:
        habit_data = {
            'Name': habit.name,
            'Type': type(habit).__name__,
            'Start Date': habit.start_date,
            'End Date': habit.end_date,
            'Completed Dates': len(habit.completed_dates),
            'Streak Count': getattr(habit, 'streak_count', None),
            'Broken': habit.check_break_status()
        }
        habit_data_list.append(habit_data)
    return pd.DataFrame(habit_data_list)

def visualize_completed_dates(habit_df):
    """
    Visualizes the number of completed dates for each habit using a bar chart.

    Parameters:
    - habit_df (pd.DataFrame): DataFrame with habit information.
    """
    habit_df.plot(kind='bar', x='Name', y='Completed Dates', legend=False)
    plt.title('Number of Completed Dates for Each Habit')
    plt.xlabel('Habit Name')
    plt.ylabel('Number of Completed Dates')
    plt.show()

def visualize_streak_count(daily_habits_df):
    """
    Visualizes the streak count for daily habits using a bar chart.

    Parameters:
    - daily_habits_df (pd.DataFrame): DataFrame with daily habit information.
    """
    daily_habits_df.plot(kind='bar', x='Name', y='Streak Count', legend=False)
    plt.title('Streak Count for Daily Habits')
    plt.xlabel('Habit Name')
    plt.ylabel('Streak Count')
    plt.show()

def visualize_broken_status(habit_df):
    """
    Visualizes the broken status for each habit using a bar chart.

    Parameters:
    - habit_df (pd.DataFrame): DataFrame with habit information.
    """
    habit_df['Broken'] = habit_df['Broken'].astype(int)
    habit_df.plot(kind='bar', x='Name', y='Broken', legend=False)
    plt.title('Broken Status for Each Habit')
    plt.xlabel('Habit Name')
    plt.ylabel('Broken (1 for True, 0 for False)')
    plt.show()
