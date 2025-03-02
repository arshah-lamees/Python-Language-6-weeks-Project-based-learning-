class Student:
    def __init__(self, name, roll_number, marks):#constructor ,__init__(self) is the function that get called whenever we make a class and it is used to initialize the attribute of class, and self(can be of any name) parameter is used to access the attributes hence passed everyfunction of class along with other parameter if have any
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average()}")

# Example usage
def main():
    student1 = Student("arshah", "A1", [85, 90, 78, 92, 88])
    student1.display_details()

    student2 = Student("naveed", "B2", [76, 89, 95, 82, 91])
    student2.display_details()

main()
