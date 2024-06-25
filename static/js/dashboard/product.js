// Function to generate random id 
const generateRandomID = (length = 6) => {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
  }



// Script of uploading thumbnail image
const fileInput = document.getElementById('file');
if(fileInput){
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0]; // Getting the image
    const imgUrl = URL.createObjectURL(file); // Making image url
    const img = document.createElement('img'); // Creating img tag 
    img.src = imgUrl; // setting img tag source code to the image url created
    const previewContainer = document.getElementById('input-thumbnail'); // getting the thumbnail container
    previewContainer.innerHTML = ''; // Emptying the thumbnail container 
    previewContainer.appendChild(img); // Adding the created img tag into thumbnail container
    addImageToDatabase(file,true)
});
}



// Script for making addimage button function
const addimage = document.getElementById('addimage');
addimage.addEventListener('change', (event) => {
    const file = event.target.files[0];
    addImageToDatabase(file)
});



// Script for adding image into image gallary
function add_image_to_imageGallary(id,url,defaultImage=false){
    const image_gallary = document.getElementById('image-gallary');
    let default_image_content = ''
    if(defaultImage){
        default_image_content = `<input type="radio" name="default_image" id="default_image" value="${id}" checked>`
    }
    else{
        default_image_content = `<input type="radio" name="default_image" id="default_image" value="${id}">`
    }
    const image = `<div class="image" id="${id}">
              <div>
                  <img src="${url}" alt="">
              </div>
              <div class="image-action-buttons default-image">
                    ${default_image_content}
              </div>
              <div class="image-action-buttons">
                    <input class="dlt-btn" type="text" name="${id}" value="${url}">
                    <img width="100" height="100" src="https://img.icons8.com/plasticine/100/filled-trash.png" alt="filled-trash" onclick='deleteImage(${id})'/>
              </div>
          </div>`
      image_gallary.innerHTML += image;
  }



// Ajax call for adding image into 
function addImageToDatabase(file,defaultImg=false){
    // Create FormData object and append the file
    const formData = new FormData();
    formData.append('image', file);
    fetch('/add-product-image/', {
        method: 'POST',
        body: formData,
        headers: {
        'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if(defaultImg){
                add_image_to_imageGallary(data.image_id,data.image_url,true)
            }
            else{
                add_image_to_imageGallary(data.image_id,data.image_url)
            }
        } else {
        console.error('Error uploading image');
        }
    })
    .catch(error => console.error('Error:', error));
}


function deleteImage(id){
    var image = document.getElementById(id)
    image.remove()
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}