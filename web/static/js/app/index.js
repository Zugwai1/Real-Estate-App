document.addEventListener("DOMContentLoaded", async function () {
    checkRole();
    let properties = await fetch('http://127.0.0.1:8000/api/v1/properties/')
        .then(response => response.json())
        .then(data => {
            return data.properties
        })
    let innerHtml = ``
    properties.forEach(property => {
        innerHtml += `
         <div class="slider-item" style="background-image:url(web/static/images/properties-1.jpg);">
            <div class="overlay"></div>
            <div class="container">
                <div class="row no-gutters slider-text align-items-md-end align-items-center justify-content-end">
                    <div class="col-md-6 text p-4">
                        <h1 class="mb-3">${property.name}</h1>
                        <span class="location d-block mb-3"><i class="icon-my_location"></i>${property.address.number_line}, ${property.address.street},
                            ${property.address.city}, ${property.address.state}, ${property.address.country}</span>
                        <p>${property.description}</p>
                        <span class="price">${property.price}</span>
                        <a href="#" class="btn-custom p-3 px-4 bg-primary">View Details <span
                                class="icon-plus ml-1"></span></a>
                    </div>
                </div>
            </div>
        </div>
    `
    })
    document.getElementById("propSection").innerHTML = innerHtml;
    let innerListHtml = ``;
    properties.forEach(property => {
        innerListHtml += `<div class="item">
                            <div class="properties">
                                <a href="#" class="img d-flex justify-content-center align-items-center"
                                   style="background-image: url(web/static/images/properties-1.jpg);">
                                    <div class="icon d-flex justify-content-center align-items-center">
                                        <span class="icon-search2"></span>
                                    </div>
                                </a>
                                <div class="text p-3">
                                    <span class="status sale">${property.type}</span>
                                    <div class="d-flex">
                                        <div class="one">
                                            <h3><a href="#">${property.name}</a></h3>
                                            <p>${property.type}</p>
                                        </div>
                                        <div class="two">
                                            <span class="price">${property.price}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>`
    });
    document.getElementById("property-list").innerHTML = innerListHtml;

    let innerRecomListHtml = ``;
    properties.forEach(pro => {
        innerRecomListHtml += `
            <div class="col-sm col-md-6 col-lg">
                    <div class="properties">
                        <a href="#" class="img img-2 d-flex justify-content-center align-items-center"
                           style="background-image: url(web/static/images/properties-1.jpg);">
                            <div class="icon d-flex justify-content-center align-items-center">
                                <span class="icon-search2"></span>
                            </div>
                        </a>
                        <div class="text p-3">
                            <span class="status sale">${pro.type}</span>
                            <div class="d-flex">
                                <div class="one">
                                    <h3><a href="#">${pro.name}</a></h3>
                                    <p>Apartment</p>
                                </div>
                                <div class="two">
                                    <span class="price">${pro.price}</span>
                                </div>
                            </div>
                            <p>Far far away, behind the word mountains, far from the countries</p>
                            <hr>
                            <p class="bottom-area d-flex">
                                <span><i class="flaticon-selection"></i> 250sqft</span>
                                <span class="ml-auto"><i class="flaticon-bathtub"></i>${pro.number_of_bathrooms}</span>
                                <span><i class="flaticon-bed"></i>${pro.number_of_bedrooms}</span>
                            </p>
                        </div>
                    </div>
                </div>
        `
    })
    document.getElementById("property-recom-list").innerHTML = innerRecomListHtml;
})