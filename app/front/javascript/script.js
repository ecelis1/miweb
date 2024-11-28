window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btnScrollToTop").style.display = "block";
    } else {
        document.getElementById("btnScrollToTop").style.display = "none";
    }
}

// Al hacer clic en el botón, desplazarse hacia arriba de la página
function topFunction() {
    document.body.scrollTop = 0; // Para Safari
    document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE y Opera
}


//Tomar Valores del Carrito y Shipping

async function handleCheckout() {
    const items = [];
    document.querySelectorAll('.product-card').forEach(card => {
        const id = card.dataset.id;
        const quantity = card.querySelector('.quantity-input').value;
        if (quantity > 0) {
            items.push({ id: parseInt(id), quantity: parseInt(quantity) });
        }
    });

    const shippingInfo = {
        fullName: document.getElementById('fullName').value,
        address: document.getElementById('address').value,
        city: document.getElementById('city').value,
        zipCode: document.getElementById('zipCode').value,
        country: document.getElementById('country').value
    };

    try {
        const response = await fetch('/create-preference', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ items, shippingInfo })
        });
        
        const data = await response.json();
        window.location.href = `https://www.mercadopago.com.ar/checkout/v1/redirect?preference-id=${data.id}`;
    } catch (error) {
        console.error('Error:', error);
    }
}
