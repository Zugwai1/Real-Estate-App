document.addEventListener("DOMContentLoaded", async () => {
    let id = JSON.parse(localStorage.getItem('user')).id
    console.log(id);
    let user = await fetch(`${baseUrl}api/v1/users/${id}`, {
         headers: {
            'Authorization': localStorage.getItem('token'),
        }
    }).then(response => {
        return response.json()
    }).then(data => {
        return data.user
    })

    document.getElementById("first_name").value = user.first_name;
    document.getElementById("last_name").value = user.last_name;
    document.getElementById("middle_name").value = user.middle_name;
    document.getElementById("email").value = user.email;
    document.getElementById("nationality").value = user.nationality;
    document.getElementById("dob").value = user.DOB;
    document.getElementById("country").value = user.address.country;
    document.getElementById("state").value = user.address.state;
    document.getElementById("street").value = user.address.street;
    document.getElementById("city").value = user.address.city;
    document.getElementById("postal_code").value = user.address.postal_code;
    document.getElementById("number_line").value = user.address.number_line;
    document.getElementById("phone_number").value = user.phone_number;
})