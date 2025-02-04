from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
        # Подключаемся к базе данных
        conn = sqlite3.connect('recipe_app.db')
        cursor = conn.cursor()
        query = "SELECT * FROM recipes WHERE"
        conditions = []
        params = []
        for ingredient in ingredients_list:
            conditions.append(" ingredients LIKE ? ")
            params.append(f"%{ingredient}%")
        query += " OR ".join(conditions)
        cursor.execute(query, params)
        recipes = cursor.fetchall()
        conn.close()

        return render_template('results.html', recipes=recipes)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
