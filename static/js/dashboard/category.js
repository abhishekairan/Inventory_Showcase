
document.addEventListener("DOMContentLoaded", addRedirect());


function addRedirect() {
    const rows = document.querySelectorAll(".project-table tbody tr");
    // console.log(rows)
    rows.forEach(row => {
        row.addEventListener("click", function() {
            // console.log("Clicked")
            const url = row.getAttribute("data-url");
            // console.log(url)
            if (url) {
                window.location.href = url;
            }
        });
    });
}



// function to render products

function renderpoducts(response){
    var product = Array.isArray(response) ? response : [response]
    // console.log(product)
    var productListElement = $('#product-list');
    productListElement.empty();
    if(JSON.parse(product[0].input_value).length > 0){
        JSON.parse(product[0].input_value).forEach(function(category){
            console.log(category)
            const featured_icon = category.fields.display ? '<img width="24" height="24" src="https://img.icons8.com/color/48/checked--v1.png" alt="checked--v1"/>' : '<img width="24" height="24" src="https://img.icons8.com/color/48/cancel--v1.png" alt="cancel--v1"/>';
            var product_row = `
                <tr data-url="/dashboard/category/${category.pk}">
                    <td>${category.pk}</td>
                    <td>${category.fields.name}</td>
                    <td>${category.fields.display_name}</td>
                    <td>${category.fields.description}</td>
                    <td>${featured_icon}</td>
                </tr>
            `;
            productListElement.append(product_row)
        })
    }
    addRedirect()
}

function ajaxCall(){
    var inputVal = $('#search_field').val()
    var featured_value = $('#featured').val();
    // console.log(inputVal)
    $.ajax({
        url: '/search/category/',
        method: 'POST',
        data: {
            'inputval': inputVal,
            'displayval': featured_value,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            renderpoducts(response)
        }
    })
}
    
$(document).ready(function(){

    
    // featured Options
    $('#featured').change(ajaxCall)


    // Search field 
    $('#search_field').on('input',ajaxCall)
})