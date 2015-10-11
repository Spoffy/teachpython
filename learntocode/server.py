from bottle import post, run, request

@post("/analytics")
def print_analytics():
    print("Hello!")
    print(request.json)

run(host="0.0.0.0", port=8080)
