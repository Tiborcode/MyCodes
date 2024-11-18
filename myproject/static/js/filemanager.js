document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');
    const uploadBtn = document.getElementById('uploadBtn');
    const uploadButton = document.getElementById('uploadButton');

    let selectedFiles = [];

    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('dragover');
    });

    dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('dragover');
    });

    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('dragover');
        selectedFiles = Array.from(e.dataTransfer.files);
        displayFiles(selectedFiles);
//        const files = e.dataTransfer.files;
//        handleFiles(files);
    });

    dropzone.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {

        selectedFiles = Array.from(e.target.files);
        displayFiles(selectedFiles);
//        handleFiles(e.target.files);
    });

    uploadButton.addEventListener('click', () => {
            if (selectedFiles.length > 0) {
                const formData = new FormData();
                selectedFiles.forEach(file => {
                    formData.append('files', file);
                });

                uploadFiles(formData);
            } else {
                alert('Please select a file first!');
            }
        });

    function displayFiles(files) {
        fileList.innerHTML = ''; // Clear previous file list
        files.forEach(file => {
            const listItem = document.createElement('div');
            listItem.textContent = file.name;
            fileList.appendChild(listItem);
        });
    }

//    function handleFiles(files) {
//        const formData = new FormData();
//        for (let i = 0; i < files.length; i++) {
//            formData.append('files', files[i]);
//        }
//
//        // Send the AJAX request
//        uploadFiles(formData);
//    }

    function uploadFiles(formData) {
        fetch('/myfolders/', {  // Ensure '/upload/' matches your Django view URL pattern
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCSRFToken() // Include CSRF token for security
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Files uploaded successfully!');
                // Optionally update UI with new files
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred during file upload.');
        });
    }

    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

//    uploadBtn.addEventListener('click', () => {
//        fileInput.click();
//    });
});