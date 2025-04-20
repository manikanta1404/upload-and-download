// This function fetches the list of files from the server
function fetchFiles() {
    fetch('/get_files')  // Assuming this endpoint returns a list of files in JSON format
        .then(response => response.json())
        .then(files => {
            const fileList = document.getElementById('file-list');
            fileList.innerHTML = '';  // Clear the previous list

            files.forEach(file => {
                const li = document.createElement('li');
                li.textContent = file;

                // Create Download button
                const downloadBtn = document.createElement('button');
                downloadBtn.textContent = 'Download';
                downloadBtn.onclick = function() {
                    window.location.href = `/download/${file}`;
                };

                // Create Delete button
                const deleteBtn = document.createElement('button');
                deleteBtn.textContent = 'Delete';
                deleteBtn.onclick = function() {
                    fetch(`/delete/${file}`, { method: 'DELETE' })
                        .then(response => response.json())
                        .then(result => {
                            if (result.success) {
                                alert(`${file} deleted`);
                                fetchFiles();  // Refresh the list after deletion
                            }
                        });
                };

                // Create View button
                const viewBtn = document.createElement('button');
                viewBtn.textContent = 'View';
                viewBtn.onclick = function() {
                    window.location.href = `/view/${file}`;
                };

                // Append buttons to the list item
                li.appendChild(downloadBtn);
                li.appendChild(deleteBtn);
                li.appendChild(viewBtn);

                // Append list item to the file list
                fileList.appendChild(li);
            });
        });
}

// Fetch the files when the page loads
window.onload = fetchFiles;
