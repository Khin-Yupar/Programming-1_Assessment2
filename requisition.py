class Requisition:
    next_id = 10001

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def requisition_details(self, items):
        self.total = sum(items)
        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"
    def respond_requisition(self, decision):
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                self.approval_reference = (
                    self.staff_id + str(self.requisition_id)[-3:]
                )
            elif decision == "Not approved":
                self.status = "Not approved"

    def display_requisition(self):
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

    @staticmethod
    def requisition_statistics(requisitions):
        print("Displaying the Requisition Statistics")
        print("Total requisitions:", len(requisitions))
        print("Approved:", sum(r.status == "Approved" for r in requisitions))
        print("Pending:", sum(r.status == "Pending" for r in requisitions))
        print("Not approved:", sum(r.status == "Not approved" for r in requisitions))

r1 = Requisition("19/11/2026", "FN19", "Jenna Paul")
r1.requisition_details([200, 150, 100])
r1.approve_requisition()
r1.display_requisition()

r2 = Requisition("19/11/2026", "FN20", "Tracy Brown")
r2.requisition_details([600, 400])
r2.approve_requisition()
r2.display_requisition()

r3 = Requisition("19/11/2026", "FN15", "Emily Wellington")
r3.requisition_details([2000, 1500])
r3.approve_requisition()
r3.display_requisition()

r4 = Requisition("19/11/2026", "FN02", "Jennifer Summers")
r4.requisition_details([250, 240])
r4.approve_requisition()
r4.display_requisition()

r5 = Requisition("19/11/2026", "FN25", "Sarah Smith")
r5.requisition_details([300, 200])
r5.approve_requisition()
r5.display_requisition()

requisitions = [r1, r2, r3, r4, r5]
Requisition.requisition_statistics(requisitions)

r2.respond_requisition("Approved")
r3.respond_requisition("Not approved")

print("\nRequisitions after manager decisions:")

for requisition in requisitions:
    requisition.display_requisition()

print("\nUpdated Statistics:")
Requisition.requisition_statistics(requisitions)