<?php
// Подключение к базе данных
$db = new SQLite3('recipe_app.db');

// Получаем данные из формы
if (isset($_POST['ingredients'])) {
    $ingredients = $_POST['ingredients'];

    // Преобразуем строку в массив
    $ingredientsArray = explode(',', $ingredients);
    
    // Обрабатываем запрос для поиска рецептов
    $query = "SELECT * FROM recipes WHERE ingredients LIKE '%" . implode("%' OR ingredients LIKE '%", $ingredientsArray) . "%'";
    $result = $db->query($query);
    
    echo "<h1>Возможные рецепты:</h1>";
    while ($row = $result->fetchArray()) {
        echo "<h2>" . $row['name'] . "</h2>";
        echo "<p>" . $row['description'] . "</p>";
    }
}
?>