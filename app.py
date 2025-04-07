from flask import Flask
#from productivity import calc_productivity, work_input_saving, best_productivity

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Productivity App!"

if __name__ == "__main__":
    app.run(debug=True)

