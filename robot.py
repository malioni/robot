from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def root():
    return """                                                                                       
    <html>                                                                                           
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>         
    <script>                                                                                         
      function forward() { $.ajax({url: "/forward"}) }                                               
    </script>                                                                                        
    <button onclick="forward()">Forward</button>                                                     
    </html>                                                                                          
    """

@app.route("/forward")
def forward():
    print("Robo go forward!")
    return jsonify({
        "message": "Robot just went forward"
    })

app.run(host="0.0.0.0")
