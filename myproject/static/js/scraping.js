console.log("javascript available")

document.addEventListener('DOMContentLoaded', () => {
    const tickerInput = document.getElementById('text');
    const uploadButton = document.getElementById('uploadButton')

    tickerInput.addEventListener('change', (e) =>{
        ticker = tickerInput.value;


    });

   uploadButton.addEventListener('click', () => {
        let passedData = new FormData();
        passedData.append('text', ticker);
        passedData.append('text2', 'abrakadabra')
        uploadFiles(passedData);
    });

    function uploadFiles(content) {
        fetch('/scrapping/', {  //  Django view URL pattern reference
            method: 'POST',
            body: content,
            headers: {
                'X-CSRFToken': getCSRFToken() // Include CSRF token for security
            }
        })
       .then(response => response.json())};

    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
})
