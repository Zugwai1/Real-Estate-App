document.addEventListener("DOMContentLoaded", async () => {
    checkRole();
    let id = document.getElementById("keep").innerText
    let property = await fetch(`${baseUrl}api/v1/properties/${id}`, {
        headers: {
            'Authorization': localStorage.getItem('token'),
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Oops',
                text: response.message,
                confirmButtonText: 'Login',
                showConfirmButton: true,
                timer: 50000,
            })
            window.location.replace("/signin");
        }
    }).then(data => {
        return data.property;
    })
    document.getElementById("name").value = property.name;
    document.getElementById("type").value = property.type;
    document.getElementById("price").value = Number(property.price).toFixed(2);
    document.getElementById("country").value = property.address.country;
    document.getElementById("number_of_bedrooms").value = property.number_of_bedrooms;
    document.getElementById("number_of_bathrooms").value = property.number_of_bathrooms;
    document.getElementById("status").value = property.status;
    document.getElementById("number_line").value = property.address.number_line;
    document.getElementById("street").value = property.address.street;
    document.getElementById("postal_code").value = property.address.postal_code;
    document.getElementById("city").value = property.address.city;
    document.getElementById("description").value = property.description;
    document.getElementById("state").value = property.address.state;
    document.getElementById("video_link").value = property.property_video_url;
})

document.getElementById("property-form").addEventListener("submit", (e) => {
    e.preventDefault();
    let data = new FormData(e.target);
    let id = document.getElementById("keep").innerText
    fetch(`${baseUrl}api/v1/properties/${id}`, {
        method: 'PUT',
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
            window.location.replace("/workspace")
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