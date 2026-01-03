'''Database initialization & utilities'''
from models import db
import random
from datetime import datetime, timedelta

'''
app parameter is the Flask application instance.
This function initializes the database with the Flask app context.
app_context is used to ensure that the database tables are created within the application context. 
It allows access to application-specific resources.
'''
def init_app(app): # Function to initialize database with Flask app
    db.init_app(app) # Initialize the db with the app

    with app.app_context(): # Use app context to create tables
        db.create_all() # Create all database tables
        print("Database initialized!")
def empty_db(): # Function to empty all tables in the database
    from models.health_models import Meal, Sleep, Steps, Weight

    Meal.query.delete()  # Delete all entries in Meal table
    Sleep.query.delete()  # Delete all entries in Sleep table
    Steps.query.delete()  # Delete all entries in Steps table
    Weight.query.delete()  # Delete all entries in Weight table
    db.session.commit()  # Commit the changes
    print("Database emptied!")

def sample_data(): # Function to add sample data to the database
    from models.health_models import Meal, Sleep, Steps, Weight
    
    # Only if tables are empty
    if Meal.query.first() is None:
        breakfast_options = [
            {'food': 'Oatmeal', 'calories': 150},
            {'food': 'Eggs and Toast', 'calories': 250},
            {'food': 'Smoothie', 'calories': 200},
            {'food': 'Pancakes', 'calories': 300},
            {'food': 'Yogurt and Fruit', 'calories': 180},
            {'food': 'Bagel with Cream Cheese', 'calories': 350},
            {'food': 'Cereal', 'calories': 220},
            {'food': 'French Toast', 'calories': 320},
            {'food': 'Breakfast Burrito', 'calories': 400},
            {'food': 'Waffles', 'calories': 300}
        ]

        lunch_options = [
            {'food': 'Chicken Salad', 'calories': 350},
            {'food': 'Turkey Sandwich', 'calories': 400},
            {'food': 'Veggie Wrap', 'calories': 300},
            {'food': 'Sushi', 'calories': 450},
            {'food': 'Pasta', 'calories': 500},
            {'food': 'Burger and Fries', 'calories': 700},
            {'food': 'Quinoa Bowl', 'calories': 400},
            {'food': 'Grilled Cheese', 'calories': 450},
            {'food': 'Caesar Salad', 'calories': 350},
            {'food': 'Tuna Sandwich', 'calories': 400}
        ]

        dinner_options = [
            {'food': 'Grilled Salmon', 'calories': 600},
            {'food': 'Steak and Veggies', 'calories': 700},
            {'food': 'Chicken Stir Fry', 'calories': 550},
            {'food': 'Tacos', 'calories': 650},
            {'food': 'Vegetable Curry', 'calories': 500},
            {'food': 'Spaghetti Bolognese', 'calories': 750},
            {'food': 'Roast Chicken', 'calories': 600},
            {'food': 'Beef Stew', 'calories': 700},
            {'food': 'Shrimp Scampi', 'calories': 650},
            {'food': 'Veggie Lasagna', 'calories': 550},
            {'food': 'BBQ Ribs', 'calories': 800},
            {'food': 'Pizza', 'calories': 900},
            {'food': 'Shrimp Fried Rice', 'calories': 600}
        ]

        #Generate data for the last 90 days
        start_date = datetime.utcnow().date() - timedelta(days=90)

        for i in range(90):
            current_date = start_date + timedelta(days=i)

            # Add random meals for variety
            breakfast = Meal(date=current_date, **random.choice(breakfast_options))
            lunch = Meal(date=current_date, **random.choice(lunch_options))
            dinner = Meal(date=current_date, **random.choice(dinner_options))
            db.session.add_all([breakfast, lunch, dinner])

            # Add sleep (6-9 hours with variation)
            sleep_hours = round(random.uniform(6, 9), 1)  # Random sleep between 6 to 9 hours
            sleep = Sleep(date=current_date, hours=sleep_hours)
            db.session.add(sleep)

            # Add steps 1000-12000 steps with variation
            step_count = random.randint(1000, 12000)  # Random steps between 1,000 to 12,000
            steps = Steps(date=current_date, count=step_count)
            db.session.add(steps)

            # Weight
            weight_value = round(random.uniform(150, 170), 1)  # Random weight between 150 to 170 lbs
            weight = Weight(date=current_date, value=weight_value)
            db.session.add(weight)

        db.session.commit() # Commit the changes
        print("Sample data added!")