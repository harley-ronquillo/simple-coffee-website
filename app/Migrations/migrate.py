from app.Migrations.CategoryMigration import categories
from app.Migrations.ProductMigration import products
from app.Migrations.UserMigration import users
from app.Config import engine, meta

def migrate():
    meta.drop_all(engine)
    meta.create_all(engine)
    print("Migration completed successfully.")

if __name__ == "__main__":
    migrate()