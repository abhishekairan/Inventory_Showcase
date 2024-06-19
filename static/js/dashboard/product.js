const generateRandomID = (length = 6) => {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
  }


const fileInput = document.getElementById('file');
if(fileInput){
fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const imgUrl = URL.createObjectURL(file);
  const img = document.createElement('img');
  img.src = imgUrl;
  const previewContainer = document.getElementById('input-thumbnail');
  previewContainer.innerHTML = '';
  previewContainer.appendChild(img);
  const image_gallary = document.getElementById('image-gallary');
  const image = `
            <div class="image" id="-1">
                <div>
                    <img src="${imgUrl}" alt="">
                </div>
                <div class="image-action-buttons default-image">
                    <input type="radio" name="default_image" id="default_image" value="-1" checked>
                </div>
                    <div class="image-action-buttons">
                        <input class="dlt-btn" type="button" onclick='deleteImage(-1)' name="image-0" value="${imgUrl}">
                    </input>
                    <img width="100" height="100" src="https://img.icons8.com/plasticine/100/filled-trash.png" alt="filled-trash"/>
                    </div>
            </div>`
    image_gallary.innerHTML += image;
});
}

const addimage = document.getElementById('addimage');

addimage.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const imgUrl = URL.createObjectURL(file);
  const image_gallary = document.getElementById('image-gallary');
  const id = generateRandomID()
  const image = `
            <div class="image" id="${id}">
                <div>
                    <img src="${imgUrl}" alt="">
                </div>
                <div class="image-action-buttons default-image">
                    <input type="radio" name="default_image" id="default_image" value="${imgUrl}}">
                </div>
                    <div class="image-action-buttons">
                        <input class="dlt-btn" type="text" onclick='deleteImage(${id})' name="image-${id}" value="${imgUrl}">
                    </input>
                    <img width="100" height="100" src="https://img.icons8.com/plasticine/100/filled-trash.png" alt="filled-trash"/>
                    </div>
            </div>`
    image_gallary.innerHTML += image;
});



function deleteImage(id){
    var image = document.getElementById(id)
    console.log(image)
    image.remove()
}