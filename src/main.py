from flask import Flask

app = Flask("app_name")

@app.route("/")
def index():
  return "<h1>Hello</h1>"

def main():
  app.run()


if __name__ == "__main__":
  main()
