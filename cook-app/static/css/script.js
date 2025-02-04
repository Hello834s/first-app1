document.addEventListener('DOMContentLoaded', function() {
    
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault(); 
        let ingredients = document.querySelector('input[name="ingredients"]').value;

        
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `ingredients=${encodeURIComponent(ingredients)}`
        })
        .then(response => response.text())
        .then(data => {
           
            console.log(data);
        });
    });
});
