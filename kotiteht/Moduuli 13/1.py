from flask import Flask

app = Flask(__name__)

def on_alkuluku(luku):
    if luku < 2:
        return False

    for i in range(2, luku):
        if luku % i == 0:
            return False

    return True

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    tulos = on_alkuluku(luku)

    return {
        "Number": luku,
        "isPrime": tulos
    }

if __name__ == '__main__':
    app.run(port=3000)