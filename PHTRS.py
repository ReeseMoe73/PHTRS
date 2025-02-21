# Represents the pothole reported
class Pothole:

    def __init__(self, pothole_id, street_address, size, location, district, repair_priority):
        # Initialize pothole attributes
        self.pothole_id = pothole_id
        self.street_address = street_address
        self.size = size
        self.location = location
        self.district = district
        self.repair_priority = repair_priority
        self.work_order = None
        self.damage_file = None

    # Method to create a work order for pothole
    def create_work_order(self, work_order):
        self.work_order = work_order

    # Method to create a damage file
    def create_damage_file(self, damage_file):
        self.damage_file = damage_file


class WorkOrder:
    # Represents a work order
    def __init__(self, pothole_location, pothole_size, crew_id, crew_num_people, equipment_assigned, hours_applied,
                 hole_status, filler_material_used, repair_cost):
        # Initialize work order attributes
        self.pothole_location = pothole_location
        self.pothole_size = pothole_size
        self.crew_id = crew_id
        self.crew_num_people = crew_num_people
        self.equipment_assigned = equipment_assigned
        self.hours_applied = hours_applied
        self.hole_status = hole_status
        self.filler_material_used = filler_material_used
        self.repair_cost = repair_cost


class DamageFile:
    # Represents a damage file
    def __init__(self, name, address, phone_number, type_damage, damage_amount):
        # Initialize damage file attributes
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.type_damage = type_damage
        self.damage_amount = damage_amount


# Create a Pothole instance
pothole = Pothole(pothole_id=1, street_address="1234 Main St", size=5, location="side curb", district="Market District", repair_priority="Moderate")

# Create a WorkOrder instance
work_order = WorkOrder(pothole_location="1234 Main St", pothole_size=5, crew_id="Crew001", crew_num_people=6,
                       equipment_assigned=["Jackhammer", "Cement", "Steam Roller"], hours_applied=4,
                       hole_status="Work In Progress", filler_material_used="3", repair_cost=16000)

# Assign the work order
pothole.create_work_order(work_order)

# Create DamageFile instance
damage_file = DamageFile(name="John Smith", address="998 State St", phone_number="213-999-999",
                         type_damage="Front Wheel Alignment (Car)", damage_amount=1000)

# Create damage file
pothole.create_damage_file(damage_file)

# Display pothole information
print("Pothole Information:")
print("ID:", pothole.pothole_id)
print("Street Address:", pothole.street_address)
print("Size:", pothole.size)
print("Location:", pothole.location)
print("District:", pothole.district)
print("Repair Priority:", pothole.repair_priority)

# Display work order information
print("\nWork Order Information:")
print("Pothole Location:", pothole.work_order.pothole_location)
print("Pothole Size:", pothole.work_order.pothole_size)
print("Crew ID:", pothole.work_order.crew_id)
print("Number of People:", pothole.work_order.crew_num_people)
print("Equipment Assigned:", pothole.work_order.equipment_assigned)
print("Hours Applied:", pothole.work_order.hours_applied)
print("Hole Status:", pothole.work_order.hole_status)
print("Filler Material Used:", pothole.work_order.filler_material_used)
print("Repair Cost:", pothole.work_order.repair_cost)

# Display damage file information
print("\nDamage File Information:")
print("Citizen Name:", pothole.damage_file.name)
print("Citizen Address:", pothole.damage_file.address)
print("Phone Number:", pothole.damage_file.phone_number)
print("Damage Type:", pothole.damage_file.type_damage)
print("Damage Amount:", pothole.damage_file.damage_amount)