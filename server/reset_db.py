#!/usr/bin/env python3

from app import app
from models import db

with app.app_context():
    # Drop all tables to remove old schema
    db.drop_all()
    # Create new tables with current schema
    db.create_all()
    print("✅ Database reset complete! New schema created.")
