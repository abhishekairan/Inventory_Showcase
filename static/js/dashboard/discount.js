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
    var discounts = Array.isArray(response) ? response : [response]
    console.log(discounts)
    var productListElement = $('#product-list');
    productListElement.empty();
    if(JSON.parse(discounts[0].input_value).length > 0){
        JSON.parse(discounts[0].input_value).forEach(function(discount){
            // console.log(product)
            var product_row = `
                <tr data-url="/dashboard/discount/${discount.pk}">
                    <td>${discount.pk}</td>
                    <td>${discount.fields.value}${discount.fields.discountType}</td>
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
    // console.log(featured_value)
    $.ajax({
        url: '/search/discounts/',
        method: 'POST',
        data: {
            'inputval': inputVal,
            'featuredval': featured_value,
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