class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    # Overloading + operator
    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours

        # Convert extra minutes into hours
        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    def display(self):
        print(f"{self.hours} hrs {self.minutes} mins")

t1 = Time(3, 50)
t2 = Time(2, 20)

t3 = t1 + t2

t3.display()
