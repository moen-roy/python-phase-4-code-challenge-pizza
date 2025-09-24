#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    print("Adding sample data...")
    
    # Create restaurants
    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Mario's Pizzeria", address="456 Oak Ave")
    db.session.add_all([r1, r2])
    db.session.commit()
    
    # Create pizzas
    p1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])
    db.session.commit()
    
    # Create restaurant_pizzas
    rp1 = RestaurantPizza(restaurant_id=r1.id, pizza_id=p1.id, price=15)
    rp2 = RestaurantPizza(restaurant_id=r1.id, pizza_id=p2.id, price=18)
    rp3 = RestaurantPizza(restaurant_id=r2.id, pizza_id=p1.id, price=16)
    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
    
    print("Sample data added successfully!")