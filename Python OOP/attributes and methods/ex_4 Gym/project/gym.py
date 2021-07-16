class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
    def subscription_info(self,subscription_id):
        current_sub = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if current_sub.customer_id == c.id][0]
        trainer =  [t for t in self.trainers if t.id == current_sub.id][0]
        plan = [p for p in self.plans if p.trainer_id == trainer.id][0]
        equipments = [eq for eq in self.equipment if eq.id == plan.equipment_id][0]

        return f"{current_sub}\n{customer}\n{trainer}\n{equipments}\n{plan}"



from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan

from project.subscription import Subscription
from project.trainer import Trainer
customer = Customer('John', 'Maple Street', 'john.smith@gmail.com')
equipment = Equipment('Treadmill')
trainer = Trainer('Peter')
subscription = Subscription('14.05.202', 1, 1, 1)
plan = ExercisePlan(1, 1, 20)
gym = Gym()
gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)
print(Customer.get_next_id())
print(gym.subscription_info(1))