from flask import Flask, render_template, request, url_for

def create_app():
    app = Flask(__name__)

    from application.routes import index
    from application.routes import about
    from application.routes import courses
    from application.routes import appointment
    
    app.register_blueprint(index.bp)
    app.register_blueprint(about.bp)
    app.register_blueprint(courses.bp)
    app.register_blueprint(appointment.bp)

    return app

if __name__ ==  '__main__':
    app = create_app()
    app.run(debug=True)