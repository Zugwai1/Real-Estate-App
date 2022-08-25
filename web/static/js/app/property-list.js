document.addEventListener("DOMContentLoaded", async () => {
    checkRole();
    let properties = await fetch(`${baseUrl}api/v1/properties/user`, {
        headers: {
            'Authorization': localStorage.getItem('token'),
        }
    })
        .then(response => response.json())
        .then(data => {
            return data.properties
        })
    let innerHtml = ``
    let count = 1;
    properties.forEach(property => {

        innerHtml += `<tr>
                                <th scope="row">${count}</th>
                                <td>${property.name}</td>
                                <td>${property.address.number_line}, ${property.address.street},
                            ${property.address.city}, ${property.address.state}, ${property.address.country}</td>
                                <td>${property.type}</td>
                                <td>${property.status}</td>
                                <td><div class="btn-group">
                                <p hidden id="property-id">${property.id}</p>
                                <a class="btn btn-success" href="${baseUrl}property/single/${property.id}">View</a>
                                <a class="btn btn-warning" href="${baseUrl}property/edit/${property.id}">Edit</a>
                                <button class="btn btn-danger" id="delete-btn" onclick="delete_record()">Delete</button>
</div></td>
                            </tr>`
        count++;
    })
    document.getElementById("table-body").innerHTML = innerHtml;
})

let delete_record = async () => {
    let property_id = document.getElementById("property-id").innerText;
    await fetch(`${baseUrl}api/v1/properties/${property_id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': localStorage.getItem('token'),
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === true) {
                Swal.fire({
                    icon: 'success',
                    title: data.message,
                    confirmButtonText: 'Ok',
                    showConfirmButton: true,
                    timer: 50000,
                })
                window.location.reload();
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
}