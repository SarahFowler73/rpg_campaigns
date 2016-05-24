from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test_view(name="Sarah"):
    return render_template(
        'test_view.html',
        message="Hello {}!".format(name)
    )


app.run(debug=True, port=8888, host='localhost')
