from src.Habit import *
import json

class DailyHabit(Habit):
    """
    Represents a daily habit that users can track and mark as completed.

    Parameters:
    - name (str): The name of the habit.
    - start_date (datetime): The start date of the habit.

    Attributes:
    - end_date (datetime): The end date of the habit.
    - streak_count (int): The count of consecutive days the habit has been completed.

    Inherits from:
    - Habit

    Methods:
    - calculate_end_date(start_date, frequency): Calculates the end date of the daily habit based on the start date and frequency.
    - mark_completed(completion_date=None): Marks the habit as completed for the specified date.
    - check_streak(target_streak): Checks if the habit has a streak of at least the specified number of consecutive days.
    - get_streak_count(): Gets the current streak count of the habit.
    """

    def __init__(self, name, start_date):
        """
        Initializes a DailyHabit object.

        Parameters:
        - name (str): The name of the habit.
        - start_date (datetime): The start date of the habit.
        """
        super().__init__(name, start_date)
        self.end_date = start_date
        self.streak_count = 0

    def calculate_end_date(self, start_date, frequency):
        """
        Calculates the end date of the daily habit based on the start date and frequency.

        Parameters:
        - start_date (datetime): The start date of the habit.
        - frequency (int): The frequency of the habit.

        Returns:
        datetime: The calculated end date of the habit.
        """
        return start_date

    def mark_completed(self, completion_date=None):
        """
        Marks the daily habit as completed for the specified date.

        Parameters:
        - completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        Raises:
        - ValueError: If the completion date is outside the habit period.

        Updates:
        - end_date: Updates the end date to the new completion date if it's a consecutive day.
        - streak_count: Increments the streak count or resets it based on consecutive completions.

        - Save the updated streak count when the habit is marked completed
        """
        if completion_date is None:
            completion_date = datetime.now().date()

        if completion_date == self.end_date:
            super().mark_completed(completion_date)
            self.streak_count += 1
        elif completion_date > self.end_date:
            # Check if the completion date is the day after the current end date (consecutive day)
            if (completion_date - self.end_date).days == 1:
                super().mark_completed(completion_date)
                self.streak_count += 1
                self.end_date = completion_date
            else:
                self.streak_count = 1  # Reset streak count if not consecutive
                super().mark_completed(completion_date)
                self.end_date = completion_date  # Update the end date to the new completion date
        else:
            raise ValueError("Completion date is outside the habit period.")

    def check_streak(self, target_streak):
        """
        Checks if the habit has a streak of at least the specified number of consecutive days.

        Parameters:
        - target_streak (int): The minimum required streak count.

        Returns:
        bool: True if the habit has a streak equal to or greater than the target_streak, False otherwise.
        """
        return self.streak_count >= target_streak

    def get_streak_count(self):
        """
        Gets the current streak count of the habit.

        Returns:
        int: The current streak count of the habit.
        """
        return self.streak_count
