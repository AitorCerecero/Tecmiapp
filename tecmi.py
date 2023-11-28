from flask import Flask, render_template, request

app = Flask(__name__)

def acccheck(Mat):
    logo_url = "https://blog.tecmilenio.mx/hubfs/Nuevos%20logos%20OCT%202022/Tecmilenio_Horizontal_Color-op.svg"
    if 'AL' in Mat:
        P1 = "IaC y Seguridad con Kevin Mitnick"
        H1 = "2:00 pm a 4:00 pm"
        P2 = "Modelacion de Apps Con Jose Manuel Bulos"
        H2 = "4:00 pm a 5:00 pm"
        P3 = "Bases de Datos con Paco Rubio"
        H3 = "5:00 pm a 6:30 pm"
        P4 = "Ingenieria de Datos Masivos Con Jesus Hiram"
        H4 = "6:30 pm a 8:00 pm"
    else:
        P1 = None
        H1 = None
        P2 = None
        H2 = None
        P3 = None
        H3 = None
        P4 = None
        H4 = None

    return P1, H1, P2, H2, P3, H3, P4, H4, logo_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Mat = request.form['Matricula']
        P1, H1, P2, H2, P3, H3, P4, H4, logo_url = acccheck(Mat)
        return render_template('result.html', P1=P1, H1=H1, P2=P2, H2=H2, P3=P3, H3=H3, P4=P4, H4=H4, logo_url=logo_url)

    # Return both the logo and the index template on GET requests
    logo_url = "https://blog.tecmilenio.mx/hubfs/Nuevos%20logos%20OCT%202022/Tecmilenio_Horizontal_Color-op.svg"
    return render_template('index.html', logo_url=logo_url)

if __name__ == '__main__':
    app.run(debug=True)
