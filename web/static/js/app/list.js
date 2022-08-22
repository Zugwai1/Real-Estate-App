document.addEventListener("DOMContentLoaded", async () => {
    checkRole();
    let properties = await fetch('http://127.0.0.1:8000/api/v1/properties/')
        .then(response => response.json())
        .then(data => {
            return data.properties
        })
    let innerHtml = ``
    properties.forEach(prop => {
        let url = `http://127.0.0.1:8000/property/single/${prop.id}`
        console.log(url);
        innerHtml += `
        <div class="col-md-4">
            <div class="properties">
                <a class="img img-2 d-flex justify-content-center align-items-center" href="${url}"
                   style="background-image: url(images/properties-1.jpg);">
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
                                <span class="price">${prop.price}</span>
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
})