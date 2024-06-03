const products = [
    // Add 100 or more product objects here in the format below
    {
        img: 'image-placeholder.jpg',
        title: 'Product 1',
        description: 'Description 1',
        price: '₹459',
        originalPrice: '₹2,999',
        discount: '84% off',
        badge: 'EOSS Special Deal'
    },
    // Repeat similar objects for other products
];

const productsPerPage = 100;
let currentPage = 1;

function displayProducts(page) {
    const productGrid = document.getElementById('product-grid');
    productGrid.innerHTML = '';
    
    const start = (page - 1) * productsPerPage;
    const end = page * productsPerPage;
    const paginatedProducts = products.slice(start, end);

    paginatedProducts.forEach(product => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        
        productCard.innerHTML = `
            <img src="${product.img}" alt="${product.title}">
            <div class="details">
                <h2>${product.title}</h2>
                <p>${product.description}</p>
                <div class="price">${product.price} <span class="original-price">${product.originalPrice}</span></div>
                <div class="discount">${product.discount}</div>
            </div>
            <div class="badge">${product.badge}</div>
        `;
        
        productGrid.appendChild(productCard);
    });
    
    document.getElementById('page-number').innerText = page;
}

function nextPage() {
    const totalPages = Math.ceil(products.length / productsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayProducts(currentPage);
    }
}

function previousPage() {
    if (currentPage > 1) {
        currentPage--;
        displayProducts(currentPage);
    }
}

// Initialize the product grid
displayProducts(currentPage);
