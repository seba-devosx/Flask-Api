from app import db,create_app

app=create_app()

## crea todas las tablas que se hayan definido en el modelo
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)