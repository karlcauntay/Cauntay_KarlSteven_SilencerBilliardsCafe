class SilencerBilliardsCafe:
    def __init__(self):
        self.available_tables = ["Table 1", "Table 2", "Table 3"]
        self.reserved_tables = []
        self.reserved_times = []
        self.equipment_list = ["Cue Stick", "Ball Set", "Chalk", "Triangle Rack"]
        self.rented_equipment = []
        self.returned_equipment = []

    def show_available_tables(self):
        print("Available Tables:")
        for table in self.available_tables:
            print(f"- {table}")

    def show_available_equipment(self):
        print("Available Equipment:")
        for equipment in self.equipment_list:
            print(f"- {equipment}")

    def show_time_cost(self):
        print("Time Cost:")
        print("1 hour = Php 250")
        print("30 minutes = Php 100")

    def make_reservation(self, tables, scanner):
        table_array = tables.split(",")
        for table in table_array:
            table = table.strip()
            if table in self.available_tables:
                self.available_tables.remove(table)
                self.reserved_tables.append(table)
                self.select_time_for_reservation(table, scanner)
            else:
                print(f"Sorry, {table} is not available.")

    def select_time_for_reservation(self, table, scanner):
        print(f"Select time to reserve for {table}:")
        print("1. 30 minutes (Php 100)")
        print("2. 1 hour (Php 250)")
        choice = int(scanner())
        time_in_minutes = 0
        if choice == 1:
            time_in_minutes = 30
        elif choice == 2:
            time_in_minutes = 60
        else:
            print("Invalid choice! Defaulting to 1 hour.")
            time_in_minutes = 60

        self.reserved_times.append(time_in_minutes)
        print(f"Reservation for {table} confirmed with {time_in_minutes} minutes.")

    def extend_reservation_time(self, scanner):
        if not self.reserved_tables:
            print("No reservations to extend.")
            return

        print("Reserved Tables and Times:")
        for i in range(len(self.reserved_tables)):
            print(f"- {self.reserved_tables[i]}: {self.reserved_times[i]} minutes")

        table = input("Enter the table you want to extend: ").strip()
        if table in self.reserved_tables:
            additional_time = int(input("Enter additional time to extend (30 or 60 minutes): ").strip())
            
            if additional_time == 30 or additional_time == 60:
                index = self.reserved_tables.index(table)
                self.reserved_times[index] += additional_time
                print(f"Time for {table} extended by {additional_time} minutes.")
            else:
                print("Invalid time. Only 30 or 60 minutes allowed.")
        else:
            print("Table not found in reserved list.")

    def calculate_payment(self):
        print("Payment Summary:")
        total_payment = 0
        for i in range(len(self.reserved_tables)):
            total_minutes = self.reserved_times[i]
            total_payment += (total_minutes // 60) * 250 + (total_minutes % 60 // 30) * 100
            print(f"{self.reserved_tables[i]}: {total_minutes} minutes -> Php {total_payment}")
        print(f"Total Payment: Php {total_payment}")

    def rent_equipment(self, scanner):
        print("Available Equipment to Rent:")
        for idx, equipment in enumerate(self.equipment_list, 1):
            print(f"{idx}. {equipment}")

        print("Enter the number(s) corresponding to the equipment you want to rent (separate with commas):")
        equipment_choices = scanner().strip().split(",")

        for choice in equipment_choices:
            try:
                choice = int(choice.strip())
                if 1 <= choice <= len(self.equipment_list):
                    equipment = self.equipment_list[choice - 1]
                    self.equipment_list.remove(equipment)
                    self.rented_equipment.append(equipment)
                    print(f"You have rented: {equipment}")
                else:
                    print("Invalid choice, that equipment is not available.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def return_equipment(self, scanner):
        if not self.rented_equipment:
            print("No equipment has been rented.")
            return

        print("Rented Equipment:")
        for equipment in self.rented_equipment:
            print(f"- {equipment}")

        equipment_to_return = input("Enter the equipment you want to return (separate with commas): ").strip()
        equipment_array = equipment_to_return.split(",")

        for equipment in equipment_array:
            equipment = equipment.strip()
            if equipment in self.rented_equipment:
                self.rented_equipment.remove(equipment)
                self.returned_equipment.append(equipment)
                self.equipment_list.append(equipment)
                print(f"Returned: {equipment}")
            else:
                print(f"You did not rent: {equipment}")

    def display_summary(self):
        print("\n--- Summary ---")

        if not self.reserved_tables:
            print("No reserved tables.")
        else:
            print("Reserved Tables and Times:")
            for i in range(len(self.reserved_tables)):
                print(f"- {self.reserved_tables[i]}: {self.reserved_times[i]} minutes")

        if not self.rented_equipment:
            print("No rented equipment.")
        else:
            print("Rented Equipment:")
            for equipment in self.rented_equipment:
                print(f"- {equipment}")

        if not self.returned_equipment:
            print("No returned equipment.")
        else:
            print("Returned Equipment:")
            for equipment in self.returned_equipment:
                print(f"- {equipment}")

        print("----------------")

def main():
    scanner = input
    cafe = SilencerBilliardsCafe()

    while True:
        print("\nWelcome to Silencer Billiards Cafe")
        print("1. View Available Tables")
        print("2. View Available Equipment")
        print("3. View Time Cost")
        print("4. Make a Reservation")
        print("5. Extend Reservation Time")
        print("6. Rent Equipment")
        print("7. Return Equipment")
        print("8. Calculate Payment")
        print("9. View Summary of Selections")
        print("10. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            cafe.show_available_tables()
        elif choice == 2:
            cafe.show_available_equipment()
        elif choice == 3:
            cafe.show_time_cost()
        elif choice == 4:
            cafe.show_available_tables()
            tables = input("Enter tables to reserve (separate with commas): ")
            cafe.make_reservation(tables, scanner)
        elif choice == 5:
            cafe.extend_reservation_time(scanner)
        elif choice == 6:
            cafe.rent_equipment(scanner)
        elif choice == 7:
            cafe.return_equipment(scanner)
        elif choice == 8:
            cafe.calculate_payment()
        elif choice == 9:
            cafe.display_summary()
        elif choice == 10:
            print("Thank you for using the Silencer Billiards Cafe system!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
