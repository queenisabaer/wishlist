//jshint esversion:8

document.addEventListener("DOMContentLoaded", function() {
    const messages = document.getElementById('msg');
    setTimeout(function(){
        let alert = new bootstrap.Alert(messages);
        // closes the alert for the django messages after 3 seconds
        alert.close();
    }, 3000); // 3000 milliseconds = 3 seconds
});


document.addEventListener('DOMContentLoaded', (event) => {
    const shareButton = document.getElementById('shareButton');
    const shareLink = document.getElementById('shareLink');
    const message = document.getElementById('share-message');

    shareButton.addEventListener('click', async () => {
        try {
            await navigator.clipboard.writeText(shareLink.value);
            message.innerHTML = 'Copied <i class="fa-solid fa-check"></i>';
            // shows the message only for 2 seconds then switch back to empy p
            setTimeout(() => {
                message.innerHTML = '';
            }, 2000); // 2000 milliseconds = 2 seconds
        } catch (error) {
            console.error('Error sharing the link because: ', error);
            message.innerHTML = 'Failed to copy. Please try again.';
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const firstNameElement = document.getElementById('f_name');
    const lastNameElement = document.getElementById('l_name');
    if (firstNameElement.innerText == 'None'){
        firstNameElement.innerText = "Not yet provided";
    }
    if (lastNameElement.innerText == 'None'){
        lastNameElement.innerText = "Not yet provided";
    }
});
