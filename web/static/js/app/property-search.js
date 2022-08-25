let searchProperty = async (e) => {
    checkRole();
    e.preventDefault();
    let info = JSON.stringify({
        'price': document.getElementById("price").value,
        'location': document.getElementById("location").value,
        'keyword': document.getElementById("keyword").value,
        'number_of_bedrooms': document.getElementById("number_of_bedrooms").value,
        'number_of_bathrooms': document.getElementById("number_of_bathrooms").value,
        'type': document.getElementById("type").value,
        'status': document.getElementById("status").value
    })
    let properties = await fetch(`${baseUrl}api/v1/properties/search`, {
        method: 'POST',
        body: info,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem('token')
        }
    }).then(response => {
        return response.json()
    }).then(data => {
        return data.properties
    })
    let innerHtml = ``
    properties.forEach(prop => {
        let url = `${baseUrl}property/single/${prop.id}`
        console.log(url);
        innerHtml += `
        <div class="col-md-4">
            <div class="properties">
                <a class="img img-2 d-flex justify-content-center align-items-center" href="${url}"
                   style="background-image: url(${prop.images[0]});">
                    <div class="icon d-flex justify-content-center align-items-center">
                        <span class="icon-search2"></span>
                    </div>
                </a>
                    <div class="text p-3">
                        <span class="status sale">${prop.type}</span>
                        <div class="d-flex">
                            <div class="one">
                                <h3><a href="${url}">${prop.name}</a></h3>
                                <p>Apartment</p>
                            </div>
                            <div class="two">
                                <span class="price">€${Number(prop.price).toFixed(2)}</span>
                            </div>
                        </div>
                        <p>Far far away, behind the word mountains, far from the countries</p>
                        <hr>
                        <p class="bottom-area d-flex">
                            <span><i class="flaticon-selection"></i> 250sqft</span>
                            <span class="ml-auto"><i class="flaticon-bathtub"></i>${prop.number_of_bathrooms}</span>
                            <span><i class="flaticon-bed"></i>${prop.number_of_bedrooms}</span>
                        </p>
                    </div>
            </div>
        </div>`
    })
    document.getElementById("property-list").innerHTML = innerHtml;
}