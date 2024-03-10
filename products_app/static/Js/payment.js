let buyModalTimeout;

function openModalBuy() {
    clearTimeout(buyModalTimeout);

    if ($("#modal-buy").css("display") === "none") {
        $("#modal-buy").css("display", "flex");
        
        buyModalTimeout = setTimeout(() => {
            $("#modal-buy").css({
                "opacity": "1",
                "transform": "translateX(0)",
            });
        }, 50);
    } else {
        closeModalBuy();
    }
}

function closeModalBuy() {
    $("#modal-buy").css({
        "opacity": "0",
        "transform": "translateX(-300px)",
    });

    clearTimeout(buyModalTimeout);

    setTimeout(() => {
        $("#modal-buy").css("display", "none");
    }, 300);
}

function clearModalBuy() {
        // Clear input values
        document.getElementById("fullnameFormP").value = "";
        document.getElementById("emailFormP").value = "";
        document.getElementById("telephoneFormP").value = "";
        document.getElementById("addressFormP").value = "";
    
}

