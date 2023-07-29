from flask import Flask
     
app = Flask(__name__)
     
@app.route("/",methods=["GET"])
def root():
   return "<h1>Welcome to ITIL exam</h1>"
         
@app.route("/modules",methods=["GET"])
def modules():
  return "<h1>FCN,COSA,SC,CA,NDC,CF,PKI,ITIM & DevOps</h1>"
    
@app.route("/me",methods=["GET"])
def me():
  return "<h1>PRN:230344223001, Name-Ajay Prakash,Phone.no-8795058705</h1>"

app.run(host="0.0.0.0",port=4000, debug=True)
