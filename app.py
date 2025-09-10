from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        total_bill = float(request.form["total_bill"])
        roommates = request.form.getlist("name")
        days = request.form.getlist("days")

        # Convert days to int
        days = [int(d) for d in days]
        total_days = sum(days)

        shares = []
        for i in range(len(roommates)):
            share = round((days[i] / total_days) * total_bill, 2)
            shares.append((roommates[i], days[i], share))

        return render_template("result.html", total_bill=total_bill, shares=shares)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    #http://127.0.0.1:5000/    paste it in in your browser 
    #run app .py
    
