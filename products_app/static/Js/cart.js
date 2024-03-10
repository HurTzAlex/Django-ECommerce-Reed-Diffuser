let cartModalVisible = false;

function toggleModalCart() {
    if (cartModalVisible) {
        closeModalCart();
    } else {
        openModalCart();
    }
}

function openModalCart() {
    $("#modal-cart").css('display', 'flex');

    setTimeout(() => {
        $('#modal-cart').css({
            "opacity": '1',
            "transform": "translateX(0)",
        });
    }, 50);

    cartModalVisible = true;
}

function closeModalCart() {
    $('#modal-cart').css({
        'opacity': '0',
        'transform': 'translateX(300px)',
    });

    setTimeout(() => {
        $('#modal-cart').css('display', 'none');
    }, 300);

    cartModalVisible = false;
}



// Buy Modal
function openModalBuy() {
    
}