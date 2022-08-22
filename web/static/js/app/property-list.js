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
                                <a class="btn btn-success" href="${baseUrl}property/single/${property.id}">View</a>
                                <a class="btn btn-warning" href="${baseUrl}property/edit/${property.id}">Edit</a>
</div></td>
                            </tr>`
        count++;
    })
    document.getElementById("table-body").innerHTML = innerHtml;
})