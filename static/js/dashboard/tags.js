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
    var tags = Array.isArray(response) ? response : [response]
    // console.log(tags)
    var productListElement = $('#product-list');
    productListElement.empty();
    if(JSON.parse(tags[0].input_value).length > 0){
        JSON.parse(tags[0].input_value).forEach(function(tag){
            // console.log(product)
            const featured_icon = tag.fields.display ? '<img width="24" height="24" src="https://img.icons8.com/color/48/checked--v1.png" alt="checked--v1"/>' : '<img width="24" height="24" src="https://img.icons8.com/color/48/cancel--v1.png" alt="cancel--v1"/>';
            var product_row = `
                <tr data-url="{% url "dashboard" %}">
                    <td>${tag.pk}</td>
                    <td>${tag.fields.name}</td>
                    <td>${tag.fields.display_name}</td>
                    <td>${tag.fields.description}</td>
                    <td>${tag.fields.main_category}</td>
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
    // console.log(featured_value)
    $.ajax({
        url: '/search/tags/',
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