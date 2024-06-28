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
    var users = Array.isArray(response) ? response : [response]
    console.log(users)
    var productListElement = $('#product-list');
    productListElement.empty();
    if(JSON.parse(users[0].input_value).length > 0){
        JSON.parse(users[0].input_value).forEach(function(user){
            console.log(user)
            const featured_icon = user.fields.is_superuser ? '<img width="24" height="24" src="https://img.icons8.com/color/48/checked--v1.png" alt="checked--v1"/>' : '<img width="24" height="24" src="https://img.icons8.com/color/48/cancel--v1.png" alt="cancel--v1"/>';
            var product_row = `
                <tr data-url="{% url "dashboard" %}">
                    <td>${user.pk}</td>
                    <td>${user.fields.username}</td>
                    <td>${user.fields.firstname} ${user.fields.last_name}</td>
                    <td>${user.fields.email}</td>
                    <td>${user.fields.date_joined}</td>
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
        url: '/search/users/',
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