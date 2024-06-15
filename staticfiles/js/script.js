document.addEventListener("DOMContentLoaded", function() {
    const messages = document.getElementById('msg');
    setTimeout(function(){
        let alert = new bootstrap.Alert(messages);
        // closes the alert for the django messages after 3 seconds
        alert.close();
    }, 3000); // 3000 milliseconds = 3 seconds
});
  