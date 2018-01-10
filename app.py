import ....make_response

app=Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
  req=request.get_json(silent=True, force=True)
  print("Request:")
  print(json.dumps(req, indent=4))
  res=makeWebhookResult(req)
  res=json.dumps(res,indent=4)
  print(res)
  r=make_response(res)
  r.headers['Conten-Type']='application/json'
  return r

def makeWebhookResult(req):
  if req.get("result").get("action")!="interest":
    return{}
  result=req.get("result")
  parameters=result.get("parameters")
  speech="Voilà les paramètre récupérés :"+parameters
  print("Response:")
  print(speech)
  return {
    "speech": speech,
    "displayText": speech,
    "source": "FormBot"
  }
if __name__=='__main__'
  port=int(os.getenv('PORT',80))
  print("Starting app on port %d" %(port))
  app.run(debug=True, port=port, host='0.0.0.0')
gtfchfgth