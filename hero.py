from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def formulari():
    if request.method == 'POST':
        tipus = request.form['tipus']
        nom = request.form['nom']
        atac = request.form['atac']
        defensa = request.form['defensa']
        moviment = request.form['moviment']
        cos = request.form['cos']
        ment = request.form['ment']
        habilitats = request.form['habilitats']
        return f"""
            <style>
                body {{
                    font-family: 'Georgia', 'Times New Roman', serif;
                    background-color: #f5f5dc;
                    padding: 20px;
                    text-align: center;
                }}
                .paper {{
                    background: #fdf6e3;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
                    max-width: 500px;
                    margin: auto;
                    border: 2px solid #8B4513;
                }}
                h1 {{
                    color: #5B3A29;
                }}
                p {{
                    font-size: 18px;
                }}
                a {{
                    display: inline-block;
                    margin-top: 15px;
                    padding: 10px;
                    background: #8B4513;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                }}
                a:hover {{
                    background: #5B3A29;
                }}
                .btn {{
                display: inline-block;
                margin-top: 15px;
                padding: 10px;
                background: #8B4513;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                font-size: 16px;
                cursor: pointer;
                }}
                .btn:hover {{
                background: #5B3A29
                }}
                .container-yelmo {{
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                }}
                .yelmo-img {{
                width: 60px;
                }}
                .yelmo2-img {{
                width: 60px;
                }}
            </style>     
        <html>
        <body>
            <div class="paper">
                <div class="container-yelmo">
                    <img src="static/yelmo.png" alt="Imagen Yelmo Derecha class="yelmo-img" style="width: 60px; height: auto;">
                    <h1>Fitxa de Monstre</h1>
                    <img src="static/yelmo2.png" alt="Imagen Yelmo Izquierda class="yelmo2-img style="width: 60px; height: auto;">
                </div>
                <p><strong>Tipus:</strong> {tipus}</p>
                <p><strong>Nom:</strong> {nom}</p>
                <p><strong>Atac:</strong> {atac}</p>
                <p><strong>Defensa:</strong> {defensa}</p>
                <p><strong>Moviment:</strong> {moviment}</p>
                <p><strong>Cos:</strong> {cos}</p>
                <p><strong>Ment:</strong> {ment}</p>
                <p><strong>Habilitats Especials:</strong> {habilitats}</p>
                <a class:"btn" href="/form">Tornar</a>
            </div>
        </body>
        </html>
        </html>
        """
    return '''
        <style>
            body {
                font-family: 'Georgia' 'Times New Roman', serif;
                background-color: #f5f5dc;
                padding: 20px;
            }
            .paper {
                background: #fdf6e3;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
                max-width: 500px;
                margin: auto;
                border: 2px solid #8B4513;
            }
            .paper h1 {
                text-align: center;
                margin: 0;
                color: 5B3A29;
            }
            .section {
                border: 1px solid black;
                padding: 10px;
                margin: 10px;
                background-color: #fffaea;
            }
            .flex-container {
                display: flex;
                justify-content: space-between;
                margin: 10px 0;
            }
            .flex-item {
                flex: 1;
                margin: 10px;
            }
            .container-yelmo {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
            }
            .yelmo-img {
                width: 60px;
            }
            .yelmo2-img {
                width: 60px;
            }
            .btn {
                font-family: 'Georgia', 'Times New Roman', serif;
                display: inline-block;
                margin-top: 15px;
                padding: 10px;
                background: #8B4513;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                font-size: 16px;
                cursor: pointer;
                }
                .btn:hover {
                background: #5B3A29
                }
        </style>
        <div class="paper">
            <form method="POST">
                <div class="container-yelmo">
                    <img src="static/yelmo.png" alt="Imagen Yelmo Derecha class="yelmo-img" style="width: 60px; height: auto;">
                    <h1>HeroQuest</h1>
                    <img src="static/yelmo2.png" alt="Imagen Yelmo Izquierda class="yelmo2-img style="width: 60px; height: auto;">
                </div>
                <div class="section">
                    Tipo de Monstruo o PNJ: <input type="text" name="tipus" required><br>
                    Nombre: <input type="text" name="nom" required><br>
                </div>
                <div class="flex-container">
                    <div class="flex-item section">
                        <label for="atac">Ataque</label><br>
                        <select name="atac" required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                        </select><br>
                    </div>
                    <div class="flex-item section">
<label for="defensa">Defensa</label><br>
                        <select name="defensa" required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select><br>
                    </div>
                    <div class="flex-item section">
                        <label for="moviment">Movimiento</label><br>
                        <select name="moviment" required>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                            <option value="9">9</option>
                            <option value="10">10</option>
                        </select><br>
                    </div>
                </div>
                <div class="flex-container">
                    <div class="flex-item section">
                        <label for="cos">Cuerpo</label><br>
                        <select name="cos" required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                            <option value="9">9</option>
                            <option value="10">10</option>
                        </select><br>
                    </div>
                    <div class="flex-item section">
                        <label for="ment">Mente</label><br>
                        <select name="ment" required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select><br>
                    </div>
                </div>
                <div class="section">
                    <label for="habilitats">Habilidades especiales</label><br>
                    <textarea name="habilitats"></textarea><br><br>
                </div>
                <div style="text-align: center;">
                    <input type="submit" value="Envia" class="btn">
                </div>
            </form>
        </div>
    '''
#<a href="/form">Volver</a>
if __name__ == '__main__':
    app.run(debug=True)
