
document.addEventListener("DOMContentLoaded", function() {
    const rows = document.querySelectorAll(".project-table tbody tr");
    // console.log(rows)
    rows.forEach(row => {
        row.addEventListener("click", function() {
            // console.log("Clicked")
            const url = row.getAttribute("data-url");
            console.log(url)
            if (url) {
                window.location.href = url;
            }
        });
    });
});



// function to render products

function renderpoducts(response){
    var product = Array.isArray(response) ? response : [response]
    // console.log(product)
    var productListElement = $('#product-list');
    productListElement.empty();
    if(JSON.parse(product[0].input_value).length > 0){
        JSON.parse(product[0].input_value).forEach(function(product){
            console.log(product)
            const featured_icon = product.fields.featured ? '<img width="24" height="24" src="https://img.icons8.com/color/48/checked--v1.png" alt="checked--v1"/>' : '<img width="24" height="24" src="https://img.icons8.com/color/48/cancel--v1.png" alt="cancel--v1"/>';
            var product_row = `
                <tr data-url="{% url "dashboard" %}">
                    <td>${product.pk}</td>
                    <td>${product.fields.name}</td>
                    <td>${product.fields.description}</td>
                    <td>${product.fields.cost}</td>
                    <td>${product.fields.discount}</td>
                    <td>${featured_icon}</td>
                    <td>${product.fields.updated_at}</td>
                </tr>
            `;
            productListElement.append(product_row)
        })
    }
}


// function to render products

function renderpoducts(response){
    var product = Array.isArray(response) ? response : [response]
    // console.log(product)
    var productListElement = $('#product-list');
    productListElement.empty();
    if(JSON.parse(product[0].input_value).length > 0){
        JSON.parse(product[0].input_value).forEach(function(product){
            console.log(product)
            const featured_icon = product.fields.featured ? '<img width="24" height="24" src="https://img.icons8.com/color/48/checked--v1.png" alt="checked--v1"/>' : '<img width="24" height="24" src="https://img.icons8.com/color/48/cancel--v1.png" alt="cancel--v1"/>';
            var product_row = `
                <tr data-url="{% url "dashboard" %}">
                    <td>${product.pk}</td>
                    <td>${product.fields.name}</td>
                    <td>${product.fields.description}</td>
                    <td>${product.fields.cost}</td>
                    <td>${product.fields.discount}</td>
                    <td>${featured_icon}</td>
                    <td>${product.fields.updated_at}</td>
                </tr>
            `;
            productListElement.append(product_row)
        })
    }
}


    
$(document).ready(function(){

    // Discount Options
    $('#discount').change(function() {
        var discount_value = $(this).val();
        $.ajax({
            url: '/search/',
            method: 'POST',
            data: {
                discountval: discount_value,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response){
                renderpoducts(response)
            }
        })
    })


    
    // featured Options
    $('#featured').change(function() {
        var discount_value = $(this).val();
        var featured_value = $(this).val();
        $.ajax({
            url: '/search/',
            method: 'POST',
            data: {
                discountval: discount_value,
                featuredval: featured_value,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response){
                renderpoducts(response)
            }
        })
    })


    // Search field 
    $('#search_field').on('input',function(){
        var inputVal = $(this).val()
        // console.log(inputVal)
        $.ajax({
            url: '/search/',
            method: 'POST',
            data: {
                'inputval': inputVal,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response){
                renderpoducts(response)
            }
        })
    })
})