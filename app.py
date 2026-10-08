from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("myForm.html")
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    gender = request.form.get("gender")
    course = request.form.get("course")
    return render_template(
        "greeting.html",
        name=name,
        email=email,
        phone=phone,
        gender=gender,
        course=course
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)