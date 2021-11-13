function add_to_cart(id, name, price) {
    fetch("/api/cart", {
        method: "post",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: id,
            name: name,
            price: price
        })
    }).then(res => res.json()).then(data => {
        var cart = document.getElementById("cartId")
        cart.innerText = data.quantity
        var amount = document.getElementById("cartAmount")
        amount.innerText = data.sum_cart + " VND"
    })
}

function delete_product(productId) {
    var c = confirm("Ban chac chan xoa khong?");
    if (c == true) {
        fetch("/api/products/" + productId, {
            method: "delete"
        }).then(function(res) {
            return res.json();
        }).then(function(data) {
            console.info(data);
            var proId = data.data.product_id;
            var p = document.getElementById("product" + proId);
            p.style.display = "none";
        }).catch(function(err) {
            console.error(err);
        });
    }
}

function pay() {
    if (confirm("Bạn chắc chắn thanh toán?") == true) {
        fetch("/api/pay", {
            "method": "post",
            "headers": {
                "Content-Type": "application/json"
            }
        }).then(res => res.json()).then(data => {
            if (data.status == 200) {
                location.reload()
            } else {
                alert("Thanh toán thất bại")
            }
        }).catch(err => alert("HỆ THỐNG LỖI!!!"))
    }
}