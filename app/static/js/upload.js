    const fileInput = document.getElementById('photo-input');
    const clearBtn = document.getElementById('clear-file-btn');

    // Kada korisnik izabere fajl
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            clearBtn.style.display = 'inline-block'; // Prikaži X
        } else {
            clearBtn.style.display = 'none'; // Sakrij ako je prazno
        }
    });

    // Kada korisnik klikne na X da poništi izbor
    clearBtn.addEventListener('click', function() {
        fileInput.value = ''; // Poništava vrednost inputa (skida fajl)
        clearBtn.style.display = 'none'; // Sakriva X dugme ponovo
    });