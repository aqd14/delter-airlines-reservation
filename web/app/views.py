from flask_restful import Resource

class Home(Resource):
    def get(self):
        return render_template('/templates/signup.html')