document.getElementById("property-form").addEventListener("submit", (e) => {
    e.preventDefault();
    let data = new FormData(e.target);
    let input = document.querySelector('input[type="file"]')
    data.append("input1", input.files[0])
    data.append("inout2", input.files[1])
    data.append("inout3", input.files[1])
    fetch(`${baseUrl}api/v1/properties/`, {
        method: 'POST',
        body: data,
        headers: {
            'Authorization': localStorage.getItem('token'),
        }
    }).then(response => {
        if (response.status === 401) {
            window.location.replace("/signin");
        }
        return response.json()
    }).then(data => {
        if (data.status === true) {
            Swal.fire({
                icon: 'success',
                title: data.message,
                confirmButtonText: 'Ok',
                showConfirmButton: true,
                timer: 50000,
            })
        } else {
            Swal.fire({
                icon: 'error',
                title: data.message,
                confirmButtonText: 'Ok',
                showConfirmButton: true,
                timer: 50000,
            })
        }
    })
        .catch(error => {
            console.log("Error");
        })
})