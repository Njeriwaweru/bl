from app import app, db, Category

def populate_db():
     with app.app_context():
        with db.session.begin():
            print("Clearing existing data...")
            db.session.query(Category).delete()

        with db.session.begin():
            print("Populating the database...")
            categories = [
                Category(name='Plumbing', icon='https://cdn-icons-png.flaticon.com/512/4310/4310770.png'),
                Category(name='Electrical', icon='https://cdn-icons-png.flaticon.com/512/8734/8734819.png'),
                Category(name='Cleaning', icon='https://cdn-icons-png.freepik.com/256/994/994928.png?semt=ais_hybrid'),
                Category(name='Carpentry', icon='https://cdn-icons-png.freepik.com/512/3531/3531568.png'),
                Category(name='Repair', icon='https://cdn-icons-png.flaticon.com/512/9759/9759793.png')
            ]

            db.session.bulk_save_objects(categories)
            print("Database populated successfully!")

if __name__ == '__main__':
    populate_db()
