from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Check if admin user already exists
    existing_admin = User.query.filter_by(username='admin').first()
    
    if not existing_admin:
        # Generate secure password hash
        hashed_password = generate_password_hash('admin123', method='scrypt')
        
        # Create new admin user instance
        admin = User(
            username='admin',
            email='admin@moonlens.com',
            password_hash=hashed_password
        )
        
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists in the database.")